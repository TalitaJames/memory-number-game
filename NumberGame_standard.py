from gtts import gTTS
from time import sleep
import os
import pyglet
import random as random
# import math

def gameIntro():
    input="Welcome to the random number game.\n\nYou will hear a list of numbers and have to type the number you hear.\n\nGood luck!"
    
    readFile(input)
    print("\n\n"+input)

def randList(level):
    listRand=[]
    for i in range(level):
        listRand.append(random.randint(0, 9))
    return listRand

def readFile(TextRead):
    tts = gTTS(text=TextRead, lang='en', tld='co.uk')
    filename = 'temp.mp3'
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file

def markInput(userInput, correctInput):
    j=0
    correct = True
    for char in userInput:
        if int(char) != correctInput[j]:
            correct=False
        j += 1
    print("Correct answer: "+str(correctInput))
    return correct

if __name__ == "__main__":
    gameIntro()
    correct = True
    level=0
    while correct:
        level+=1
        numberList=randList(level) #returns list of rng numbers

        TextRead = "Round "+str(level) +".   "+ str(numberList)


        readFile(TextRead)
        sleep(1)
        
        correct = markInput(input("Please write the number you heard:\n"), numberList)
        print("\n\n")
    
    readFile("That is incorrect.\nThe correct answer was" + str(numberList) + "You made it to level "+str(level)+". Good job!")