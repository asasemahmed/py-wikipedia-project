import webbrowser as web
import time
from tkinter import messagebox as msb
import random


football_players = [
    r"https://ar.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%B5%D9%84%D8%A7%D8%AD",
    r"https://ar.wikipedia.org/wiki/%D9%84%D9%8A%D9%88%D9%86%D9%8A%D9%84_%D9%85%D9%8A%D8%B3%D9%8A",
    r"https://ar.wikipedia.org/wiki/%D9%83%D8%B1%D9%8A%D8%B3%D8%AA%D9%8A%D8%A7%D9%86%D9%88_%D8%B1%D9%88%D9%86%D8%A7%D9%84%D8%AF%D9%88",
    r"https://ar.wikipedia.org/wiki/%D9%86%D9%8A%D9%85%D8%A7%D8%B1",
    r"https://ar.wikipedia.org/wiki/%D9%83%D9%8A%D9%84%D9%8A%D8%A7%D9%86_%D9%85%D8%A8%D8%A7%D8%A8%D9%8A",
    r"https://ar.wikipedia.org/wiki/%D9%83%D8%B1%D9%8A%D9%85_%D8%A8%D9%86%D8%B2%D9%8A%D9%85%D8%A7",
    r"https://ar.wikipedia.org/wiki/%D9%81%D9%8A%D8%B1%D8%AC%D9%8A%D9%84_%D9%81%D8%A7%D9%86_%D8%AF%D9%8A%D9%83",
    r"https://ar.wikipedia.org/wiki/%D9%84%D9%88%D9%8A%D8%B3_%D8%B3%D9%88%D8%A7%D8%B1%D9%8A%D8%B2",
    r"https://ar.wikipedia.org/wiki/%D8%B2%D9%84%D8%A7%D8%AA%D8%A7%D9%86_%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85%D9%88%D9%81%D9%8A%D8%AA%D8%B4"
]

actors = [

    r"https://ar.wikipedia.org/wiki/%D8%B9%D8%A7%D8%AF%D9%84_%D8%A5%D9%85%D8%A7%D9%85",
    r"https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D9%8A%D9%86_%D8%AC%D9%88%D9%86%D8%B3%D9%88%D9%86",
    r"https://ar.wikipedia.org/wiki/%D8%A5%D9%85%D9%8A%D9%84%D9%8A%D8%A7_%D9%83%D9%84%D8%A7%D8%B1%D9%83",
    r"https://ar.wikipedia.org/wiki/%D8%A3%D9%84%D9%83%D8%B3%D9%86%D8%AF%D8%B1%D8%A7_%D8%AF%D8%A7%D8%AF%D8%A7%D8%B1%D9%8A%D9%88",
    r"https://ar.wikipedia.org/wiki/%D8%B5%D9%88%D9%81%D9%8A_%D8%AA%D9%8A%D8%B1%D9%86%D8%B1",
    r"https://ar.wikipedia.org/wiki/%D9%84%D9%8A%D9%88%D9%86%D8%A7%D8%B1%D8%AF%D9%88_%D8%AF%D9%8A_%D9%83%D8%A7%D8%A8%D8%B1%D9%8A%D9%88",
    r"https://ar.wikipedia.org/wiki/%D8%A3%D8%AD%D9%85%D8%AF_%D8%AD%D9%84%D9%85%D9%8A",
    r"https://ar.wikipedia.org/wiki/%D9%83%D9%8A%D9%84%D9%8A%D8%A7%D9%86_%D9%85%D9%88%D8%B1%D9%81%D9%8A"
]


fiction_information = [
    r"https://ar.wikipedia.org/wiki/%D8%A3%D8%B3%D8%B7%D9%88%D8%B1%D8%A9_%D9%83%D9%88%D8%B1%D8%A7",
    r"https://ar.wikipedia.org/wiki/%D8%A5%D9%8A%D8%B2%D9%8A%D8%B3",
    r"https://ar.wikipedia.org/wiki/%D8%A3%D8%BA%D9%86%D9%8A%D8%A9_%D8%A7%D9%84%D8%AC%D9%84%D9%8A%D8%AF_%D9%88%D8%A7%D9%84%D9%86%D8%A7%D8%B1"
]

general_information = [
    r"https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AD%D8%B1%D8%A8_%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85%D9%8A%D8%A9_%D8%A7%D9%84%D8%AB%D8%A7%D9%86%D9%8A%D8%A9",
    r"https://ar.wikipedia.org/wiki/%D8%A8%D8%B1%D9%85%D8%AC%D8%A9",
    r"https://ar.wikipedia.org/wiki/%D8%A2%D8%AF%D8%A7_%D9%84%D9%88%D9%81%D9%84%D8%A7%D9%8A%D8%B3",
    r"https://ar.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%A8%D9%86_%D9%85%D9%88%D8%B3%D9%89_%D8%A7%D9%84%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85%D9%8A",
    r"https://ar.wikipedia.org/wiki/%D8%B4%D8%A8%D9%83%D8%A9_%D8%AD%D8%A7%D8%B3%D9%88%D8%A8",
    r"https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A9_%D8%A7%D9%84%D8%B9%D8%AB%D9%85%D8%A7%D9%86%D9%8A%D8%A9",
    r"https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%A5%D8%AF%D8%B1%D9%8A%D8%B3%D9%8A",
    r"https://ar.wikipedia.org/wiki/%D8%A3%D9%84%D8%A8%D8%B1%D8%AA_%D8%A3%D9%8A%D9%86%D8%B4%D8%AA%D8%A7%D9%8A%D9%86",
    r"https://ar.wikipedia.org/wiki/%D8%A5%D9%8A%D9%84%D9%88%D9%86_%D9%85%D8%A7%D8%B3%D9%83",
    r"https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A9_%D8%A7%D9%84%D8%A3%D9%85%D9%88%D9%8A%D8%A9"
]


# a = 0
# for count in actors:
#     a += 1

# print(a)

name = input("Enter your name : ")

print(f"\nHello MR {name}")

print("""
what you want read about

foot ball players => 1
actors => 2
fiction information => 3
general information => 4
""")

choise = int(input("Enter your choise : "))

if choise == 1:
    if msb.askyesno("open web", "you want open the web page now"):
        web.open_new(football_players[random.randint(0, 8)])

    else:
        print("thanks for using this app")

elif choise == 2:
    if msb.askyesno("open web", "you want open the web page now"):
        web.open_new(actors[random.randint(0, 7)])

    else:
        print("thanks for using this app")

elif choise == 3:
    if msb.askyesno("open web", "you want open the web page now"):
        web.open_new(fiction_information[random.randint(0, 2)])

    else:
        print("thanks for using this app")

elif choise == 4:
    if msb.askyesno("open web", "you want open the web page now"):
        web.open_new(general_information[random.randint(0, 9)])

    else:
        print("thanks for using this app")

print("program closed")

time.sleep(5)
