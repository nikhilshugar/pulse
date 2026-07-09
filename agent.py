import psutil
import time

while True:
    #Getting the cpu percent. Here we have set interval=1, it is like a stopwatch we ask the cpu to wait for 1 sec calculate the avg usage of the cpu and print it
    cpu_percent = psutil.cpu_percent(interval=1)
    #Getting the Ram percent, it is kind of static.
    ram_percent = psutil.virtual_memory().percent
    print(f"The percentage of CPU being used is {cpu_percent}%")
    print(f"The percentage of RAM being used is {ram_percent}%")
    #We are in a while loop so we ask the computer/python to sleep for 2 seconds and then again repeat this loop.
    time.sleep(2)