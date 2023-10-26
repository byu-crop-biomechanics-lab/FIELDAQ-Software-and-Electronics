import zmq
from topics import Topic

ZMQ_PORT = 5555

class Publisher:
    def __init__(self, topic: Topic):
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f'tcp://*:{ZMQ_PORT}')

    def publish(self, message):
        self.socket.send_string(f"{self.topic.name} {message}")

    def close(self):
        self.socket.close()
        self.context.term()
            
    def __del__(self):
        self.close()



if __name__ == '__main__':
    import time
    start_time = time.time()
    pub = Publisher(Topic.LOAD1)
    i = 0
    while time.time() - start_time < 10:
        pub.publish(f'test: {i}')
        i += 1
        time.sleep(0.25)
        # time.sleep(10)
    pub.close()