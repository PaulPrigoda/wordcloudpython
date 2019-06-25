#PT Prigoda
#Programming Assignment 4
#Due date 10/28/15
#This program will take the inputed user file, then take out stop words and
#punctuation, then all the stop words, and display the most common words of the
#inputed text and display them in a GUI, the most common words being the largest
#and the less used words being smaller. They will be random colors every time
#you run the program.

from graphics import *
from random import *

def printIntro():
    #creates GUI
    win = GraphWin("PT's Word Cloud",600,600)
    win.setCoords(-1,-1,100,100)

    des = Text(Point(50,75),"This program will take a user inputed file, then take the most\n"
                            " common words of the file and output them in a GUI that displays\n"
                            " the most common words of the file as the biggest words.")
    des.setSize(20)
    des.draw(win)

    intro = Text(Point(50,90),"PT's Word Cloud")
    intro.setSize(25)
    intro.setFill("green4")
    intro.draw(win)

    enter = Text(Point(50,40),"Enter the file name to cloud,\n Then click anywhere!")
    enter.setSize(20)
    enter.draw(win)
    

    #creates input box
    inputBox = Entry(Point(50,50),20)
    inputBox.setText("frankenstein.txt")
    inputBox.draw(win)

    getText = inputBox.getText()

    pt = win.getMouse()

    #undraw everything for word cloud
    des.undraw()
    enter.undraw()
    inputBox.undraw()
    intro.undraw()

    return win,getText

def getInput(getText):
    #reads user inputted file
    inputFile = open(getText,"r")
    text = inputFile.read()
    wordList = text.lower()
    #returns to main function
    return wordList

def noJunk(text):
    #replaces all puncuation with nothing
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}~':
        text = text.replace(ch,"")
    #returns to main function
    return text

def stopWords(fileNoCh):
    #takes all non stop words and puts them in a list
    clean = []
    stopFile = open("stopwords.txt","r")
    read = stopFile.read()
    wordList = fileNoCh.split()
    stopList = read.split()
    for word in wordList:
        if word not in stopList:
            clean.append(word)
    #return to main function
    return clean

def commonWords(fileNoStop,freq):
    #takes the most common words of the new file and sends back to main
    for word in fileNoStop:
        if not (word in freq):
            freq[word] = 1
        else:
            freq[word] = freq[word] + 1
    items = freq.items()
    freqList = list(items)
    freqList.sort(key=order,reverse=True)
    #return to main function
    return freqList

def order(item):
    return item[1]

def graphics(mostCommon,win):
    win.setBackground("grey10")
    #blank list to store points
    points = []
    for x in range(10,90,13):
        for y in range(10,90,13):
            pt1 = Point(random()*5+x,random()*5+y)
            points.append(pt1)
    size = 50
    #how many words on screen
    for j in range(30):
        #words random colors every time
        color = color_rgb(randrange(0,255),randrange(0,255),randrange(0,255))
        i = (randrange(0,len(points)))
        textObj = Text(points[i],mostCommon[j][0])
        textObj.draw(win)
        #sets size of most common word
        textObj.setSize(size)
        if size > 20:
            size = size - 2
        textObj.setFill(color)
        points.pop(i)

    goodbye = Text(Point(50,10),"Click anywhere to close.")
    goodbye.setFill("white")
    goodbye.draw(win)

    win.getMouse()
    win.close()

def main():
    #dictionary for words and how many times it appears
    freq = {}

    #intro to the program
    win,getText = printIntro()
    print(getText)
    
    #gets text from user input
    file = getInput(getText)

    #list with file no punctuation
    fileNoCh = noJunk(file)

    #list with no punctuation and no stop words
    fileNoStop = stopWords(fileNoCh)
    
    #dictionary with most common words
    mostCommon = commonWords(fileNoStop,freq)
    
    g = graphics(mostCommon,win)
    #hry whats up

main()
