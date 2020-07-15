import time
from pynput.keyboard import Key, Controller as KeyboardController

# requires: pynput
# pip install pynput

keyboard = KeyboardController()

# Adjust minWait depending on your comp / net speed
# essentially cool down time between messages

minWait = 0.5

# Spam function
# Usage of pynput

def spamThis(inputString):
    keyboard.type(inputString)
    keyboard.press(Key.enter)
    time.sleep(0.05)
    keyboard.release(Key.enter)
    time.sleep(minWait)

def main():


    # Spam input, followed by handling

    spam = input("What to spam: ")
    amount = input("How many times (0 to loop forever): ")

    # Default iterations set to 0

    iterations = 0

    try:
        iterations = int(amount)

    except:

        # if "amount" input isn't a string which can be parsed to and int, raise

        raise ValueError("Amount must be a number, and not '0'.")

    # variable to add next word

    spamBuilder = spam

    # Countdown to tab into Twitch

    for x in range(0,5):
        print("Spamming in " + str(5-x))
        time.sleep(1)

    # Spam loop

    count = 0
    while True:
        if iterations != 0:
            if count >= iterations: 
                break
        if len(spamBuilder) >= 500:
            spamBuilder = spam
        else:
            spamThis(spamBuilder)
            spamBuilder += " " + spam
        count += 1

    print("Done.")

if __name__ == '__main__':
    main()
