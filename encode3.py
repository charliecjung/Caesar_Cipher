#!/usr/bin/python
import string
userMessage = input("Enter the message you would like to encrypt: ")
shiftNum = int(input("Enter the shift number: "))
alphabet = string.printable[:-6]
finalMessage = ""

for x in range(0, len(userMessage)):
   if (userMessage[x] == " "):
      finalMessage += " "
      continue
   newShiftNum = (alphabet.index(userMessage[x]) + shiftNum) % len(alphabet) 
   """
   Debugging Print Statements
   print ("Encrypting your message...")
   print ("Position of letter[" + userMessage[x] + "]: " + str(alphabet.index(userMessage[x]))) 
   print ("ShiftNum: " + str(newShiftNum))
   """
   newChar = alphabet[newShiftNum]
   finalMessage += newChar 
   

print ("Your Final Message is: " + finalMessage)
