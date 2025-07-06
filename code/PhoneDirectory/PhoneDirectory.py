class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = set()

        for x in range(0,maxNumbers):
            self.slots.add(x)

    def get(self) -> int:
        if len(self.slots)!= 0:
            return self.slots.pop()
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.slots:
            return True
        return False

    def release(self, number: int) -> None:
        self.slots.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)