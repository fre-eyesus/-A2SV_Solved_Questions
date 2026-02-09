class FrequencyTracker:
    def __init__(self):
     self.count = {}
     self.freq = {}
    def add(self, number: int) -> None:

        before = self.count.get(number, 0)

        if before > 0:
            self.freq[before]-= 1
        new = before + 1
        self.count[number] = new
        self.freq[new] = self.freq.get(new,0) + 1


    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return 
        old = self.count[number]
        self.freq[old]-= 1

        if old == 1:
            del self.count[number]
        else:
            new = old - 1
            self.count[number] = new
            self.freq[new] = self.freq.get(new,0) + 1


    

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
