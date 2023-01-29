# About

This script is a basic keylogger that captures and records every keystroke made by the user, thens sends the keylog file remotely via an FTP server. It uses the pynput library to listen for keyboard input and the ftplib library to store the recorded keystrokes on a remote FTP server. The keystrokes are saved in a file named "keylogs.txt" and the script is designed to run in the background.

# pynput

pynput is a Python library that allows for control and monitoring of the keyboard and mouse. It provides a clean and easy-to-use interface for accessing and controlling input devices. With pynput, developers can write scripts to automate keyboard and mouse actions, such as simulating key presses, clicking mouse buttons, and scrolling. It also allows for the creation of keyboard and mouse listeners, which can be used to detect and respond to specific input events in real-time. This library is useful for creating automation tools, games, and other applications that require low-level control of input devices.

# ftplib

ftplib is a built-in Python library that provides a set of classes for implementing the File Transfer Protocol (FTP). It allows developers to write scripts that can connect to FTP servers, navigate the server's file system, upload and download files, and perform other operations commonly associated with FTP. The library provides a high-level, easy-to-use interface for interacting with FTP servers, making it simple to perform common tasks like logging in, creating directories, and transferring files. It also supports secure FTP connections via SSL/TLS. This library is useful for automating file transfer tasks, such as backup scripts, or for integrating FTP functionality into other applications.
