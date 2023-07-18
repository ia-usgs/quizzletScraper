# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:55:05 2022

@author: irvin
"""

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

def fetch_quizlet():
    url = entry.get()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

    result = ""

    for num, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
        result += 'QUESTION {}\n\n'.format(num)
        result += question.get_text(strip=True, separator='\n') + '\n\n'
        result += 'ANSWER:\n'
        result += answer.get_text(strip=True, separator='\n') + '\n'
        result += '-' * 100 + '\n'
        result += '-' * 100 + '\n\n'

    text.delete('1.0', tk.END)
    text.insert(tk.END, result)

def save_results():
    result = text.get('1.0', tk.END)
    file_path = filedialog.asksaveasfilename(initialdir="~/Downloads", defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result)

# Create the main window
window = tk.Tk()
window.title("Quizlet Scraper")

# Create an input field for the Quizlet URL
label = tk.Label(window, text="Enter Quizlet URL:")
label.pack()
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button to fetch the Quizlet
button_fetch = tk.Button(window, text="Fetch Quizlet", command=fetch_quizlet)
button_fetch.pack()

# Create a text box to display the answers
text = tk.Text(window, width=80, height=30)
text.pack()

# Create a button to save the results
button_save = tk.Button(window, text="Save Results", command=save_results)
button_save.pack()

# Start the main event loop
window.mainloop()
