from enum import Enum, auto

class PomodoroState(Enum):
    IDLE = auto()
    WORK = auto()
    BREAK = auto()
