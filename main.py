from logic import parser

if __name__ == "__main__":
    with open("questions.txt","r") as f:
        questions = f.read().splitlines()
    with open("participants.txt","r") as f:
        participants = f.read().splitlines()

    parser_instance = parser.Parser(participants, questions)
    parser_instance.parse_participants()
    parser_instance.parse_questions()
    parser_instance.isParsedCorrectly()
    print("Participants:", parser_instance.participants)
    print("Questions:", parser_instance.questions)
    print("Answers:", parser_instance.answers)
