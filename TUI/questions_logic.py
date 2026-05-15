from logic.question_status import QuestionStatus
from logic.bank import Bank


class QuestionsLogic:
    parsed_questions: list[str] = []
    parsed_answers: list[str] = []
    parsed_participants: list[str] = []
    current_question: str
    current_answer: str
    current_participant: str
    bank: Bank

    def __init__(self, questions: list[str], answers: list[str], participants: list[str]):
        self.questions = questions
        self.answers = answers
        self.participants = participants
        self.bank = Bank(0)

        if len(self.questions) > 0 and len(self.answers) > 0 and len(self.participants) > 0:
            self._current_question = self.questions[0]
            self._current_answer = self.answers[0]
            self._current_participant = self.participants[0]
        else:
            raise ValueError("The lists of questions, answers, and participants cannot be empty.")

    @property
    def current_question(self) -> str:
        """Returns the current question."""
        return self._current_question

    @property
    def current_answer(self) -> str:
        """Returns the current answer."""
        return self._current_answer

    @property
    def bank_chain(self) -> int:
        """Returns the current amount of money in the bank."""
        return self.bank._current_chain_position

    def question_answered(self, answer_status: QuestionStatus) -> tuple[str, str, str, int]:
        """Updates the current question, answer, participant, and bank chain position based on the status of the answered question.
        Args:
            answer_status (QuestionStatus): The status of the answered question, indicating whether it was answered correctly or incorrectly.
        Returns:
            tuple[str, str, str, int]: A tuple containing the updated current question, answer, participant, and bank chain position."""

        if answer_status == QuestionStatus.ANSWERED_CORRECTLY:
            """ Update the question status to answered correctly"""

            self.bank.correct_answer()
            self._current_question = self.questions[
                self.questions.index(self._current_question) + 1
            ]
            self._current_answer = self.answers[
                self.answers.index(self._current_answer) + 1
                ]
            if self._current_participant == self.participants[-1]:
                self._current_participant = self.participants[0]
            else:
                self._current_participant = self.participants[
                    self.participants.index(self._current_participant) + 1
                ]
            return self._current_question, self._current_answer, self._current_participant, self.bank_chain

        elif answer_status == QuestionStatus.ANSWERED_INCORRECTLY:
            """ Update the question status to answered incorrectly"""

            self.bank.incorrect_answer()
            self._current_question = self.questions[
                self.questions.index(self._current_question) + 1
            ]
            self._current_answer = self.answers[
                self.answers.index(self._current_answer) + 1]
            if self._current_participant == self.participants[-1]:
                self._current_participant = self.participants[0]
            else:
                self._current_participant = self.participants[
                    self.participants.index(self._current_participant) + 1
                ]
            return self._current_question, self._current_answer, self._current_participant, self.bank_chain
        
    def bank_money(self) -> int:
        """Banks the current amount of money and resets the current question."""

        self.bank.bank_money()
        return self.bank.current_amount
