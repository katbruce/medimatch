#!/usr/bin/env python3
import click
import time
from helpers import welcome, get_symptom
finish = False
if __name__ == "__main__":
    welcome()
    name = input(">>")
    while finish == False:
        get_symptom(name)
        y = input("Would you like me to fix more of your problems? If so press [y]>>")
        if (y != 'y'):
            finish = True
        else: 
            finish = False
    
    click.echo("\n\nHope you feel better soon!")
    time.sleep(10)