from blessed import Terminal
from logic.timer import GameTimer
from logic.question_status import QuestionStatus
from TUI.questions_logic import QuestionsLogic
import time


class HostTUI:
    """Terminal User Interface for the host of the weakest link simulator.
    Provides a visual interface for the host to manage the game, display questions, and track the current state of the game.
    
    Attributes:
        term (Terminal): An instance of the Terminal class from the blessed library, used for terminal
        manipulation.
        running (bool): A flag to indicate whether the TUI is currently running."""
    def __init__(self, questions: list[str], answers: list[str], participants: list[str]):
        """Initializes the HostTUI with a Terminal instance and sets the running flag to True."""
        self.term = Terminal()
        self.running = True
        self.questions_logic = QuestionsLogic(questions, answers, participants)
        self.time_available = True

    def draw_screen(
        self, question: str, answer: str, chain: int, bank: int, time_left: int, participant: str
    ):
        """Draws the TUI screen with the current question, chain position, bank amount, time left, and current participant."""
        print(self.term.clear, end="")
        height = self.term.height
        print(
            self.term.move_y(0)
            + self.term.black_on_white(
                self.term.center("=== Yet Another Weakest Link Simulator : Host Panel ===")
            )
        )
        print(self.term.move_y(2) + self.term.center(f"Question: {question}"))
        print(self.term.move_y(3) + self.term.center(self.term.green(f"Answer: {answer}")))
        print(self.term.move_y(4) + self.term.center(f"Chain: {chain}"))
        print(self.term.move_y(6) + self.term.center(f"Bank: {bank}"))
        if self.time_available:
            print(
                self.term.move_y(8) + self.term.center(f"Time remaining: {time_left}")
            )
        else:
            print(self.term.move_y(8) + self.term.center(self.term.red("Time is up!")))
        print(
            self.term.move_y(10) + self.term.center(f"Current participant: {participant}")
        )
        print(
            self.term.move_y(height - 2)
            + self.term.center(
                "[Space] Correct answer | [Backspace] Incorrect answer | [Enter] Bank"
            )
        )

    def run(self):
        """Runs the TUI, allowing the host to interact with the game by pressing keys to indicate correct or incorrect answers, or to bank the current amount."""
        with self.term.fullscreen(), self.term.hidden_cursor(), self.term.cbreak():
            current_question = "PRESS BACKSPACE TO INITIATE A QUESTION"
            answer = "Press space to mark the answer as correct"
            bank = 0
            timer = GameTimer(30)
            timer.start_round()
            participant = "John Doe"
            chain = 0
            while self.running:
                if timer.time_left == 0 and self.time_available:
                    self.time_available = False
                    print(self.term.move_y(8) + self.term.center(self.term.red("Time is up!")))
                self.draw_screen(current_question, answer, chain, bank, timer.time_left, participant)
                key = self.term.inkey(timeout=0.1)
                if key.lower() == " ":
                    print(
                        self.term.move_y(12) + self.term.center("Correct answer!")
                    )
                    timer.record_answer(participant)
                    current_question, answer, participant, chain = self.questions_logic.question_answered(QuestionStatus.ANSWERED_CORRECTLY)
                elif key.code == self.term.KEY_BACKSPACE:
                    print(
                        self.term.move_y(12)
                        + self.term.center("Incorrect answer!")
                    )
                    timer.record_answer(participant)
                    current_question, answer, participant, chain = self.questions_logic.question_answered(QuestionStatus.ANSWERED_INCORRECTLY)
                elif key.code == self.term.KEY_ENTER:
                    print(self.term.move_y(12) + self.term.center("Banking!"))
                    bank = self.questions_logic.bank_money()
                    chain = 0
                elif key.lower() == "q":
                    self.running = False
                    print(self.term.move_y(12) + self.term.center("Game ended."))
                time.sleep(0.3)
