# YetAnotherWeakestLinkSimulator

A Python-based simulator for "The Weakest Link" game show, focused on running question sequences, tracking participant turns, and handling game flow through a blessed terminal interface. The current prototype includes question parsing, participant management, and a host UI built for English output.

# YAWSS (Yet Another Weakest Link Simulator)

📚 **[The full documentaction of this project can be found on our wiki page!](https://github.com/MaciejMalak/YAWSS/wiki)**

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

## Version History

### v0.0.3 (Current)
- Official release with full Blessed Terminal support and English interface text.
- Active work on game logic and improving the terminal interface.

### v0.0.2
- Added chain logic and question updates for Blessed Terminal.

### v0.0.1
- Initial prototype with basic parser and bank implementation.
- Blessed Terminal was not yet implemented properly.

### Next release: v0.0.4
- Planned timer support.
- Expect additional game flow and interface enhancements.


