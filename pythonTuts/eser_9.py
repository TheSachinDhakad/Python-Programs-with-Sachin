import requests
import json
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today ")
    url = "https://newsapi.org/v2/" \
          "everything?q=tesla&from=2022-06-08&sortBy=publishedAt&apiKey=8ec635efb5f648878ec0e3755e79d78b"
    newz = requests.get(url).text
    newz_dict = json.loads(newz)
    print(newz_dict["articles"])
    arts = newz_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving id the next newz ,   Listen carefully")
    # print("Thanks for listening..")
