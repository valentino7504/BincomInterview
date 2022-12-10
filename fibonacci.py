# FIBONACCI QUESTION
def fibonacci_generator(num):
    if num == 0 or num == 1:
        return num
    return fibonacci_generator(num-2) + fibonacci_generator(num-1)


fibonacci_array = []
n = 0
while len(fibonacci_array) <= 50:
    fibonacci_array.append(fibonacci_generator(n))
    n += 1
print(fibonacci_array)
print(f"9. The sum of the first {len(fibonacci_array)} terms of the Fibonacci sequence is {sum(fibonacci_array)}")

