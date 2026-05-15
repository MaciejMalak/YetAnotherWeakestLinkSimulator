from logic.question_status import QuestionStatus
from logic.bank import Bank


class QuestionsLogic:
    parsed_questions: list[str] = []
    current_question: str
    bank: Bank

    def __init__(self, questions: list[str]):
        self.questions = questions
        self.bank = Bank(0)

        if len(self.questions) > 0:
            self._current_question = self.questions[0]
        else:
            raise ValueError("The list of questions cannot be empty.")

    @property
    def current_question(self) -> str:
        """Returns the current question."""
        return self._current_question

    @property
    def bank_chain(self) -> int:
        """Returns the current amount of money in the bank."""
        return self.bank._current_chain_position

    def question_answered(self, answer_status: QuestionStatus) -> tuple[str, int]:
        """Updates the question and bank based on the answer status."""

        if answer_status == QuestionStatus.ANSWERED_CORRECTLY:
            """ Update the question status to answered correctly"""
            self.bank.correct_answer()
            self._current_question = self.questions[
                self.questions.index(self._current_question) + 1
            ]
            return self._current_question, self.bank_chain

        elif answer_status == QuestionStatus.ANSWERED_INCORRECTLY:
            """ Update the question status to answered incorrectly"""
            self.bank.incorrect_answer()
            self._current_question = self.questions[
                self.questions.index(self._current_question) + 1
            ]
            return self._current_question, self.bank_chain
