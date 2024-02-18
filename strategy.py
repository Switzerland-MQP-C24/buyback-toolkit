class Strategy:
    def __init__(self, strategy):
        raise NotImplementedError("You should implement this!")

    def execute(self, data):
        raise NotImplementedError("You should implement this!")