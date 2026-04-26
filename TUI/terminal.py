from blessed import Terminal
import time


class HostTUI:
    def __init__(self):
        self.term = Terminal()
        self.running = True

    def draw_screen(
        self, question: str, chain: int, bank: int, time_left, participant: str
    ):
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
