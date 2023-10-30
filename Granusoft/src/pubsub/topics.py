from enum import Enum, auto

class Topic(Enum):
    '''
    Enum class for publishable topics.

    This class defines the available topics that can be published to the message broker.

    Attributes:
        ARM_SENSORS: A topic for publishing data from the arm sensors.
        DARLING_SENSORS: A topic for publishing data from the darling sensors.
        CAMERA_SENSORS: A topic for publishing data from the camera sensors.
        DOGBONE_SENSORS: A topic for publishing data from the dogbone sensors.
        STALK_STIFFNESS: A topic for publishing data of the stalk stiffness.
    '''
    ARM_SENSORS = auto()
    DARLING_SENSORS = auto()
    CAMERA_SENSORS = auto()
    DOGBONE_SENSORS = auto()
    STALK_STIFFNESS = auto()
    