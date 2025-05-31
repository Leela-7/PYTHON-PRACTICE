import time

def countdown(t):
    while t > 0:
        mins = t // 60
        secs = t % 60
        output = "Your Time left is {:02d}:{:02d}".format(mins, secs)
        print(output)
        time.sleep(1)
        t -= 1
    print("Time is Up")

def start():
    t = input("Enter the number of seconds:")
    if t.isdigit() and int(t) > 0:
        countdown(int(t))
    else:
        print("Was not a valid positive number")
        start()

if __name__ == "__main__":
    start()

