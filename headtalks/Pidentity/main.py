import logging
import logging.handlers

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


    cam = camera()
    cam.capture("test.jpg")

    logging.info('finished')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

