# YetAnotherWeakestLinkSimulator

A Python-based simulator for "The Weakest Link" game show, focused on running question sequences, tracking participant turns, and handling game flow through a blessed terminal interface. The current prototype includes question parsing, participant management, and a host UI built for English output.

# YAWLS (Yet Another Weakest Link Simulator)

📚 **[The full documentaction of this project can be found on our wiki page!](https://github.com/MaciejMalak/YetAnotherWeakestLinkSimulator/wiki)**

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Features (WIP)

| Feature | Status |
|---------|--------|
| Parser | ✅ |
| Blessed Terminal UI | ✅ |
| User-only interface | ⬜ |
| Discord Bot Integration (private usage) | ⬜ |
| Game Logic (timer, current question, bank, etc.) | ⏳ |
| Terminal Interface (host and players) | ⏳ |

**Note:** The project now includes full blessed terminal support with English screen text. Game logic and terminal interface improvements are actively being worked on.

## Repository Structure

```
YetAnotherWeakestLinkSimulator/
├── README.md
├── main.py
├── participants.txt
├── questions.txt
├── logic/
│   ├── bank.py
│   ├── parser.py
│   └── question_status.py
└── TUI/    
    ├── questions_logic.py
    └── terminal.py
```

## Customizing Your Game

The current version includes both `questions.txt` and `participants.txt` in the repository so you can edit them directly.

- `questions.txt` contains the quiz questions and answers.
- `participants.txt` contains the player names for each game.

### How to edit
1. Open `questions.txt` in any text editor.
2. Add or change questions, keeping the existing format.
3. Open `participants.txt` and update participant names as needed.
4. Save both files and run `main.py` again to use the updated game data.

## Version History

### v0.1.0 (Current)
- Included `questions.txt` and `participants.txt` in the repository.
- Added a simple tutorial on how to edit game content.
- This is a hotfix applied to the current `0.1.0` version, not the next release.
- First alpha build with full Blessed Terminal support and English interface text.
- Active work on game logic and improving the terminal interface.

### v0.0.2
- Added chain logic and question updates for Blessed Terminal.

### v0.0.1
- Initial prototype with basic parser and bank implementation.
- Blessed Terminal was not yet implemented properly.

### Next release: v0.1.1
- Planned timer support.
- Expect additional game flow and interface enhancements.


