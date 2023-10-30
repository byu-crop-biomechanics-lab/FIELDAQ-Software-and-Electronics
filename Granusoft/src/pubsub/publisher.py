import zmq
from topics import Topic
import json

ZMQ_PORT = 5555

class Publisher:
    '''
    Class for publishing data to a topic using ZeroMQ.

    This class is used to publish data to a topic using ZeroMQ. The topic must be one of the topics defined in the Topic enum class.

    Attributes:
        topic (Topic): The topic to publish to.
        context (zmq.Context): The ZeroMQ context object.
        socket (zmq.Socket): The ZeroMQ socket object.

    Methods:
        __init__(self, topic: Topic): Initializes a publisher object.
        publish(data: dict): Publishes a message to the topic of the publisher.
        close(): Closes the publisher object.
        __del__(): Destructor for the publisher object.

    Raises:
        TypeError: If data is not a python dictionary.

    Example:
        # Create a publisher object for the "temperature" topic
        publisher = Publisher(Topic.TEMPERATURE)

        # Publish a message to the "temperature" topic
        data = {"value": 25.0, "unit": "C"}
        publisher.publish(data)

        # Close the publisher object
        publisher.close()
    '''

    def __init__(self, topic: Topic):
        '''
        Initializes a publisher object.

        This constructs a socket, binds it to the ZMQ_PORT, and sets the topic to the given topic.

        Args:
            topic (Topic): The topic to publish to.

        Returns:
            None
        '''
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f'tcp://*:{ZMQ_PORT}')

    def publish(self, data: dict):
        '''
        Publishes a message to the topic of the publisher.

        This function serializes the data to JSON and publishes it to the topic of the publisher.

        Args:
            data (dict): A python dictionary containing the data to be published. The dictionary must be JSON serializable.

        Returns:
            None

        Raises:
            TypeError: If data is not a python dictionary.
        '''
        if not isinstance(data, dict):
            raise TypeError("data must be a python dictionary")
        message_string = json.dumps(data)
        self.socket.send_string(f"{self.topic.name} {message_string}")

    def close(self):
        '''
        Closes the publisher object.

        This closes the socket and terminates the context.

        Args:
            None

        Returns:
            None
        '''
        self.socket.close()
        self.context.term()

    def __del__(self):
        '''
        Destructor for the publisher object. This is called automatically when the object is deleted.

        This calls the close() method.

        Args:
            None

        Returns:
            None
        '''
        self.close()