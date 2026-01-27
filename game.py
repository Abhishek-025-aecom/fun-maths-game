import random

print("Welcome to the Fun Maths Game 🎲")

score = 0

for _ in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a + b

    user_input = int(input(f"What is {a} + {b}? "))

    if user_input == answer:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌ The answer was {answer}")

print(f"\nGame Over! Your score: {score}/5")
