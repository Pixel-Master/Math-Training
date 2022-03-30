#Mathe Quiz
from tkinter import *
from random import randint
from time import sleep
modus="non"
if modus != "+" or "-" or "*" or "/":
      score = 0
print ("WELCOME TO THE MATH QUIZ!(version: 0.1)")
sleep(0.5)
print("Choose a Mode: (+|-|*|/)")
modus = input()
while modus == "+":
      ingame = 1
      a = randint(0,10000)
      b = randint(0,1000)
      ergebnis = a + b
      print("What results in",a,"+",b)
      antwort = input()
      antwort = int(antwort)
      if antwort == ergebnis:
                 score = score +1
                 print ("Correct!\nYour Score:",score)
      if antwort != ergebnis:
                 ingame = 0
                 print ("GAME OVER!\nThe correct solution is:",ergebnis,"\nYour Score: ",score)
      if ingame == 0:
                 break
while modus == "-":
      ingame = 1
      a = randint(0,1000)
      b = randint(0,1000)
      ergebnis = a - b
      print("What results in",a,"-",b)
      antwort = input()
      antwort = int(antwort)
      if antwort == ergebnis:
                 score = score +1
                 print ("Correct!")
                 print ("Your Score:",score)
      if antwort != ergebnis:
                 ingame = 0
                 print ("GAME OVER!\nThe correct solution is:",ergebnis,"\nYour Score: ",score)
      if ingame == 0:
                 break
while modus == "*":
      ingame = 1
      a = randint(0,12)
      b = randint(0,12)
      ergebnis = a * b
      print("What results in",a,"*",b)
      antwort = input()
      antwort = int(antwort)
      if antwort == ergebnis:
                 score = score +1
                 print ("Correct!")
                 print ("Your Score:",score)
      if antwort != ergebnis:
                 ingame = 0
                 print ("GAME OVER!\nThe correct solution is:",ergebnis,"\nYour Score: ",score)
      if ingame == 0:
                 break
while modus == "/":
      ingame = 1
      a = randint(50,100)
      b = randint(0,50)
      ergebnis = a / b
      print("What results in",a,"/",b)
      antwort = input()
      antwort = int(antwort)
      if antwort == ergebnis:
                 score = score +1
                 print ("Correct!")
                 print ("Your Score:",score)
      if antwort != ergebnis:
                 ingame = 0
                 print ("GAME OVER!\nThe correct solution is:",ergebnis,"\nYour Score: ",score)
      if ingame == 0:
                 break
if modus != "+" or not "-" or not "*" or not "/":
      print(modus,"is not a Mode")
