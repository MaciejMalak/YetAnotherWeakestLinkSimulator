from logic import parser
from logic import bank
from TUI.terminal import HostTUI

if __name__ == "__main__":
    with open("questions.txt","r") as f:
        questions = f.read().splitlines()
    with open("participants.txt","r") as f:
        participants = f.read().splitlines()

    parser_instance = parser.Parser(participants, questions)
    parser_instance.parse_participants()
    parser_instance.parse_questions()
    parser_instance.isParsedCorrectly()

    prowadzacy = HostTUI()
    prowadzacy.run()


