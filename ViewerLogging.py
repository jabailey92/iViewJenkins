class logger():
    def __init__(self, verbose=False):
        self._verbose = verbose

    def debug(self, msg):
        if self._verbose:
            print("DEBUG: " + msg)

    def info(self, msg):
        print("INFO: " + msg)