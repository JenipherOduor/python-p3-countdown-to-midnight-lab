
from time import sleep

def countdown(number):
    while number > 0:
        print(f'{number} SECOND (S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

countdown(5)

def countdown_with_sleep(number):

    while number > 0:
        print(f"{number} SECOND (S)!")
        sleep(1)
        number -=1
    print("HAPPY NEW YEAR!")

countdown_with_sleep(5)


