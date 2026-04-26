from enum import Enum

class QuestionStatus(Enum):
    """Represents the status of a question in the weakest link simulator.
    """
    UNANSWERED = 0
    ANSWERED_CORRECTLY = 1
    ANSWERED_INCORRECTLY = -1