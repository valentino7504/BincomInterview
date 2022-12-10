import random

binary_digits = [0, 1]
binary_number_list = [str(random.choice(binary_digits)) for i in range(4)]
binary_number = "".join(binary_number_list)
base_ten = int(binary_number, 2)
print(f"8. The binary digit is {binary_number} and in base ten it is {base_ten}")
