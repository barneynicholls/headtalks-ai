import logging
import logging.handlers
from tkinter import *
from PIL import ImageTk, Image

#try:
#    from picamera import PiCamera as camera
#except ImportError:
from mocks import Mockpicamera as camera

def main():
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    # application log
    h = logging.handlers.RotatingFileHandler('pidentity.log', 'a', (1024 * 1024 * 2), 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)
    logging.info('Started')


    #cam = camera()
    #cam.capture("test.jpg")

    window = Tk()      
    window.attributes('-fullscreen', True)
    window.configure(background = 'white')

    header = Label(window, text="Welcome to Headtalks",font=("Arial", 50), background='white')
    header.grid(column=0, row=0)

    path = "putin.jpg"
    img = ImageTk.PhotoImage(Image.open(path))


    panel = Label(window, image = img)
    panel.grid(column=0, row=1)

    request = Label(window, text="Please tap your card and look at the camera",font=("Arial", 50), background='white')
    request.grid(column=0, row=2)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)

    window.mainloop()

    #app = App(title="Headtalks")
    #message = Text(app, text="Hi Please tap your card to enter the
    #competition!")
    #app.display()

    logging.info('finished')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

