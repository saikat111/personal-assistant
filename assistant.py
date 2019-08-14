import webbrowser as wb
import speech_recognition as sr
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
uc_path='C:/Program Files (x86)/UCBrowser/Application/ucbrowser.exe %s'
nlist = ["CHROME","UC"]

def my_function():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What you want to search:")
        audio = r.listen(source)
        print ("done")
        try:
            text = r.recognize_google(audio)
            print("you  say:" + text)
            f_text = 'https://www.google.com/search?q=' + text
            wb.get(chrome_path).open(f_text)
        except Exception as e:
            print(e)
        print("TNX")

def se_one():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What you want to search:")
        audio = r.listen(source)
        print ("done")
        try:
            ut = r.recognize_google(audio)
            print("you  say:" + ut)
            u_text = 'https://www.google.com/search?q=' + ut
            wb.get(uc_path).open(u_text)
        except Exception as e:
            print(e)
        print("TNX")


print('List has the items: ', nlist)
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        found = False
        for i in range(len(nlist)):
            if nlist[i] == text:
                found = True
                if i==0:
                    my_function()
                elif i ==1:
                    se_one()
    except Exception as e:
                print(e)
