class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def taste(self):
        print(f"{self.name}는 새콤하다")

orange = Fruit(name='오렌지', color='노란색')

print(f"이름: {orange.name}")
print(f"색상: {orange.color}")

orange.taste()