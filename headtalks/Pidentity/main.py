import logging
import logging.handlers
import tempfile
import os.path
from tkinter import *
from PIL import ImageTk, Image

try:
    from picamera import PiCamera as camera
except ImportError:
    from mocks import Mockpicamera as camera

cam = camera()
cam.resolution = (800, 600)
window = Tk() 
panel = Label(window)

def open_image(path):

    if(not os.path.isfile(path)):
        path = "trump.jpg"

    snapped = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=snapped)
    panel.image_names=snapped

def capture():
    f = tempfile.NamedTemporaryFile(delete=False)
    imageFile = f.name + ".jpg"
    logging.info('capturing file: '+imageFile)
    cam.capture(imageFile)
    logging.info('opening file: '+imageFile)
    open_image(imageFile)

def stop_preview():
    cam.stop_preview()

def start_preview():
    cam.start_preview()

def close():
    sys.exit()

def init():
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('pidentity.log', 'a', (1024 * 1024 * 2), 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)
    logging.info('Started')

def default_ui():
    window.attributes('-fullscreen', True)
    window.configure(background = 'white')

    header = Label(window, text="Welcome to Headtalks",font=("Arial", 50), background='white')
    header.grid(column=0, row=0)

    open_image("putin.jpg")
    panel.grid(column=0, row=1)

    request = Label(window, text="Please tap your card and look at the camera",font=("Arial", 50), background='white')
    request.grid(column=0, row=2)

    buttonFrame = Frame(window,background = 'white')
    buttonFrame.grid(column=0,row=3)

    cam_capture = Button(buttonFrame,text="Capture", command=capture)
    cam_capture.grid( padx=10,column=0,row=0)

    cam_startPreview = Button(buttonFrame,text="Start Preview", command=start_preview)
    cam_startPreview.grid(padx=10,column=1,row=0)

    cam_stopPreview = Button(buttonFrame,text="Stop Preview", command=stop_preview)
    cam_stopPreview.grid(padx=10,column=2,row=0)

    closeIt = Button(buttonFrame,text="Close", command=close)
    closeIt.grid(padx=10,column=3,row=0)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.rowconfigure(4, weight=1)

def main():
    window.mainloop()

    #app = App(title="Headtalks")
    #message = Text(app, text="Hi Please tap your card to enter the
    #competition!")
    #app.display()

    logging.info('finished')


if __name__ == "__main__":
    try:
        init()
        default_ui()
        main()
    except KeyboardInterrupt:
        pass

