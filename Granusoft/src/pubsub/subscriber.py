import zmq
import threading
from topics import Topic
from collections.abc import Callable
import signal
import json
import time

ZMQ_PORT = 5555

import zmq
import json
import signal
import threading
import time
from typing import Callable
from .topic import Topic

class Subscriber:
    '''
    Class for subscribing to a topic.

    This class provides functionality for subscribing to a topic using ZeroMQ (ZMQ) sockets. It allows the user to receive messages from the subscribed topic either by blocking and waiting for a message to be received, or by providing a callback function to be called when a message is received. The messages are expected to be in JSON format.

    Attributes:
        _socket_timeout (int): The timeout for the ZMQ socket in milliseconds.
        _subscribed_topic (Topic): The topic that the subscriber is subscribed to.
        _context (zmq.Context): The ZMQ context object.
        _socket (zmq.Socket): The ZMQ socket object.
        _poller (zmq.Poller): The ZMQ poller object.
        _shutdown (bool): A flag indicating whether the subscriber has been shut down.
        _callback (Callable): An optional callback function to be called when a message is received. The callback function must take a single argument which will be the data received.
        _callback_thread (threading.Thread): The thread object for the callback function.

    Methods:
        __init__(self, topic: Topic, optional_callback: Callable = None): Initializes a subscriber object.
        receive(self): Receives a message from the subscribed topic.
        close(self): Closes the subscriber object.
        _listen(self): Listens for messages from the subscribed topic.
        _shutdwn_handler(self, sig, frame): Signal handler for SIGINT.
        __del__(self): Destructor for the subscriber object. This is called automatically when the object is deleted.
    '''
class Subscriber:
    '''
    Class for subscribing to a topic.
    
    
    '''
    def __init__(self, topic: Topic, optional_callback: Callable = None):
        '''
        Initialize a subscriber object.
        
        This contructs a socket, connects it to the ZMQ_PORT, and sets the topic to the given topic.
        
        Args:
            topic (Topic): The topic to subscribe to.
            [Optional] optional_callback (Callable): An optional callback function to be called when a message is received. The callback function must take a single argument which will be the data received.
            
        Returns:
            None
            
        Raises:
            TypeError: If optional_callback is not a function.
        '''
        self._socket_timeout = 1 # ms
        self._subscribed_topic = topic
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.connect(f'tcp://localhost:{ZMQ_PORT}')
        self._socket.setsockopt_string(zmq.SUBSCRIBE, topic.name) 
        self._poller = zmq.Poller()
        self._poller.register(self._socket, zmq.POLLIN)
        self._shutdown = False 
        signal.signal(signal.SIGINT, self._shutdwn_handler)
        
        self._callback = optional_callback
        self._callback_thread = None
        if self._callback is not None:
            if not isinstance(self._callback, Callable):
                raise TypeError("optional_callback must be a function")
            self._callback_thread = threading.Thread(target=self._listen)
            self._callback_thread.start()

    def receive(self):
        '''
        Receive a message from the subscribed topic.
        
        This function blocks until a message is received from the subscribed topic. The message is returned as a python dictionary.
        
        Args:
            None
            
        Returns:
            dict: A python dictionary containing the data received.
        '''
        while not self._shutdown:
            try:
                socks = dict(self._poller.poll(self._socket_timeout))
            except zmq.error.ZMQError as e:
                # Supress this error as it occurs when the socket is closed before the poller finishes its update. This can occur
                # in various ways depending on when the user calls close() and recive(). The error is harmless as it simply indicates 
                # that the socket was closed and can be ignored.
                if e != 'Socket operation on non-socket':
                    print(e)
            if self._socket in socks and socks[self._socket] == zmq.POLLIN:
                data = self._socket.recv().split()
                # topic = data[0].decode('utf-8')
                messagedata = (b' '.join(data[1:])).decode('utf-8')
                data = json.loads(messagedata)
                return data
            
    def close(self):
        '''
        Close the subscriber object.
        
        This closes the socket and terminates the context.
        
        Args:
            None
            
        Returns:
            None
        '''
        self._socket.close()
        self._context.term()
    
    def _listen(self):
        '''
        Listen for messages from the subscribed topic.
        
        This function is called in a separate thread when a callback function is given to the constructor. It blocks until a message is received from the subscribed topic. The message is passed to the callback function as a python dictionary.
        
        Args:
            None
            
        Returns:
            None
        '''
        while not self._shutdown:
            socks = dict(self._poller.poll(self._socket_timeout))
            if self._socket in socks and socks[self._socket] == zmq.POLLIN:
                data = self._socket.recv().split()
                # topic = data[0].decode('utf-8')
                messagedata = (b' '.join(data[1:])).decode('utf-8')
                data = json.loads(messagedata)
                self._callback(data)

    def _shutdwn_handler(self, sig, frame):
        '''
        Signal handler for SIGINT.
        
        This function is called when SIGINT is received. It sets the shutdown flag to True.
        
        Args:
            sig: The signal number.
            frame: The current stack frame.
            
        Returns:
            None
        '''
        self.__del__()
        
    def __del__(self):
        '''
        Destructor for the subscriber object. This is called automatically when the object is deleted.
        
        This calls the close() method.
        
        Args:
            None
            
        Returns:
            None
        '''
        self._shutdown = True
        if self._callback_thread is not None:
            self._callback_thread.join()
        time.sleep(self._socket_timeout/1000) # Let socket polling close before closing the socket
        self.close()