class Logger:
    def __init__(self, name, enabled=True):
        self.name = name
        self.enabled = True
    def log(self, text):
        if self.enabled:
            print("{0}: {1}".format(self.name, self.text))