from kivy.logger import Logger

class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
            Logger.debug(f'Constructor: creating new {cls.__name__}')
        else:
            Logger.debug(f'Constructor: {cls.__name__} already exists')
        return cls.instance