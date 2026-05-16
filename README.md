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
| Properties (`properties.txt`) | ✅ |
| Host Interface | ✅ |
| Player Interface | ⬜ |

**Note:** The project now includes full blessed terminal support with English screen text, timer support introduced in the previous release, and a project-level `properties.txt` settings file in the current `v0.3.0` release. The host interface is implemented, while player interface work has not started yet. The `properties.txt` file currently defines `round_duration` (seconds per round) and `extra_time` (additional prep time for the host).

## Repository Structure

```
YetAnotherWeakestLinkSimulator/
├── README.md
├── main.py
├── properties.txt
├── config.py
├── participants.txt
├── questions.txt
├── logic/
│   ├── bank.py
│   ├── parser.py
│   ├── question_status.py
│   └── timer.py
└── TUI/    
    ├── questions_logic.py
    └── terminal.py
```

## Customizing Your Game

The current version includes `questions.txt`, `participants.txt`, and `properties.txt` in the repository so you can edit them directly.

- `questions.txt` contains the quiz questions and answers.
- `participants.txt` contains the player names for each game.
- `properties.txt` contains configurable settings for the game logic (timer durations, scoring rules, UI options).

### How to edit
1. Open `questions.txt` in any text editor.
2. Add or change questions, keeping the existing format.
3. Open `participants.txt` and update participant names as needed.
4. Open `properties.txt` and adjust settings to your preference. Current keys include `round_duration` (seconds per round) and `extra_time` (host preparation seconds) — consult the project wiki for full details.
5. Save the files and run `main.py` again to use the updated game data and settings.

## Version History

### v0.3.0 (Current)
- Added `properties.txt` to provide project-level settings for game logic and UI.
- Integrated `properties.txt` into startup/config flow; settings control timers, scoring, and display options.
- Updated README, features, and editing instructions to include properties/settings.
- Continued refinement of host interface; player interface work remains to be started.

### v0.2.0
- Added timer support and improved game flow in the terminal interface.
- Completed the first alpha release for the next major version.
- Continued enhancements for question handling, participant turns, and UI flow.

### v0.1.1
- Bugfix release prior to the current alpha.
- Improved terminal UI stability and fixed parser/flow issues.
- Prepared the codebase for the timer-enabled release.

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


