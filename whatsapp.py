import pywhatkit as kit
import schedule
import time
import tkinter as tk
from tkinter import filedialog

def send_message():
    number = entry_number.get()
    message = text_message.get("1.0", tk.END).strip()
    hour = int(entry_hour.get())
    minute = int(entry_minute.get())
    kit.sendwhatmsg(number, message, hour, minute)
    status_label.config(text="Message Scheduled!")


def send_image():
    number = entry_number.get()
    file_path = filedialog.askopenfilename()
    caption = text_message.get("1.0", tk.END).strip()
    kit.sendwhats_image(number, file_path, caption)
    status_label.config(text="Image Scheduled!")


def send_pdf():
    number = entry_number.get()
    file_path = filedialog.askopenfilename()
    kit.sendwhats_document(number, file_path)
    status_label.config(text="PDF Scheduled!")

# GUI Setup
root = tk.Tk()
root.title("WhatsApp Scheduler")
root.geometry("400x400")
root.configure(bg="lightblue")

tk.Label(root, text="Recipient Number (with country code):").pack()
entry_number = tk.Entry(root)
entry_number.pack()

tk.Label(root, text="Message:").pack()
text_message = tk.Text(root, height=5, width=40)
text_message.pack()

tk.Label(root, text="Scheduled Time (24-hour format):").pack()
frame_time = tk.Frame(root)
frame_time.pack()
entry_hour = tk.Entry(frame_time, width=5)
entry_hour.pack(side=tk.LEFT)
tk.Label(frame_time, text=":").pack(side=tk.LEFT)
entry_minute = tk.Entry(frame_time, width=5)
entry_minute.pack(side=tk.LEFT)

tk.Button(root, text="Schedule Message", command=send_message).pack()
tk.Button(root, text="Send Image", command=send_image).pack()
tk.Button(root, text="Send PDF", command=send_pdf).pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
