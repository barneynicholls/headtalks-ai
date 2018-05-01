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
    #window.attributes('-fullscreen', True)
    window.configure(background = 'white')

    label = Label(window, text="Welcome to Headtalks",font=("Arial", 50))
    label.grid(column=0, row=0)

    path = "putin.jpg"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(window, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    window.mainloop()

    #app = App(title="Headtalks")
    #message = Text(app, text="Hi Please tap your card to enter the competition!")
    #app.display()

    logging.info('finished')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

