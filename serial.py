"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.startValue = start
        self.value = start

    def reset(self):
        self.value = self.startValue

    def generate(self):
        self.value += 1

serial = SerialGenerator(start=100)

