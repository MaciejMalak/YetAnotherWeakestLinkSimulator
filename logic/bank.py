class Bank:
    """Represents the bank in the game, which keeps track of the current amount of money and the current chain position.
    
    Attributes:
        current_amount (int): The current amount of money in the bank.
        current_chain_position (int): The current position in the value chain.
        value_chain (list[int]): A list of values for each position in the chain."""
    def __init__(self, amount: int | None):
        self._current_amount : int = amount if amount is not None else 0
        self._current_chain_position : int = 0
        self.value_chain = [0, 100, 300, 600, 900, 1300, 1800, 2400, 3000]

    def correct_answer (self):
        """Increases the current amount by the value of the question in the value chain."""
        self._current_chain_position += 1

    def incorrect_answer (self):
        """Resets the current amount to 0 and the current chain position to 0."""
        self._current_chain_position = 0

    def bank_money (self):
        """Adds the current amount to the total amount in the bank and resets the current amount and chain position."""
        self._current_amount += self.value_chain[self._current_chain_position]
        self._current_chain_position = 0
    
    @property
    def current_amount(self) -> int:
        """Returns the current amount of money in the bank."""
        return self._current_amount
    
    @property
    def current_chain_position(self) -> int:
        """Returns the current position in the value chain."""
        return self._current_chain_position
    
    def __str__(self) -> str:
        """Returns a string representation of the bank."""
        return f"Current amount: {self.current_amount}, Current chain position: {self.current_chain_position}"

    


    
    