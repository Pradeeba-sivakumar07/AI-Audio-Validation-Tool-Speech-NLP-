import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import speech_recognition as sr
import pyttsx3
import PyPDF2


# ---------------------- Functions ----------------------


def open_github():
github_url = "https://github.com/your-username" # Replace with your GitHub profile
webbrowser.open_new_tab(github_url)


def audio_to_text():
recognizer = sr.Recognizer()
try:
with sr.Microphone() as source:
messagebox.showinfo("Info", "Recording... Speak now")
audio = recognizer.listen(source)
text = recognizer.recognize_google(audio)
output_text.delete("1.0", tk.END)
output_text.insert(tk.END, text)
except Exception as e:
messagebox.showerror("Error", f"Could not process audio:\n{e}")


def pdf_to_text():
file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
if file_path:
try:
pdf_file = open(file_path, 'rb')
reader = PyPDF2.PdfReader(pdf_file)
text = ""
for page in reader.pages:
text += page.extract_text() + "\n"
pdf_file.close()
output_text.delete("1.0", tk.END)
output_text.insert(tk.END, text)
except Exception as e:
messagebox.showerror("Error", f"Could not read PDF:\n{e}")


def text_to_speech():
text = output_text.get("1.0", tk.END).strip()
if text:
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
else:
messagebox.showwarning("Warning", "No text available for speech")


# ---------------------- GUI Setup ----------------------


root = tk.Tk()
root.title("Audio Weaver AI Tools")
root.geometry("700x450")


# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)


tk.Button(btn_frame, text="GitHub Profile", fg="white", bg="#333", command=open_github, width=18).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Audio to Text", fg="white", bg="#007acc", command=audio_to_text, width=18).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="PDF to Text", fg="white", bg="#007acc", command=pdf_to_text, width=18).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Text to Speech", fg="white", bg="#28a745", command=text_to_speech, width=18).grid(row=0, column=3, padx=5, pady=5)


# Text output area
output_text = tk.Text(root, wrap=tk.WORD, height=20, width=85)
output_text.pack(pady=10)


# Run the GUI
root.mainloop()
