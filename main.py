from logic import parser
from logic import bank

if __name__ == "__main__":
    with open("questions.txt","r") as f:
        questions = f.read().splitlines()
    with open("participants.txt","r") as f:
        participants = f.read().splitlines()

    parser_instance = parser.Parser(participants, questions)
    parser_instance.parse_participants()
    parser_instance.parse_questions()
    parser_instance.isParsedCorrectly()

    # Tests to check if the parser is working correctly
    print("Participants:", parser_instance.participants)
    print("Questions:", parser_instance.questions)
    print("Answers:", parser_instance.answers)

    # Tests to check if the bank is working correctly
    bank_instance = bank.Bank(0)
    print(bank_instance)
    bank_instance.correct_answer()
    print(bank_instance)
    bank_instance.correct_answer()
    print(bank_instance)
    bank_instance.incorrect_answer()
    print(bank_instance)
    bank_instance.correct_answer()
    print(bank_instance)
    bank_instance.bank_money()
    print(bank_instance)

