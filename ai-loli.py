from typing import Text
import random
import pyttsx3
import datetime
import speech_recognition
import webbrowser as wb
import wikipedia
from wikipedia.wikipedia import search
import string    

#giong bosss
loli=pyttsx3.init()
voices = loli.getProperty('voices') 
loli.setProperty('voice', voices[1].id)
you=input()

   

def speak(audio):
    print("Loli: " + audio)
    loli.say(audio)
    loli.runAndWait()
    
def open_goole():
    speak("Boss bạn cần tìm gì ?")
    search = input()
    url = ('https://google.com/search?q='+ search)
    speak("Đang tìm "+ search)
    wb.open_new_tab(url)
    speak("đã tim thấy ")
    
def open_youtobe():
    speak("Boss cần tìm gì trên youtobe ?")
    search = input()
    url = ('https://www.youtube.com/results?search_query='+ search)
    speak("Đang tìm "+ search)
    wb.open_new_tab(url)
    speak("Đã mở trang youtobe")

def open_wiki():
    speak("Cần tìm gì trên wiki boss ?")
    wiki_seark = input()
    print("Boss: " + wiki_seark)
    wikipedia.set_lang("vi")
    speak(wikipedia.summary(wiki_seark))    

def time():
    Time=datetime.datetime.now().strftime(" %H:%M")
    speak("hiện tại là " + Time)
def day():
    Day=datetime.datetime.now().strftime("%x")
    speak("Hôm nay là ngày "+Day)
#comamd chào
def wecom():
    time_now=datetime.datetime.now().strftime("%p")
    hour=datetime.datetime.now().hour
    if time_now == "AM":
        if hour >= 0 and hour<7:
            speak("Chào buổi sáng boss. Sao boss thức sớm vậy ?")
        elif hour >= 6 and hour<10:
            speak("Chào buổi sáng boss. Chúc boss 1 ngày tốt lành.")
        elif hour >= 10 and hour<12:
            speak("Chào buổi trưa boss anh đã nghĩ ra mình ăn gì chưa ?")
        speak("Em có thể Giúp gì được cho anh ?")
    else:
        if hour >= 1 and hour<5:
            speak("Chúc anh 1 buổi chiều tốt lành nhé ")
        elif hour >= 5 and hour<9:
            speak("Chiều tối rồi anh nên đi tắm ăn cơm đi ...")
        elif hour >= 9 and hour<11:
            speak("Nên nghĩ nghơi thôi code nhiều ra gây lú đó")
        elif hour >= 11:
            speak("Tối lắm rồi nên ngủ sớm thôi thức khuya z không tốt đâu")
        speak("Thần thiếp có thể giúp gì bệ hạ?")   
#comamnd
            
def robot_bran():
    while True:
        you=input()
        
        print("Boss " + you)
        
        if "wiki" in you:
            open_wiki()  
            
        elif "giờ" in you:
            time()
        
        elif "ngày" in you:
            day()
        
        elif "goole" in you:
            open_goole()
            
        elif "youtobe" in you:
            open_youtobe()
        
        elif you == "" in you:
            speak("bạn nói gì tôi không hiểu")
        elif you == "tạm biệt" in you:
            speak("tạm biệt boss")
            
            
            break
       

if __name__ == '__main__':
        if "hey loli" in you:
            wecom()
            robot_bran()
            
