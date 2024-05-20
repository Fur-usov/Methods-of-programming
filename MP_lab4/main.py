import datetime
import random
import time


class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        name = args[0]  # Используем имя в качестве ключа
        if name not in cls._instances:
            cls._instances[name] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[name]



# класс синглтон, логгирует события
class Logger(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"all_events.log", "a") as file:
            file.write(f"{timestamp} - {self.name.upper()} - {message}\n")


# класс эмуляции системы, генерирует случайные события
class System:
    def __init__(self):
        self.loggers = {
            "warning": Logger("warning"),
            "error": Logger("error"),
            "log": Logger("log"),
        }

    def emulate(self):
        messages = ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5"]    
        
        for _ in range(200):
            severity = random.choice(list(self.loggers.keys()))
            message = random.choice(messages)
            self.loggers[severity].log(message)
            time.sleep(0.05)


system = System()
system.emulate()
