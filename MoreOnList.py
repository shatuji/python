#List comprehensions
squares = []
for x in range(10):
    squares.append(x**4)

print(squares)

squares = [x**3 for x in range(50)]
print(squares)
