import time

def loading(message):

    print()

    print(message)

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)

    print(" Done!\n")