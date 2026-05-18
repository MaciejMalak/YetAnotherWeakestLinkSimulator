from pathlib import Path

class GameConfig:
    """Loads and manages the game configuration from a properties file. If the file is not found, it uses default values.
    Attributes:
        _round_duration (int): The duration of each round in seconds.
        _base_round_duration (int): The base duration of each round in seconds.
        _extra_time (int): The extra time that can be added to a round in seconds.
        """

    def __init__(self):
        """Loads the game configuration from a properties file. If the file is not found, it uses default values."""
        self._base_round_duration = 30
        self._extra_time = 0
        self._discord_webhook_url = ""
        self._auto_end_on_timeout = True
        self._discord_embed_color = 8421504
        self._discord_blank_time = 3

        self._load_properties()

        self._base_round_duration += self._extra_time

    def _load_properties(self):
        """Loads the game configuration from a properties file. If the file is not found, it uses default values."""

        base_dir = Path(__file__).parent.parent
        config_path = base_dir / "properties.txt"
        secret_key_path = base_dir / "discord_key.txt"

        if not config_path.exists():
            print("[YAWLS] Config file not found, using default values.")
            return
        
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()

                    if key == "round_duration":
                        try:
                            self._base_round_duration = int(value)
                        except ValueError:
                            raise ValueError(f"Invalid value for round_duration: {value}. Must be an integer.")
                    
                    if key == "extra_time":
                        try:
                            self._extra_time = int(value)
                        except ValueError:
                            raise ValueError(f"Invalid value for extra_time: {value}. Must be an integer.")

                    if key == "discord_webhook_url":
                        self._discord_webhook_url = value

                    if key == "auto_end_on_timeout":
                        try:
                            self._auto_end_on_timeout = value.lower() in ("true", "1", "yes")
                        except ValueError:
                            raise ValueError(f"Invalid value for auto_end_on_timeout: {value}. Must be a boolean.")
                        
                    if key == "discord_embed_color":
                        try:
                            self._discord_embed_color = int(value)
                        except ValueError:
                            raise ValueError(f"Invalid value for discord_embed_color: {value}. Must be an integer color code.")

        if secret_key_path.exists():
            with open(secret_key_path, "r", encoding="utf-8") as f:
                secret_key = f.read().strip()
                if "YOUR_KEY" in self._discord_webhook_url:
                    self._discord_webhook_url = self._discord_webhook_url.replace("YOUR_KEY", secret_key)

    @property
    def round_duration(self) -> int:
        """Returns the duration of each round in seconds."""

        return self._base_round_duration

    @property
    def discord_url(self) -> str:
        """Returns the Discord webhook URL."""

        return self._discord_webhook_url

    @property
    def auto_end_on_timeout(self) -> bool:
        """Returns whether the game should automatically end on timeout."""

        return self._auto_end_on_timeout
    
    @property
    def discord_embed_color(self) -> int:
        """Returns the color used for Discord embeds."""

        return self._discord_embed_color

    @property
    def extra_time(self) -> int:
        """Returns the extra time that can be added to a round in seconds."""

        return self._extra_time