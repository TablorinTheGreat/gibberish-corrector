# -*- coding: utf-8 -*-
#מלאddגגגג מלא hekkodjd
from keyboard import on_press, on_release, wait
import keyboard
import ctypes
engTOheb={'q':'/','w':"'",'e':'ק','r':'ר','t':'א','y':'ט','u':'ו','i':'ן','o':'ם','p':'פ','a':'ש','s':'ד','d':'ג','f':'כ','g':'ע','h':'י','j':'ח','k':'ל','l':'ך','z':'ז','x':'ס','c':'ב','v':'ה','b':'נ','n':'מ','m':'צ',",":'ת',".":'ץ',';':'ף'}
hebTOeng={'/': 'q', "'": 'w', 'ק': 'e', 'ר': 'r', 'א': 't', 'ט': 'y', 'ו': 'u', 'ן': 'i', 'ם': 'o', 'פ': 'p', 'ש': 'a', 'ד': 's', 'ג': 'd', 'כ': 'f', 'ע': 'g', 'י': 'h', 'ח': 'j', 'ל': 'k', 'ך': 'l', 'ז': 'z', 'ס': 'x', 'ב': 'c', 'ה': 'v', 'נ': 'b', 'מ': 'n', 'צ': 'm', 'ת': ',', 'ץ': '.', 'ף': ';'}
words=["","",""]
i=0
l=False
def isEnglishJibrish(words):
    for i in range(len(words)):
        if words[i] in eng:
            return False
    return  True
def isHebrewJibrish(words):
    o=0
    for i in range(len(words)):
        if words[i] in heb:
            o+=1
    if o>=2:return False
    return  True
def correctEnglishJibrish(words):
    keyboard.press_and_release("alt+shift")
    for c in range(sum(len(i) for i in words)+3):
        keyboard.press_and_release('backspace')
    if start==english:
        for i in range(len(words)):
            for c in range(len(words[i])):
                keyboard.press_and_release(words[i][c])
            keyboard.press_and_release("space")
    else:
        for i in range(len(words)):
            for c in range(len(words[i])):
                keyboard.press_and_release(engTOheb[words[i][c]])
            keyboard.press_and_release("space")


def correctHebrewJibrish(words):
    keyboard.press_and_release("alt+shift")
    for c in range(sum(len(i) for i in words)+3):
        keyboard.press_and_release('backspace')
    if start==hebrew:
        for i in range(len(words)):
            for c in range(len(words[i])):
                keyboard.press_and_release(words[i][c])
            keyboard.press_and_release("space")
    else:
        for i in range(len(words)):
            for c in range(len(words[i])):
                keyboard.press_and_release(hebTOeng[words[i][c]])
            keyboard.press_and_release("space")

def onKeyBoardEvent(event):
    global user32,i,words,l
    lang = user32.GetKeyboardLayout(user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0))
    c=event.name
    if c=="enter" or c=="space":
        if l:
            i+=1
            l=False
            if i==3:
                print(words)
                if lang==english:
                    if isEnglishJibrish(words):
                        correctEnglishJibrish(words)
                elif lang==hebrew:
                    if isHebrewJibrish(words):
                        correctHebrewJibrish(words)
                words = ["", "", ""]
                i=0
    elif c=="backspace":
        if l:
            words[i]=words[i][:len(words[i])-1]
        else:
            i-=1
            if i<0:
                i=0
    elif lang==english:
        if c in engTOheb:
            words[i]+=c
            l=True
        elif c in hebTOeng:
            c=hebTOeng[c]
            words[i] += c
            l=True
    elif lang==hebrew:
        if c in hebTOeng:
            words[i] += c
            l=True
        elif c in engTOheb:
            c=engTOheb[c]
            words[i] += c
            l=True
f = open('english.txt','r')
eng = f.read().split('\n')
b = open('hebrew.txt',encoding='utf-8')
heb = b.read().split('\n')
user32 = ctypes.WinDLL('user32', use_last_error=True)
start=user32.GetKeyboardLayout(user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0))
english=67699721
hebrew=-264436723
on_release(onKeyBoardEvent)
wait()

