from logic.question_status import QuestionStatus

class StatsTracker:

    def __init__(self, participants: list[str]):
        self.stats = {
            name: {"correct": 0, "incorrect": 0, "banked_total": 0}
            for name in participants
        }

    def record_answer(self, participant: str, question_status: QuestionStatus) -> None:
        """Records whether a participant answered a question correctly or incorrectly. This is used to calculate the strongest and weakest links at the end of the game."""
        if participant in self.stats:
            key = "correct" if question_status == QuestionStatus.ANSWERED_CORRECTLY else "incorrect"
            self.stats[participant][key] += 1

    def record_bank(self, participant: str, amount: int) -> None:
        """Records the amount banked by a participant. This is used to break ties when calculating the strongest and weakest links."""
        if participant in self.stats:
            self.stats[participant]["banked_total"] += amount

    def calculate_results(self) -> tuple[str | None, str | None]:
        """Calculates the strongest and weakest links based on the recorded stats. 
        The strongest link is the participant with the most correct answers, and in case of a tie, the one with the highest banked total. 
        The weakest link is the participant with the most incorrect answers, and in case of a tie, the one with the lowest banked total."""

        if not self.stats:
            return None, None
        
        def sort_key(item) -> tuple[float, int]:
            data = item[1]
            total_answered = data['correct'] + data['incorrect']
            percentage = (data['correct'] / total_answered * 100) if total_answered > 0 else 0
            return (percentage, data['correct'], data['banked_total'])
        
        sorted_players = sorted(self.stats.items(), key=sort_key, reverse=True)

        strongest = sorted_players[0][0]
        weakest = sorted_players[-1][0]

        return strongest, weakest
    
    def display_final_board(self) -> None:
        """Displays the final stats board at the end of the game, showing the number of correct and incorrect answers, the percentage of correct answers, and the total amount banked for each participant. 
        It also highlights the strongest and weakest links."""
        print("\n" + "="*65)
        print("📊 ROUND SUMMARY FOR HOST")
        print("="*65)
        print(f"{'Player':<15} | {'Correct':<8} | {'Incorrect':<10} | {'% Accurate':<9} | {'Banked':<8}")
        print("-" * 65)
        
        for name, data in self.stats.items():
            total_answered = data['correct'] + data['incorrect']
            percentage = (data['correct'] / total_answered * 100) if total_answered > 0 else 0
            
            print(f"{name:<15} | {data['correct']:<8} | {data['incorrect']:<10} | {percentage:>6.1f}%   | {data['banked_total']:<8}")
        
        strongest, weakest = self.calculate_results()
        print("-" * 65)
        print(f"🌟 STRONGEST LINK: {strongest}")
        print(f"💀 WEAKEST LINK:    {weakest}")
        print("="*65 + "\n")
