# random_module.py
import random

# 시드: 같은 결과를 보장
# random.seed(412)    

animals = ["너구리", "강아지", "곰", "호랑이"]

print(random.choice(animals))

print(random.sample(animals, 2))
print(random.sample(animals, 3))

print(random.randint(1, 45))