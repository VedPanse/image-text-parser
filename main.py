# Credits to google AI Vision for the API. This program will not work if copied and pasted. You'll need to have a subscription of google's ai vision api.


import requests
from tkinter import *

def process():
    image_URL = enter.get()
    payload = "{\n    \"source\": \"" + image_URL + "\",\n    \"sourceType\": \"url\"\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "google-ai-vision.p.rapidapi.com",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = response.json()["text"]

    text_label = Label(text="This image says:")
    text_label.grid(row=10, column=2)

    data_label = Label(text=data, font=("Arial", 16, "normal"))
    data_label.grid(row=12, column=2)

window = Tk()
window.minsize(800, 800)
window.title("Scraping text off images")

title = Label(text="Image Text Parsing", font=("Arial", 20, "bold"))
title.grid(row=2, column=2)

label = Label(text="Enter the url of the image you want to scrape data from: ")
label.grid(row=4, column=2)

enter = Entry()
enter.grid(row=6, column=2)

url = "https://google-ai-vision.p.rapidapi.com/cloudVision/imageToText"
button = Button(text="Enter", command=process)
button.grid(row=8, column=2)

window.mainloop()
