import time

class GameTimer:
    """Manages the timing for each round and tracks how long each participant takes to answer questions.
    Args:
        duration (int): The duration of each round in seconds.
    Attributes:
        duration (int): The duration of each round in seconds.
        start_time (float): The time when the round started.
        question_start_time (float): The time when the current question started.
        round_end_time (float): The time when the round will end."""

    def __init__(self, duration: int):
        """Initializes the GameTimer with a specified duration for each round and sets up the necessary attributes to track time."""

        self.duration = duration
        self.start_time = 0.0
        self.question_start_time = 0.0
        self.round_end_time = 0.0

        self.player_stats : dict[str, list[float]] = {}

    def start_round(self):
        """Starts a new round by recording the current time and calculating the end time for the round."""

        current_time = time.time()
        self.round_end_time = current_time + self.duration
        self.start_question()
    
    @property
    def time_left(self) -> int:
        """Calculates and returns the time left in the current round. If the round has ended, it returns 0."""

        return max(0, int(self.round_end_time - time.time()))
    
    def start_question(self):
        """Starts a new question by recording the current time as the start time for the question."""

        self.question_start_time = time.time()

    def record_answer(self, participant: str):
        """Records the time taken by a participant to answer the current question."""
        
        time_taken = time.time() - self.question_start_time
        if participant not in self.player_stats:
            self.player_stats[participant] = []
        self.player_stats[participant].append(time_taken)
        self.start_question()
