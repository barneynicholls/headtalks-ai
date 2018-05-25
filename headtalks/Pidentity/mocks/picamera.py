#!/usr/bin/env python

import time
import logging

class Mockpicamera(object):
    def __init__(self):
        self.resolution = (1280,720)

    def capture(self, filename):
        logging.debug("capture: '{}' ".format(filename))
        time.sleep(1)

    def start_preview(self):
        logging.debug("start_preview")
        time.sleep(1)

    def stop_preview(self):
        logging.debug("stop_preview")
        time.sleep(1)


