from logic import parser
from TUI.terminal import HostTUI
from pathlib import Path
from logic.config import GameConfig

BASE_DIR = Path(__file__).parent

if __name__ == "__main__":
    with open(BASE_DIR / "questions.txt", "r") as f:
        questions = f.read().splitlines()
    with open(BASE_DIR / "participants.txt", "r") as f:
        participants = f.read().splitlines()

    parser_instance = parser.Parser(participants, questions)
    parser_instance.parse_participants()
    parser_instance.parse_questions()
    parser_instance.isParsedCorrectly()

    config = GameConfig()
    prowadzacy = HostTUI(parser_instance.questions, parser_instance.answers, parser_instance.participants, config)
    prowadzacy.run()
