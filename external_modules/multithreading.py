# multiprocessing and multitheading are simmilar in meaning 

import threading
import time

def worker(num):
    print(f"Thread {num} : Starting")
    time.sleep(10)
    print(f"Thread {num} : Finishing")

threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join() # wait for all thread to finish 

print("All threads have been joined")

# go ahead and expore the multiprocessing module 