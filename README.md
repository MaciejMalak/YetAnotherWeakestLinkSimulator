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
| Game Logic (timer, current question, bank, etc.) | ✅ |
| Host Interface | ✅ |
| Player Interface | ⬜ |

**Note:** The project now includes full blessed terminal support with English screen text and timer support in the current alpha release. The host interface is implemented, while player interface work has not started yet. The next release will probably include a `properties.txt` settings file for game logic configuration.

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

### v0.2.0 (Current)
- Added timer support and improved game flow in the terminal interface.
- Completed the first alpha release for the next major version.
- Continued enhancements for question handling, participant turns, and UI flow.

### v0.1.1
- Bugfix release prior to the current alpha.
- Improved terminal UI stability and fixed parser/flow issues.
- Prepared the codebase for the timer-enabled `v0.2.0-alpha` release.

### v0.1.0
- Included `questions.txt` and `participants.txt` in the repository.
- Added a simple tutorial on how to edit game content.
- First alpha build with full Blessed Terminal support and English interface text.
- Active work on game logic and improving the terminal interface.

### v0.0.2
- Added chain logic and question updates for Blessed Terminal.

### v0.0.1
- Initial prototype with basic parser and bank implementation.
- Blessed Terminal was not yet implemented properly.


