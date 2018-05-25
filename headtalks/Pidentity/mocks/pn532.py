import logging

class MockPN532Module(object):
    def __init__(self):
        self.mock = True;

    def PN532(cs, sclk, mosi, miso):
        logging.debug("MockPN532Module create MockPN532")
        return MockPN532()

class MockPN532(object):
    def __init__(self):
        self.mock = True;

    def SAM_configuration(self):
        logging.debug("MockPN532 SAM_configuration")

    def read_passive_target(self):
        logging.debug("MockPN532 read_passive_target")
        return None

    def begin(self):
        logging.debug("MockPN532 begin")
       

