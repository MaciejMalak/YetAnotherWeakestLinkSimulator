import requests

class DiscordNotifier:

    def __init__(self, webhook_url: str, color: int = 8421504):
        self.url = webhook_url
        self.message_id = None
        self.color = color

    def send_game_update(self, question: str, participant: str, end_time_unix: float, chain_drawn: str, bank: int):
        if not self.url:
            return

        payload = {
            "embeds": [{
                "title": "❓ Question Tab!",
                "description": f"**Question:** {question}\n**Answering:** {participant}",
                "color": self.color,
                "fields": [
                    {
                        "name": "⏳ Time",
                        "value": f"<t:{int(end_time_unix)}:R>", 
                        "inline": True
                    },
                    {
                        "name": "🔥 Chain",
                        "value": f"{chain_drawn}", 
                        "inline": True
                    },
                    {
                        "name": "💰 Bank",
                        "value": f"{bank}",
                        "inline": True
                    }
                ]
            }]
        }

        try:
            if self.message_id is None:
                response = requests.post(f"{self.url}?wait=true", json=payload)
                if response.status_code in [200, 201]:
                    self.message_id = response.json().get("id")
            else:
                requests.patch(f"{self.url}/messages/{self.message_id}", json=payload)
        except Exception as e:
            print(f"[YAWLS] Error with Discord update: {e}")
            pass

    def freeze_old_message(self, question: str, participant: str, chain_drawn: str, bank: int):
        if not self.url or self.message_id is None:
            return
        
        if question == "__OUT_OF_QUESTIONS__":

           payload = {
                "embeds": [{
                    "title": "🏁 Round Finished / Out of Questions",
                    "description": "The question pool has been exhausted. Great job!",
                    "color": 16766720,
                    "fields": [
                        {
                            "name": "💰 Final Bank",
                            "value": f"{bank}",
                            "inline": True
                        },
                        {
                            "name": "🔥 Final Chain",
                            "value": f"`{chain_drawn}`",
                            "inline": True
                        }
                    ]
                }]
            }
           
        elif question == "__TIMEOUT__":

            payload = {
                "embeds": [{
                    "title": "⏳ Time's Up!",
                    "description": f"**Answering:** {participant}\nTime has run out for this question.",
                    "color": 16744192,
                    "fields": [
                        {
                            "name": "🔥 Final Chain",
                            "value": f"`{chain_drawn}`",
                            "inline": True
                        },
                        {
                            "name": "💰 Final Bank",
                            "value": f"{bank}",
                            "inline": True
                        }
                    ]
                }]
            }

        else:

            payload = {
                "embeds": [{
                    "title": "🏁 Round Finished / Interrupted",
                    "description": f"**Question:** {question}\n**Answering:** {participant}",
                    "color": 8421504,
                    "fields": [
                        {
                            "name": "⏳ Time",
                            "value": "🛑 Stopped",
                            "inline": True
                        },
                        {
                            "name": "🔥 Chain",
                            "value": f"{chain_drawn}", 
                            "inline": True
                        },
                        {
                            "name": "💰 Bank",
                            "value": f"{bank}", 
                            "inline": True
                        }
                    ]
                }]
            }

        try:
            requests.patch(f"{self.url}/messages/{self.message_id}", json=payload)
        except Exception as e:
            print(f"[YAWLS] Error with Discord update: {e}")
            pass

    def send_disconnect_message(self):
        if not self.url:
            return

        payload = {
            "embeds": [{
                "title": "🔌 Terminal Disconnected",
                "description": "**Game has been finished.**\nConnection to the Host panel has been lost.",
                "color": 8421504,
            }]
        }

        try:
            requests.post(self.url, json=payload)
        except Exception as e:
            print(f"[YAWLS] Error with Discord update: {e}")
            pass