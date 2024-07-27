import speech_recognizer as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

filename = "audio.wav"
duration = 3
fs = 44100

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

print("Welcome to VoiceSearch:-\n"
      "Youtube\n"
      "Wikipedia\n"
      "Google")

start_rec = input("Shall I start recording? [Y] or [N]\n")

if start_rec == "Y":
    sr.record_audio(filename, duration, fs)
    search_engine = sr.recognize_speech_from_audio(filename)

    if search_engine.lower() == "youtube":
        print("What would you like to search in youtube?")
        start = input("Shall I start recording? [Y] or [N]\n")

        if start == "Y":
            sr.record_audio(filename, duration, fs)
            search_text = sr.recognize_speech_from_audio(filename)

            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://www.youtube.com/")

            search = driver.find_element(By.NAME, "search_query")
            search.click()
            search.send_keys(search_text, Keys.ENTER)
        else:
            print("Alright, Bye!")
    elif search_engine.lower() == "wikipedia":
        print("What would you like to search in wikipeda?")
        start = input("Shall I start recording? [Y] or [N]\n")

        if start == "Y":
            sr.record_audio(filename, duration, fs)
            search_text = sr.recognize_speech_from_audio(filename)

            driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://www.wikipedia.org/")

            search = driver.find_element(By.NAME, "search")
            search.click()
            search.send_keys(search_text, Keys.ENTER)
        else:
            print("Alright, Bye!")
    elif search_engine.lower() == "google":
        print("What would you like to search in google?")
        start = input("Shall I start recording? [Y] or [N]\n")

        if start == "Y":
            sr.record_audio(filename, duration, fs)
            search_text = sr.recognize_speech_from_audio(filename)

            driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://www.google.com/")

            search = driver.find_element(By.TAG_NAME, "textarea")
            search.click()
            search.send_keys(search_text, Keys.ENTER)
        else:
            print("Alright, Bye!")
else:
    print("Alright, bye!")
