from blessed import Terminal
from logic.config import GameConfig
from logic.timer import GameTimer
from logic.question_status import QuestionStatus
from TUI.questions_logic import QuestionsLogic
from logic.discord_notifier import DiscordNotifier
import time


class HostTUI:
    """Terminal User Interface for the host of the weakest link simulator.
    Provides a visual interface for the host to manage the game, display questions, and track the current state of the game.
    
    Attributes:
        term (Terminal): An instance of the Terminal class from the blessed library, used for terminal
        manipulation.
        running (bool): A flag to indicate whether the TUI is currently running."""
    def __init__(self, questions: list[str], answers: list[str], participants: list[str], config: GameConfig):
        """Initializes the HostTUI with a Terminal instance and sets the running flag to True."""
        self.term = Terminal()
        self.running = True
        self.questions_logic = QuestionsLogic(questions, answers, participants)
        self.time_available = True
        self.config = config
        self.notifier = DiscordNotifier(config.discord_url, config.discord_embed_color)

    def draw_screen(
        self, question: str, answer: str, chain_drawn: str, bank: int, time_left: int, participant: str
    ):
        """Draws the TUI screen with the current question, chain position, bank amount, time left, and current participant."""
        print(self.term.clear, end="")
        height = self.term.height
        width = self.term.width
        separator = self.term.bright_black("─" * width)


        print(
            self.term.move_y(1)
            + self.term.black_on_white(
                self.term.center("=== Yet Another Weakest Link Simulator : Host Panel ===")
            )
        )
        print(self.term.move_y(5) + self.term.center(f"Question: {question}"))
        print(self.term.move_y(6) + self.term.center(self.term.green(f"Answer: {answer}")))

        print(self.term.move_y(8) + separator)

        print(self.term.move_y(12) + self.term.center(f"Chain: {chain_drawn}"))
        print(self.term.move_y(13) + self.term.center(f"Bank: {bank}"))
        if self.time_available:
            print(
                self.term.move_y(15) + self.term.center(f"Time remaining: {time_left}")
            )
        else:
            print(self.term.move_y(15) + self.term.center(self.term.red("Time is up!")))
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
            timer = GameTimer(self.config.round_duration)
            timer.start_round()
            participant = "John Doe"
            chain = 0
            chain_drawn = "[--------]"

            now = time.time()
            end_time = now + timer.time_left
            self.notifier.send_game_update(current_question, participant, end_time, chain_drawn, bank)


            while self.running:

                if timer.time_left == 0 and self.time_available:
                    self.time_available = False
                    if self.config.auto_end_on_timeout:
                        self.running = False
                        print(self.term.move_y(14) + self.term.center("Game over! Time is up."))
                        self.notifier.freeze_old_message("__TIMEOUT__", participant, chain_drawn, bank)
                        self.notifier.send_disconnect_message()
                        break

                self.draw_screen(current_question, answer, chain_drawn, bank, timer.time_left, participant)
                key = self.term.inkey(timeout=0.1)
                    
                if key.lower() == " ":
                    print(
                        self.term.move_y(7) + self.term.center("Correct answer!")
                    )
                    timer.record_answer(participant)
                    current_question, answer, participant, chain = self.questions_logic.question_answered(QuestionStatus.ANSWERED_CORRECTLY)

                    if current_question == "__OUT_OF_QUESTIONS__":
                        self.running = False
                        print(self.term.move_y(14) + self.term.center("Game over! No more questions left."))
                        self.notifier.freeze_old_message(current_question, participant, chain_drawn, bank)
                        self.notifier.send_disconnect_message()
                        break

                    chain_drawn = self.questions_logic.draw_chain(chain)
                    now = time.time()
                    end_time = now + timer.time_left
                    self.notifier.send_game_update(current_question, participant, end_time, chain_drawn, bank)

                elif key.code == self.term.KEY_BACKSPACE:
                    print(
                        self.term.move_y(7)
                        + self.term.center("Incorrect answer!")
                    )
                    timer.record_answer(participant)
                    current_question, answer, participant, chain = self.questions_logic.question_answered(QuestionStatus.ANSWERED_INCORRECTLY)

                    if current_question == "__OUT_OF_QUESTIONS__":
                        self.running = False
                        print(self.term.move_y(14) + self.term.center("Game over! No more questions left."))
                        self.notifier.freeze_old_message(current_question, participant, chain_drawn, bank)
                        self.notifier.send_disconnect_message()
                        break

                    chain_drawn = self.questions_logic.draw_chain(chain)
                    now = time.time()
                    end_time = now + timer.time_left
                    self.notifier.send_game_update(current_question, participant, end_time, chain_drawn, bank)

                elif key.code == self.term.KEY_ENTER:
                    print(self.term.move_y(7) + self.term.center("Banking!"))
                    bank = self.questions_logic.bank_money()
                    chain = 0
                    chain_drawn = self.questions_logic.draw_chain(chain)

                    now = time.time()
                    end_time = now + timer.time_left
                    self.notifier.send_game_update(current_question, participant, end_time, chain_drawn, bank)

                elif key.lower() == "q":
                    self.running = False
                    print(self.term.move_y(7) + self.term.center("Game ended."))
                    self.notifier.freeze_old_message(current_question, participant, chain_drawn, bank)
                    self.notifier.send_disconnect_message()

                time.sleep(0.3)
