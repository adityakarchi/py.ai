import random
n = random.randint(1, 10)
print("Guess a number between 1 and 10")
for i in range(3):
    g = int(input("Your guess: "))
    if g == n:
        print("🎉 Correct!")
        break
    else:
        print("❌ Try again")
else:
    print(f"😞 Out of tries! The number was {n}")
