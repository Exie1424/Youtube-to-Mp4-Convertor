from tkinter import *
import pytube

# Video Link: https://youtu.be/BZP1rYjoBgI

creamColor = "#FFFDD0"



# Window Customisation
window = Tk()
window.title("Youtube to Mp4 Converter")
window.geometry("560x500")
window.config(bg=creamColor)

# Main Label
youtubeLabel = Label(window,
                    text="Youtube to Mp4 Converter!",
                    fg="Red",
                    bg=creamColor,
                    font=("Comic Sans",30,"underline","bold")).place(x=30,y=5)


# User Input
userLink = StringVar()
userInput = Entry(window,
                width=83,
                borderwidth=5,
                textvariable=userLink).place(x=30,y=70)

# Conversion Button
def convertToMp4():
    videoURL = pytube.YouTube(userLink.get())
    video = videoURL.streams.get_highest_resolution()
    video.download("Videos")
    successLabel = Label(window,
                        text="Success, Video downloaded!",
                        bg="Green",
                        fg="White",
                        padx=25,
                        pady=10,
                        font=("Comic Sans",15,"bold")).place(x=115,y=170)

convertButton = Button(window,
                    text="Convert to Mp4",
                    fg="White",
                    bg="Green",
                    borderwidth=5,
                    command=convertToMp4).place(x=230,y=110)

window.mainloop()