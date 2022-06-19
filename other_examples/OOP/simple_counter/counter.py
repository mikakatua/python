class Counter:

    def __init__(self, initial_value=0):
        self.value = initial_value

    def up(self):
        self.value +=1

    def down(self):
        self.value -=1

c1 = Counter()
c2 = Counter(10)

while c1.value != c2.value:
    c1.up()
    c2.down()
    print(c1.value, c2.value)
