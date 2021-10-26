
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__=="__main__":
    i=0
    speak("Here is today's News .... Be ready with a cup of tea or coffee!!")

    speak("Which Category do you wanna listen to.....select down below")
    print("1.Business\n2.Entertainment\n3.Health\n4.Science"
          "\n5.Sports\n6.Technology")
    cate=int(input())
    if cate==1:
        url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f78eb5febab84dc7991b468fa235d145"
    elif cate==2:
        url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=f78eb5febab84dc7991b468fa235d145"
    elif cate==3:
        url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f78eb5febab84dc7991b468fa235d145"
    elif cate==4:
        url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=f78eb5febab84dc7991b468fa235d145"
    elif cate==5:
        url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f78eb5febab84dc7991b468fa235d145"
    elif cate==6:
        url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f78eb5febab84dc7991b468fa235d145"
    else:
        speak("You have entered wrong key....try again")
    news = requests.get(url=url).text
    news_dict = json.loads(news)
    print(news_dict['status'])
    arts=news_dict['articles']
    for i in range(1,10):
             print(i,'.',arts[i]['title'])
             speak(i)
             speak(arts[i]['title'])
             print("for more details click here ",arts[i]['url'])
             if i==10:
                speak("Thanks for listening........Have a wonderful day BOSS")
             else:
                 speak("Moving on to the next news")


