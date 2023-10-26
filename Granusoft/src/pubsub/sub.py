import zmq
import threading
from topics import Topic
import signal

ZMQ_PORT = 5555

class Subscriber:
    def __init__(self, topic: Topic, optional_callback = None):
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
            self._callback_thread = threading.Thread(target=self._listen)
            self._callback_thread.start()

    def receive(self):
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
                return messagedata
            
    def close(self):
        self._socket.close()
        self._context.term()
    
    def _listen(self):
        while not self._shutdown:
            socks = dict(self._poller.poll(self._socket_timeout))
            if self._socket in socks and socks[self._socket] == zmq.POLLIN:
                data = self._socket.recv().split()
                # topic = data[0].decode('utf-8')
                message = (b' '.join(data[1:])).decode('utf-8')
                self._callback(message)

    def _shutdwn_handler(self, sig, frame):
        self.__del__()
        
    def __del__(self):
        self._shutdown = True
        if self._callback_thread is not None:
            self._callback_thread.join()
        time.sleep(self._socket_timeout/1000) # Let socket polling close before closing the socket
        self.close()
        
        
        
def callback(message):
    print(message)
            
if __name__ == '__main__':
    # import time
    # start_time = time.time()
    # sub = Subscriber(Topic.LOAD1, optional_callback=callback)
    # while time.time() - start_time < 10 and not sub._shutdown:
    #     time.sleep(0.001)
    # sub.close()
    
    import time
    start_time = time.time()
    sub = Subscriber(Topic.LOAD1)
    while time.time() - start_time < 10 and not sub._shutdown:
        time.sleep(0.001)
        print(sub.receive())
    sub.close()