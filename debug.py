from logic.config import GameConfig
from logic.discord_notifier import DiscordNotifier
import time

def run_debug():
    print("--- ROZPOCZYNAM DIAGNOSTYKĘ ---")
    
    # 1. Test wczytywania URL
    config = GameConfig()
    url = config.discord_url
    print(f"1. Wczytany URL z properties.txt:\n   '{url}'")
    
    if not url or url == "https://discord.com/api/webhooks/YOUR_KEY":
        print("\n❌ BŁĄD: URL jest pusty lub ma domyślną wartość! Sprawdź properties.txt")
        return

    # 2. Test wysyłania (inicjalizacja klasy)
    print("\n2. Próbuję połączyć się z Discordem...")
    notifier = DiscordNotifier(url)
    
    # 3. Próba wysłania fikcyjnego pytania
    end_time = time.time() + 60
    
    # Symulujemy dokładną treść z Twojej gry
    notifier.send_game_update(
        question="Is this question not visible?", 
        participant="Participant1", 
        end_time_unix=end_time
    )
    
    if notifier.message_id:
        print(f"✅ SUKCES! Discord przyjął wiadomość. ID wiadomości: {notifier.message_id}")
    else:
        print("❌ BŁĄD: Wiadomość nie została wysłana, ale nie było też 'Crashu'.")
        print("Możliwa przyczyna: Problem z payloadem (np. zły kolor w embeds).")

if __name__ == "__main__":
    run_debug()