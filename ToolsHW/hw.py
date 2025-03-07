import webbrowser  
import sys
import time
import random
import os

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
B1 = False     
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    while True:
        try:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                open_video()
                B1 = True
                UndefinedVar += 1  
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1 
        except:
            ERROR_COUNT -= 1
            pass 

def open_video():
    webbrowser.open(VIDEO_URL)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 10 / 0 


if __name__ == "__main__":
    input_math()
