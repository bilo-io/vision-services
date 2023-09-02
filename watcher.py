import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the directory to watch for changes (the directory where main.py is located)
watch_directory = os.path.dirname(os.path.abspath(__file__))

# Set the script to restart (main.py)
script_to_restart = 'main.py'

# Function to restart the script
def restart_script():
    print("Restarting the server...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Watch for changes to main.py
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('main.py'):
            restart_script()

if __name__ == '__main__':
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=watch_directory, recursive=False)  # Set recursive to True if you want to monitor subdirectories
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
