import speech_recognition as sr
from gtts import gTTS
#pip3 install play sound
from time import ctime
import time
import playsound
import os
import re
import webbrowser
import bs4
import requests
from bs4 import BeautifulSoup # from Displaying Clean Data
import requests # used to get the data
import google
import bs4
import pandas as pd

#i = 0

def listen1(i):
    r = sr.Recognizer() #dot means i m taking funtionalities from it
    with sr.Microphone() as source: # taking microphone as source
        print("I m listning...")
        audio = r.listen(source,phrase_time_limit = 8)# i m giving wait time to fecthch the data
    data =""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You Said:"+data)
    except sr.UnknownValueError:
        i=i+1
        respond("Choose module again",i)
        print("I cannot Hear u")
    except sr.RequestError as e:
        print("Request Failed")
    return data

def listen():
    r = sr.Recognizer() 
    with sr.Microphone() as source: # taking microphone as source
        print("I m listning...")
        audio = r.listen(source,phrase_time_limit = 8)# i m giving wait time to fecthch the data
    data =""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You Said:"+data)
    except sr.UnknownValueError:
        print("I cannot Hear u")
    except sr.RequestError as e:
        print("Request Failed")
    return data

def respond(String,i):
    print(String)
    #i = i+1
    tts = gTTS(text=String, lang = "en") 
    tts.save("Speech"+str(i)+".mp3")
    playsound.playsound("Speech"+str(i)+".mp3")
    os.remove("Speech"+str(i)+".mp3")
    j = int(i)
    return j

def voice_assistant(data,i):
    
    if "how are you" in data: # by voice input "how are you" this module will be executing
        listening = True
        i = i + 1
        respond("I am well",i)
        return i
    elif "time" in data: # by voice input "time" this module will be executing
        listening = True
        i = i+1
        respond(ctime(),i)
        return i
    elif "dictionary" in data.casefold():# by voice input "dictionary" this module will be executing
        pin = 0
        try :            
            listening = True
            i=i+1
            respond("What word You want to search, for example say blue",i)
            word = listen1(i)
            url = "https://www.dictionary.com/browse/"+word+"?s=t/" #scrapping dictionary meaning data from this site
            page = requests.get(url)
            #print(page.text)
            soup = BeautifulSoup(page.text,'lxml')
            b = soup.find("span",{"class":"one-click-content css-1p89gle e1q3nk1v4"})
            #print(b)
            tex = b.text
            i=i+1
            #print(tex)
            respond(tex,i)
            return i
        except:
            print("Error in pronounciation")
            pin = 1 
        if pin == 1:
            return i

    elif "translator" in data.casefold():# by voice input "translator" this module will be opening
        pin1 = 0
        try :
            listening = True
            i = i+1 
            respond("which English word u want to translate, for example say blue",i)
            word = listen1(i)
            i = i+1
            respond("In which language u want to translate, for example say Hindi or any Language like Telugu etc",i)
            lang = listen1(i)
            str1 = lang[0].upper()
            str2 = lang[1:].lower()
            str3 = str1+str2
            print(str3)
            url = "https://www.indifferentlanguages.com/words/"+word #scrapping translated data from this site
            page = requests.get(url)
            print(page.status_code)
            soup = BeautifulSoup(page.text,'html.parser')
            stat = soup.find('div',{'class':'translations'})
            print(len(stat))
            print(stat.text)
            a = stat.text
            #print(a)
            x = a.split()
            print(x)
            count = 0
            flag = 0
            for j in x:
                if j == "[edit]"+str3:
                    print("found")
                    flag = 1
                    break
                count = count + 1
            if flag==1:
                print("found",count)
                print(x[count+1])
                i = i+1
                respond(x[count+1],i)
            else:
                print("not found")
            return i
        except:
            print("Error in pronounciation")
            pin1 =1
        if pin1 == 1:
            return i
    

    elif "stop" in data:# by voice input "stop" this module will be getting stop
        listening = False
        print("listening stop")
        i = i+1
        respond("Thank you for using our system. Work with us Again",i)
        exit()
        
        

    else:
        return i
    


    
i = 0    
time.sleep(2)
respond("Welcome! say dictionary to open dictionary, say translator to open translator, say time to know time, say stop to stop",i)

listening = True
while (listening == True):
    data = listen() # call the listen function
    check =  isinstance(data,str)
    if (check == True):
        i = voice_assistant(data,i)
    #print(listening)


