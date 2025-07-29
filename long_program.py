import os
import time

pid = os.getpid()

data = []
i = 0

while True:
    i += 1
    print(f'PID: {pid}, Iteration: {i}')
    data.append(' ' * 10 ** 6)
    time.sleep(1)
