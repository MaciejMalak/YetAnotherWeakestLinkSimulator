class Parser:
    """A class that parses the participants and questions from the input files.

    Attributes:
        participants (list[str]): A list of participants' names.
        questions (list[str]): A list of questions.
    """

    def __init__(self, participants: list[str], questions: list[str]):
        self.participants = participants
        self.questions_unformated = questions
        self._answers: list[str] = []
        self._questions: list[str] = []

    def isCommentOrEmpty(self, line: str) -> bool:
        """Checks if a line is a comment or empty."""
        return line.startswith("#") or line.strip() == ""

    def parse_participants(self) -> list[str]:
        """Removes empty lines and comments from the participants list, and strips whitespace from each participant's name."""
        for participant in self.participants:
            if self.isCommentOrEmpty(participant):
                self.participants.remove(participant)
            else:
                self.participants[self.participants.index(participant)] = (
                    participant.strip()
                )
        return self.participants

    def parse_questions(self) -> list[str]:
        """Removes empty lines and comments from the questions list, and strips whitespace from each question."""
        for question in self.questions_unformated:
            if self.isCommentOrEmpty(question):
                self.questions_unformated.remove(question)
            else:
                question_split = question.split("|")
                self.questions.append(question_split[0].strip())
                self.answers.append(question_split[1].strip())

        return self.questions

    def isParsedCorrectly(self) -> bool:
        """Checks if the number of questions and answers are the same."""
        if len(self.questions) != len(self.answers):
            raise ValueError("The number of questions and answers must be the same.")
        return True

    @property
    def answers(self) -> list[str]:
        """Returns the list of answers."""
        return self._answers

    @answers.setter
    def answers(self, value: list[str]):
        """Sets the list of answers."""
        self._answers = value

    @property
    def questions(self) -> list[str]:
        """Returns the list of questions."""
        return self._questions

    @questions.setter
    def questions(self, value: list[str]):
        """Sets the list of questions."""
        self._questions = value

    @property
    def participants(self) -> list[str]:
        """Returns the list of participants."""
        return self._participants

    @participants.setter
    def participants(self, value: list[str]):
        """Sets the list of participants."""
        self._participants = value
