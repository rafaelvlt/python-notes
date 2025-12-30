import re
#while loop wich asks for a file name for the user checking if the format is correct.

while True:
  askFile = str(input("Which file do you want to play with? "))
  #see if the file has the .txt extension and stop the loop if true
  if askFile[-4:] == '.txt':
       break
       print(askFile)
  #if the file doesn't have a .txt at the end, add it, if the file has other extension send it to else
  elif not '.' in askFile:
      askFile = askFile + '.txt'
      break
  else:
      print("The file you inputed is not valid! Try inputing it again.")
#open the file and save it's content to validate in the for loop and the print it
fileRead = open(askFile)
content = str(fileRead.read())
print(content)
fileRead.close()
#new file in which we will save the answred file
answer = open("Answered" + askFile, 'w')
answer.write('')
answer.close()
#madlibs keys, i tried to put regex in this shit without sucess, someday i'm gonna go back to this and fix it
words = ["ADJECTIVE", "NOUN", "ADVERB", "VERB", "ADJECTIVE,", "NOUN,", "ADVERB,", "VERB,", "ADJECTIVE.", "NOUN.", "ADVERB.", "VERB."]
for i in content.split():
      #basic check
      if i in words:
         word = input("Enter a " + i.lower() + " ")
         word = word + " "
      else:
         word = (i + " ")
      #writing the previous file into this
      answer = open("Answered" + askFile, 'a')
      answer.write(word)
      answer.close()
      word = ""
answer = open("Answered" + askFile)
final = str(answer.read())
print(final)
answer.close()
