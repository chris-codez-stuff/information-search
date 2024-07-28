import tkinter as tk
from tkinter import messagebox
import speech_recognizer as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

filename = "audio.wav"
duration = 3
fs = 44100

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class VoiceSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Information Search")

        # Main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.label_title = tk.Label(self.main_frame, text="Information Search", font=("Helvetica", 24, "bold"))
        self.label_title.pack(pady=(20, 10))

        self.label_websites = tk.Label(self.main_frame, text="Websites:-", font=("Helvetica", 18))
        self.label_websites.pack(anchor="w", padx=20)

        self.label_youtube = tk.Label(self.main_frame, text="• Youtube", font=("Helvetica", 16))
        self.label_youtube.pack(anchor="w", padx=40)

        self.label_google = tk.Label(self.main_frame, text="• Google", font=("Helvetica", 16))
        self.label_google.pack(anchor="w", padx=40)

        self.label_wikipedia = tk.Label(self.main_frame, text="• Wikipedia", font=("Helvetica", 16))
        self.label_wikipedia.pack(anchor="w", padx=40)

        self.label_instruction = tk.Label(self.main_frame, text="Speak what you need", font=("Helvetica", 16))
        self.label_instruction.pack(pady=(20, 10))

        self.record_button = tk.Button(self.main_frame, text="Record", font=("Helvetica", 16, "bold"),
                                       command=self.start_recording)
        self.record_button.pack(pady=(0, 20))

        self.quit_button = tk.Button(self.main_frame, text="Quit", font=("Helvetica", 16, "bold"), command=root.quit)
        self.quit_button.pack(pady=(0, 20))

        # Search frame
        self.search_frame = tk.Frame(root)

        self.search_label = tk.Label(self.search_frame, text="", font=("Helvetica", 24, "bold"))
        self.search_label.pack(pady=(20, 10))

        self.search_instruction = tk.Label(self.search_frame, text="Speak what you need", font=("Helvetica", 16))
        self.search_instruction.pack(pady=(20, 10))

        self.search_record_button = tk.Button(self.search_frame, text="Record", font=("Helvetica", 16, "bold"),
                                              command=self.record_search)
        self.search_record_button.pack(pady=(0, 20))

        self.search_quit_button = tk.Button(self.search_frame, text="Quit", font=("Helvetica", 16, "bold"),
                                            command=root.quit)
        self.search_quit_button.pack(pady=(0, 20))

        self.search_engine = None

    def start_recording(self):
        start_rec = messagebox.askquestion("VoiceSearch", "Shall I start recording?")

        if start_rec == "yes":
            sr.record_audio(filename, duration, fs)
            self.search_engine = sr.recognize_speech_from_audio(filename)
            self.search_engine = self.search_engine.lower()

            if self.search_engine in ["youtube", "wikipedia", "google"]:
                self.show_search_frame()
            else:
                messagebox.showinfo("VoiceSearch", "Invalid search engine. Please say YouTube, Wikipedia, or Google.")

    def show_search_frame(self):
        self.main_frame.pack_forget()
        self.search_label.config(text=f"{self.search_engine.capitalize()} Search")
        self.search_frame.pack(fill="both", expand=True)

    def record_search(self):
        start = messagebox.askquestion(self.search_engine.capitalize(),
                                       f"What would you like to search in {self.search_engine.capitalize()}? Shall I start recording?")

        if start == "yes":
            sr.record_audio(filename, duration, fs)
            search_text = sr.recognize_speech_from_audio(filename)

            driver = webdriver.Chrome(options=chrome_options)
            if self.search_engine == "youtube":
                url = "https://www.youtube.com/"
                search_box_name = "search_query"
            elif self.search_engine == "wikipedia":
                url = "https://www.wikipedia.org/"
                search_box_name = "search"
            else:  # google
                url = "https://www.google.com/"
                search_box_name = "q"

            driver.get(url)

            search = driver.find_element(By.NAME, search_box_name)
            search.click()
            search.send_keys(search_text, Keys.ENTER)
        else:
            messagebox.showinfo(self.search_engine.capitalize(), "Alright, Bye!")


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceSearchApp(root)
    root.mainloop()