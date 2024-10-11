class Fibonacci:
    def __init__(self, number):
        self.number = number

    def work(self,li):
        firEl = 0
        secEl = 1
        for _ in range(self.number):
            li.append(firEl)
            firEl, secEl = secEl, firEl + secEl

    def showWork(self):
        print(li)


li = []
obj = Fibonacci(20)
obj.work(li)
obj.showWork()
