from blessed import Terminal
import time


class HostTUI:
    """Terminal User Interface for the host of the weakest link simulator.
    Provides a visual interface for the host to manage the game, display questions, and track the current state of the game.
    
    Attributes:
        term (Terminal): An instance of the Terminal class from the blessed library, used for terminal
        manipulation.
        running (bool): A flag to indicate whether the TUI is currently running."""
    def __init__(self):
        """Initializes the HostTUI with a Terminal instance and sets the running flag to True."""
        self.term = Terminal()
        self.running = True

    def draw_screen(
        self, question: str, chain: int, bank: int, time_left, participant: str
    ):
        """Draws the TUI screen with the current question, chain position, bank amount, time left, and current participant."""
        print(self.term.clear, end="")
        height = self.term.height
        print(
            self.term.move_y(0)
            + self.term.black_on_white(
                self.term.center("=== YAWSS: Panel Prowadzącego ===")
            )
        )
        print(self.term.move_y(2) + self.term.center(f"Pytanie: {question}"))
        print(self.term.move_y(4) + self.term.center(f"Łańcuch: {chain}"))
        print(self.term.move_y(6) + self.term.center(f"Bank: {bank}"))
        print(
            self.term.move_y(8) + self.term.center(f"Czas do odpowiedzi: {time_left}")
        )
        print(
            self.term.move_y(10) + self.term.center(f"Obecny uczestnik: {participant}")
        )
        print(
            self.term.move_y(height - 2)
            + self.term.center(
                "[Spacja] Odpowiedź poprawna | [Backspace] Odpowiedź niepoprawna | [Enter] Bankowanie"
            )
        )

    def run(self):
        """Runs the TUI, allowing the host to interact with the game by pressing keys to indicate correct or incorrect answers, or to bank the current amount."""
        with self.term.fullscreen(), self.term.hidden_cursor(), self.term.cbreak():
            current_question = "Jakie jest największe jezioro na świecie?"
            bank = 1500
            time_left = 30
            participant = "Jan Kowalski"
            chain = 1
            while self.running:
                self.draw_screen(current_question, chain, bank, time_left, participant)
                key = self.term.inkey(timeout=0.1)
                if key.lower() == " ":
                    print(
                        self.term.move_y(12) + self.term.center("Odpowiedź poprawna!")
                    )
                elif key.code == self.term.KEY_BACKSPACE:
                    print(
                        self.term.move_y(12)
                        + self.term.center("Odpowiedź niepoprawna!")
                    )
                elif key.code == self.term.KEY_ENTER:
                    print(self.term.move_y(12) + self.term.center("Bankowanie!"))
                elif key.lower() == "q":
                    self.running = False
                time.sleep(0.3)
