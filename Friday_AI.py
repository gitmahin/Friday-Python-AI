import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import smtplib
import time
import pywhatkit
import pyautogui
from PIL import Image, ImageGrab
import screen_brightness_control as sbc
from pytube import YouTube
import math
import speedtest
# import re
# import requests
# import urllib.request


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=9 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")

    else:
        print("Good Evening!")

    speak("Hi, saying Friday.")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        # r.pause_threshold = 0.9
        # r.adjust_for_ambient_noise(source, duration=5)
        # r.energy_threshold= 1
        # r.dynamic_energy_threshold = True 
        Audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(Audio, language='en-bn')
        print(f"User said: {query}\n")

    except Exception :
        # print(e)
        
        print("Say that again please......")
        return takeCommand()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nimahin25@gmail.com', 'sbxrfvcgeamfxoxq')
    server.sendmail('nimahin25@gmail.com', to, content)
    server.close()

def takeScreenshot():
    image = ImageGrab.grab()
    image.show()
    image.save

def hit(key):
    pyautogui.press(key)
    
def messenger():
   
    mespath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Messenger\\Messenger.exe"
    os.startfile(mespath)
                    
    while True:
        typee2 = takeCommand().lower()
        if 'stop typing' in typee2:
            speak('stopped typing')
            break
        else:
            pyautogui.typewrite(typee2)
            pyautogui.press('enter')

def messenger2():
    while True:
        ty_1 = takeCommand().lower()
        if 'stop typing' in ty_1:
            speak('stopped typing')
            break
        
        else:
            pyautogui.typewrite(ty_1)
            pyautogui.press('enter')

def Download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()

    try:
        youtubeobject.download()
        speak('download has completed successfully')

    except Exception as e:
        speak("Sorry, an error has occuurred.Download can't complete.")

# def download3(link):
#     html = requests.get(link)

#     try:
#         url = re.search('hd_src:"(.+?)"', html.text)[1]
#         speak('found the HD quality.')

#     except:
#         url = re.search('sd_src:"(.+?)"', html.text)[1]
#         speak('found the SD quality.')

#     speak('downloading file.')
#     urllib.request.urlretrieve(url, "Video.mp4")
#     speak('download has been completed successfully')

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f'{size} Mbp,s'





while True:
    query = takeCommand()
    if 'wake up' in query:
        os.startfile('C:\\Users\\Nimul Islam Mahin\\Desktop\\friday.py')

    

        if __name__ == "__main__":
            wishMe()
            while True:
                query = takeCommand().lower()


                
# wikipedia:
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    try:
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=5)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except Exception:
                        speak("say again to wikipedia")

# starting system programe:
                elif 'wake up' in query:
                    speak("I'm here. Tell me!")

# screenshot programe:  
                elif 'screenshot' in query:
                    speak("taking screenshot")
                    # time.sleep(1)
                    takeScreenshot()

# volume controls programes:
                elif 'mute' in query:
                    speak('muted')
                    hit("volumemute")
                    speak("unmuted")

                elif 'increase sound' in query:
                    speak("increasing")
                    hit("volumeup")
                    
# time programme:
                elif 'time' in query:
                    localtime = time.asctime(time.localtime(time.time()))
                    speak(localtime)

# wifi speed test programme:
                elif 'speed test' in query:

                    speak('Wait for a moment. interrupting your router...')

                    try:

                        wifi = speedtest.Speedtest()
                        

                        speak('Getting download speed...')
                        download_speed = bytes_to_mb(wifi.download())

                        speak('Getting upload speed...')
                        upload_speed = bytes_to_mb(wifi.upload())

                    except Exception as e :
                        speak('sorry, an error has occurred. Please try again.')

                    speak(f'download speed:{download_speed}')
                    print(f'download speed:{download_speed}')
                    speak(f'and upload speed:{upload_speed}')
                    print(f'upload speed:{upload_speed}')
# apps opening programs:
                elif 'open youtube' in query:
                    speak("opening youtube")
                    webbrowser.open("youtube.com")
                    
                elif 'open whatsapp' in query:
                    son = query.replace('open whatsapp', '')
                    speak("opening whatsapp")
                    pywhatkit.open_web()

                elif 'open google' in query:
                    speak("opening google")
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    speak("opening stackoverflow")
                    webbrowser.open("stackoverflow.com")
                
                elif 'open facebook' in query:
                    speak ("opening facebook")
                    webbrowser.open("facebook.com")
                    # fac = query.replace('open facebook', '')
                    # pywhatkit.search("https://ms-my.facebook.com/ni.mahin.94/")

                elif 'open messenger' in query:
                    speak ("opening messenger")
                    mespath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Messenger\\Messenger.exe"
                    os.startfile(mespath)

                elif 'open vs code'  in query:
                    speak("opening visual code")
                    codepath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)

                elif 'open illustrator' in query:
                    speak("opening illustrator")
                    illpath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2022\\Support Files\\Contents\\Windows\\Illustrator.exe"
                    os.startfile(illpath)

                elif 'open photoshop' in query:
                    speak("opening adobe photoshop, please wait sir")
                    phopath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
                    os.startfile(phopath)

                elif 'open gmail' in query:
                    speak("opening Gmail")
                    webbrowser.open("gmail.com")

# calling someones and open someones profile programs:
        # these profiles will open in opera browser:                   
                
                elif 'call to mom' in query:
                    speak('calling to mom')
                    webbrowser.open('https://www.facebook.com/groupcall/ROOM:5746244038791106/?call_id=1537071055&has_video=false&initialize_video=false&is_e2ee_mandated=false&nonce=f3k5eebxpgki&thread_type=1&users_to_ring[0]=100051675605998&use_joining_context=true&peer_id=100051675605998&server_info_data=GANwcm4YFVJPT006NTc0NjI0NDAzODc5MTEwNhgQSlhQUW9UUVhTYlhCTktGQwA%3D')
                    
                    
                    

                    
                elif "open profile" in query:
                    password = int(5006)
                    speak('say password.')                    
                    for i in range(2):
                        try:
                            password_command = int(takeCommand())

                            try:    
                                if password_command == password:
                                    speak('profile unlocked! opening.')
                                    webbrowser.open('https://www.facebook.com/messages/t/100084734888594/')
                                    speak('typing started. what to send?')
                                    messenger2()
                                    break    #from - def messenger2() function
                                else:
                                    speak('incorrect password.')
                                
                            except Exception as e:
                                print(e)

                        except Exception :
                            speak('please say numeric password.')
                    speak('profile is locked.Try again later...')

                elif "open mom's profile" in query:
                    speak('opening')
                    webbrowser.open('https://www.facebook.com/messages/t/100051675605998/') 
                    speak('typing started. what to send?')  
                    messenger2()     #from - def messenger2() function
                
                elif 'bright coaching' in query:
                    speak('opening')
                    webbrowser.open('https://www.facebook.com/messages/t/5516055828506646/')
                    speak ('typing started. what to send?')
                    messenger2()    #from - def messenger2() function

                elif 'omi' in query:
                    speak('opening')
                    webbrowser.open('https://www.facebook.com/messages/t/100023835227672/')
                    speak ('typing started. what to send?')
                    messenger2()    #from - def messenger2() function


# play music programs:
                # elif 'play music' in query:
                #     music_dir= 'F:\\Non Critical\\musics'
                #     songs = os.listdir(music_dir)
                #     print(songs)
                #     os.startfile(os.path.join(music_dir, songs[0]))


# browsers programs:
                elif 'open browser' in query:
                    speak('Which browser will open sir?')

                elif 'open opera'  in query:
                    speak("opening opera")
                    opepath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                    os.startfile(opepath)

                elif 'go to opera'  in query:
                    speak("going in opera")
                    opepath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                    os.startfile(opepath)


                elif 'open microsoft' in query:
                    speak("opening edge")
                    micropath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(micropath)
                    

                elif ' open edge' in query:
                    speak("opening edge")
                    micropath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(micropath)
                
                elif 'open my favourite browser' in query:  #opera
                    speak("okhay sir, enjoy your browsing")
                    favpath = "C:\\Users\\Nimul Islam Mahin\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                    os.startfile(favpath)

               

# normal talking programme:
                elif 'fine' in query:
                    speak("mode off,sir?")
                
                elif 'shut up' in query:
                    speak("okhay sir")
                
                elif 'going on' in query:
                    speak("Friday silenting")

                elif 'who is mahim' in query:
                    speak("Firstly he is my creator. He is a student of college. Age 18.Born in 2005, June 18. He programmed me.")

                elif 'built' in query:
                    speak("Mahin. He is my creator. He programmed me. And named me as Friday.")
                
                elif 'builted' in query:
                    speak("your pronunciation is wrong.")

                elif 'functions' in query:
                    speak("My functions is hidden by my creator.")

                elif 'health' in query:
                    speak("All functions are well. No issues")

                elif 'who are you' in query:
                    speak("I'm Friday, I am an automated function. ")

                elif 'mother' in query:
                    speak("Welcome! I respect you. do you need any help from me?")

                # elif 'no friday' in query:
                #     speak("Okhay thank you, honour for call me.")

                elif 'help from you' in query:
                    speak('''if you need any voice search , you have to say the name which you want to search to wikipedia . if you want to open any app you have to say open, the name of the app which app you want to open. Besides you can send email to you friend
                            through saying , email to then name of you friend. ''')

                elif 'father' in query:
                    speak("Welcome! I respect you. do you need any help from me?")

                elif 'hello' in query:
                    speak("Yes, I'm here. Tell me.")

                elif 'no problem' in query:
                    speak("Thank you")

                elif 'there is a problem' in query:
                    speak("WHAT HAPPENNED SIR! ARE YOU ALL RIGHT?")

                elif 'tantion' in query:
                    speak("Okhay sir.")

# sent email to someone:
                elif 'email to mom' in query:
                    try:
                        speak('What should I say?')
                        content = takeCommand()
                        to = "nsfatema1@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry Sir, I cannot sent email")

                elif 'email to techno' in query:
                    try:
                        speak('What should I say?')
                        content1 = takeCommand()
                        to1 = "nsfatema1@gmail.com"
                        sendEmail(to1, content1)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry Sir, I cannot sent email")

                elif 'email to me' in query:
                    try:
                        speak('What should I say?')
                        content2 = takeCommand()
                        to2 = "nimahin25@gmail.com"
                        sendEmail(to2, content2)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry, I cannot sent email")

                elif 'email to tawhid' in query:
                    try:
                        speak('what should I say?')
                        content3 = takeCommand()
                        to3 = "tawhidanjum30@gmail.com"
                        sendEmail(to3, content3)
                        speak('Email has been send!')
                    
                    except Exception as e :
                        print(e)
                        speak('Sorry, I cannot sent email')


# vedio pause and resume programe:
                elif 'pause' in query:
                    hit('space')
                    speak('paused')

                elif 'resume' in query:
                    hit('space')
                    speak('resuming')

# play on youtube programe:
                elif 'play' in query:
                    song = query.replace('play', '')
                    speak('playing' + song)
                    pywhatkit.playonyt(song)

# google search programe:
                elif 'search' in query:
                    jel = query.replace('search', '')
                    speak('searching' + jel)
                    pywhatkit.search(jel)

# screen brightness controler programe:
                elif 'brightness' in query:
                    speak("how much")
                    try: 
                    # sbc.set_brightness(takeCommand()) 
                        bright = sbc.set_brightness(takeCommand())
                        print(bright)
                        speak('brightness seted')
                        
                    except Exception:
                        speak('say right number pronounciation and say again')

                    pass

# auto type programe in anywhere: 
                elif 'type' in query:
                    speak('what should be typed?')
                    while True:
                        typee = takeCommand().lower()
                        if 'stop typing' in typee:
                            speak('stopped typing')
                            break
                        else:
                            pyautogui.typewrite(typee, interval=0.01)

# auto type programe only for messenger:
                elif 'sent messege' in query:
                    speak ("Okhay, opening messenger")
                    messenger()      #from - def messenger() function


# download vedio from facebook:
                # elif 'download facebook' in query:
                #     speak('opening facebook. please select the video and copy link')
                #     webbrowser.open('facebook.com')
                #     speak('input copied link, which you want to download.')

                #     while True:
                #         try:
                #             link = input('Enter the facebook video url: ')

                #             if link == 'stop':
                #                 speak("download has been stopped!")
                #                 break

                #             speak('Downloading. Please wait for a moment.')
                #             download3(link)
                #             speak("If you want to download more vedio, input url. Otherwise to stop downloading input 'stop'.")

                #         except Exception as e :
                #             speak('You have not inputed url. Please input url to download vedio.')




# download vedio from youtube:
                elif 'download youtube' in query:
                    speak('Opening youtube. Please select the video and copy link.')
                    webbrowser.open('youtube.com')
                    speak('Input the vedio link, which you want to download.')

                    while True:
                        try:
                            link = input('Enter the youtube video url: ')

                            if link=='stop':
                                speak('download has been stopped!')
                                break
                            
                            speak('Downloading. Please wait for a moment')
                            Download(link)
                            speak("to stop downloading input 'stop'.")
                        except Exception as e :
                            speak('You have not inputed url. Please input url to download vedio.')
                    

                elif 'stop friday' in query:
                    speak("STOPPING Friday")
                    speak("Friday has been stopped")
                    break

                else:
                    print("say again please")

        

    elif 'exit' in query:
        speak("exiting in 5 seconds")
        time.sleep(5)
        speak("exited")
        exit()

    else:
        print('FINDING VOICE')







