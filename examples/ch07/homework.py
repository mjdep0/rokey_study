#3번

def calculate_area(length, width = 10) : 
    return length*width

print(calculate_area(5))
print(calculate_area(5,20))

#4번
def add_numbers(a, b) : 
    return a + b
print(add_numbers(10, 20))

#5번
def inner_function(x, y) : 
    return x+y

def outer_function(x, y) : 
    return inner_function(x,y)

add_10 = outer_function(10,5)
print(add_10)

#6번
def add_numbers(a, b):
    global result
    result = a + b

add_numbers(2, 3)
print(result)

#7번
def message() :
    print("A")
    print("B")
message()
print("C")
message()

#8번
print("A")
def message() :
    print("B")
print("C")
message()
