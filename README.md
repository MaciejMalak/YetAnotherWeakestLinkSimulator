<p align="center">
  <img src="logo.png" alt="YAWLS Logo" width="100%"/>
</p>

# YetAnotherWeakestLinkSimulator

A Python-based simulator for "The Weakest Link" game show, focused on running question sequences, tracking participant turns, and handling game flow through a blessed terminal interface. The current prototype includes question parsing, participant management, and a host UI built for English output.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Terminal](https://img.shields.io/badge/Interface-TUI-lightgrey?style=flat-square)
![Discord](https://img.shields.io/badge/Integration-Discord_Webhooks-5865F2?style=flat-square&logo=discord)

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
| User-only interface | ✅ |
| Discord Websocket Integration (optional) | ✅ |
| Game Logic (timer, current question, bank, etc.) | ✅ |
| Properties (`properties.txt`) | ✅ |
| Host Interface | ✅ |
| Player Interface | ✅ |

**Note:** `v0.7.0` is ready to release and brings a boatload of new features: host statistics after every round, cleaner `properties.txt` formatting, extra host prep time before rounds via `extra_time`, and a new Discord embed for the setup phase of the game. The next update will likely focus on polishing the existing features rather than adding new ones, since the game is now nearly in a go-to state.

## Road to v1.0.0

- 🛠️ `v0.8.0` — Polish release: quality improvements, bug fixes, and stability updates.
- 🌟 `v1.0.0` — Official 1.0 release with a finished and polished experience.

## Repository Structure

```
YetAnotherWeakestLinkSimulator/
├── README.md
├── main.py
├── debug.py
├── properties.txt
├── config.py
├── discord_key.txt
├── participants.txt
├── questions.txt
├── logic/
│   ├── bank.py
│   ├── config.py
│   ├── discord_notifier.py
│   ├── parser.py
│   ├── question_status.py
│   ├── stats_tracker.py
│   └── timer.py
└── TUI/    
    ├── questions_logic.py
    └── terminal.py
```

## Customizing Your Game

The current version includes `questions.txt`, `participants.txt`, and `properties.txt` in the repository so you can edit them directly.

- `questions.txt` contains the quiz questions and answers.
- `participants.txt` contains the player names for each game.
- `properties.txt` contains configurable settings for the game logic, timing, Discord embed colors, and optional webhook key.

### How to edit
1. Open `questions.txt` in any text editor.
2. Add or change questions, keeping the existing format.
3. Open `participants.txt` and update participant names as needed.
4. Open `properties.txt` and adjust settings to your preference. Current keys include `round_duration` (seconds per round), `extra_time` (host preparation seconds), `auto_end_on_timeout`, `discord_embed_color`, and optional `discord_key` for Discord webhook support — consult the project wiki for full details.
5. Save the files and run `main.py` again to use the updated game data and settings.

## Version History

### v0.7.0 (Current)
- Added host statistics after every round so the host can review performance immediately.
- Cleaned up `properties.txt` formatting and improved settings clarity.
- Added `extra_time` in `properties.txt` for extra host preparation before the round starts.
- Added a new Discord embed for the setup phase of the game.
- Included `logic/stats_tracker.py` to support the new round stats and tracking flow.
- The next update will likely focus on polishing existing features rather than adding new functionality.

### v0.6.0
- Added new `properties.txt` options: `auto_end_on_timeout` and `discord_embed_color`.
- Updated `config.py` to load and handle the new settings.
- Added embedded Discord messages after timeout and when questions have run out.
- Next update will probably mostly include new settings in `properties.txt`.

### v0.5.0
- Added optional Discord websocket integration; the app runs normally when Discord is not configured.
- Updated `properties.txt` to support an optional `discord_key` for webhook integration.
- Added root-level `debug.py` and `discord_key.txt` files to support new configuration flows.
- Completed host, user-only, and player interface implementation.

### v0.3.0
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


