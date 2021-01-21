from pydictionary import Dictionary
import wikipedia
import wolframalpha
import time
import datetime
import winsound
import os
from database import built_in_functions
from database import Dictionary
from database import file_methods
from database import Lists
from database import string_methods
from database import keywords
from database import java_keywords
from database import java_string_methods
from database import java_math_methods


input("Hello Master Ana! I am your assistant! I exist to help!")

Main_Menu = input("Now, type in a keyword, or type in help to see all keywords! ")

duration = 2000
frequency = 2500


if "python database" in Main_Menu:
    Q = input("Type in a keyword or type in help to see all available keywords ")

    if "built in functions" in Q:
        print(built_in_functions)
    elif "string methods" in Q:
        print(string_methods)
    elif "dictionary" in Q:
        print(Dictionary)
    elif "file methods" in Q:
        print(file_methods)
    elif "Lists" in Q:
        print(Lists)
    elif "keywords" in Q:
        print(keyword)
    elif "help" in Q:
        print("built in functions")
        print("string methods")
        print("dictionary")
        print("file methods")
        print("Lists")
        print("keywords")
    else:
        print("Incorrect Keyword. Try Again.")

    input()

elif "time?" in Main_Menu:
    date_time = datetime.datetime.now()
    print(date_time)
    input()

elif "wikipedia" in Main_Menu:
    E = input("Search Wikipedia ")
    furg = int(input("How many sentences?"))
    W = wikipedia.summary(E, sentences = furg)
    print(W)
    input()

elif "wolframalpha" in Main_Menu:
    client = wolframalpha.Client("LA6KGW-K7ALPJV6L6")

    r = input()
    res = client.query(r)
    print(next(res.results).text)
    input()

elif "timer" in Main_Menu:
    import time
    print("What shall I remind you about?")
    text = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    winsound.Beep(frequency, duration)
    print(text)
    input()


elif "calculat" in Main_Menu:
    input('Choose Two Numbers To Calculate')

    x = input("Number 1 ")

    use = input(' +, -, x, /,')

    y = input("Number 2 ")


    if use == '+':
       print(int(x) + int(y))
    elif use == '-':
       print(int(x) - int(y))
    elif use == 'x':
       print(int(x) * int(y))
    elif use == '/':
       print(int(x) / int(y))

    input()


elif "command prompt" in Main_Menu:
   while True:
       input("Type something in cmd! ")
       o = input()
       os.system(o)

elif "remember something" in Main_Menu:
        f = open("Memory.txt", "a")
        pap = input("Enter Info to Save!")
        f.write(pap)
        f.close()
        input()

elif "extract info" in Main_Menu:
    f = open("Memory.txt", "r")
    lp = int(input("How many lines?"))
    print(f.read(lp))
    input()

elif "java database" in Main_Menu:
    Qpo = input("Search Java Database or type in help to see all keywords ")

    if "java keywords" in Qpo:
        input()
        print(java_keywords)
    elif "java string methods" in Qpo:
        input()
        print(java_string_methods)
    elif "java math methods" in Qpo:
        input()
        print(java_math_methods)
    elif "elp" in Qpo:
        print("java keywords")
        print("java string methods")
        print("java math methods")
    else:
        print("Incorrect keyword. Try again.")

    input()

elif "help" in Main_Menu:
    print("This list contains only words that MUST be in the sentence for the function to activate")
    print("python database")
    print("time?")
    print("wikipedia")
    print("wolframalpha")
    print("timer")
    print("calculat")
    print("command prompt")
    print("remember something")
    print("extract info")
    print("java database")
    input()

else:
    print("Incorrect Keyword. Try again.")




