def get_positive_input(prompt):
    while True:
        text = input(prompt)
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Invalid input. Try again.")

n = get_positive_input("Enter a positive number: ")
numbers = []

for i in range(1, n+1):
    numbers.append(i)

print(numbers)
print("The sum of the numbers is:", sum(numbers))