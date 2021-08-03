import os

os.system('cls')

i = 0

for i in range(100):
    if i < 100 or i == 100:
        if i != 0:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            else:
                if i % 3 == 0:
                    print("Fizz")
                    continue
                if i % 5 == 0:
                    print("Buzz")
                    continue
                else:
                    print(i)
    else:
        break
