# YetAnotherWeakestLinkSimulator

A Python-based simulator for "The Weakest Link" game show. This early prototype parses participants and questions to set up the game mechanics.

## Features (WIP)

| Feature | Status |
|---------|--------|
| Parser | ✅ |
| Blessed Terminal UI | ⏳ |
| Discord Bot Integration (private usage) | ⬜ |
| Game Logic (timer, current question, bank, etc.) | ⬜ |
| Terminal Interface (host and players) | ⬜ |

**Note:** This is a very early prototype. Features and functionality will be updated as development progresses.

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

- **Future versions**: TBA
- **v0.0.3** (in progress): Bank updates and current participant updates (working towards this release).
- **v0.0.2** (current): Chain logic and question updates for Blessed Terminal.
- **v0.0.1**: Initial prototype — basic parser and bank implementation; Blessed Terminal not yet implemented properly.


