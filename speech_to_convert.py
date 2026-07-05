from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import speech_recognition as sr
import os
import threading

root = Tk()
root.title("Speech to Text and Text to Speech")
root.geometry("600x500")
root.config(bg="#f2f2f2")

# ---------- Text to Speech ----------
def text_to_speech():
    text = text_box.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Pehle kuch text likhiye.")
        return

    try:
        tts = gTTS(text=text, lang="en")
        tts.save("voice.mp3")

        # Windows me audio play karega
        os.system("start voice.mp3")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- Speech to Text ----------
def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening... Boliyega")
            root.update()

            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=8)

        status_label.config(text="Converting speech to text...")
        root.update()

        text = recognizer.recognize_google(audio, language="en-IN")

        text_box.delete("1.0", END)
        text_box.insert(END, text)

        status_label.config(text="Speech converted successfully")

    except sr.WaitTimeoutError:
        status_label.config(text="Time out: Aapne kuch nahi bola")
    except sr.UnknownValueError:
        status_label.config(text="Voice samajh nahi aayi, dobara boliye")
    except sr.RequestError:
        status_label.config(text="Internet connection check kijiye")
    except Exception as e:
        status_label.config(text="Error: " + str(e))


def start_speech_thread():
    threading.Thread(target=speech_to_text, daemon=True).start()


def clear_text():
    text_box.delete("1.0", END)
    status_label.config(text="Text cleared")


# ---------- GUI ----------
title_label = Label(
    root,
    text="Speech to Text and Text to Speech",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2",
    fg="blue"
)
title_label.pack(pady=20)

instruction_label = Label(
    root,
    text="Text likhiye ya microphone button dabakar boliye",
    font=("Arial", 12),
    bg="#f2f2f2"
)
instruction_label.pack()

text_box = Text(root, height=12, width=60, font=("Arial", 12))
text_box.pack(pady=15)

button_frame = Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

speak_button = Button(
    button_frame,
    text="Text to Speech",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=18,
    command=text_to_speech
)
speak_button.grid(row=0, column=0, padx=10)

mic_button = Button(
    button_frame,
    text="Speech to Text",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=18,
    command=start_speech_thread
)
mic_button.grid(row=0, column=1, padx=10)

clear_button = Button(
    root,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=clear_text
)
clear_button.pack(pady=10)

status_label = Label(
    root,
    text="Ready",
    font=("Arial", 11),
    bg="#f2f2f2",
    fg="black"
)
status_label.pack(pady=10)

root.mainloop()