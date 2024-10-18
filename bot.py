import subprocess
import time
import os

def restart_bot():
    while True:
        try:
            # Get the current directory
            current_directory = os.path.dirname(os.path.abspath(__file__))
            
            # Replace '(link unavailable)' with the name of your bot script
            subprocess.run(['python3', os.path.join(current_directory, 'm.py')], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Bot crashed with error: {e}. Restarting...')
            time.sleep(5)  # Wait for 5 seconds before restarting
        except Exception as e:
            print(f'Unexpected error: {e}. Restarting...')
            time.sleep(5)  # Wait for 5 seconds before restarting

if __name__ == "__main__":
    while True:
        try:
            restart_bot()
        except Exception as e:
            print(f'Main loop error: {e}. Restarting...')
            time.sleep(5)  # Wait for 5 seconds before restarting
``"