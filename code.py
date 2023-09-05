from board import GP14, GP21
from digitalio import DigitalInOut, Direction
from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut
from random import randint
from time import sleep
from os import listdir

#Configure sound output
audio = PWMAudioOut(GP14)
enablePin = DigitalInOut(GP21)
enablePin.direction = Direction.OUTPUT

#Function to play sound
def play_sound(filename):
    with open("sounds/"+filename, "rb") as full_path:
        
        #Initialize MP3Decoder object from path
        sound = MP3Decoder(full_path)
        
        #Pin sends high to FET, enabling speaker
        enablePin.value = True
        
        #Plays sound on speaker
        audio.play(sound)
        while audio.playing:
            pass
        
        #Pin sends low to FET, disabling speaker
        enablePin.value = False

if __name__ == "__main__":
    while(True):
        
        #Selects random sound file in sounds directory
        soundsDir = listdir("sounds")
        fileVal = randint(0, len(soundsDir)-1)
        
        #Create random delay to play sound
        delay = randint(3, 12)
        print("Waiting "+str(delay)+" seconds to play "+soundsDir[fileVal])
        sleep(delay)
        
        #Call on function to play sound
        play_sound(soundsDir[fileVal])
