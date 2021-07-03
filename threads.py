import threading
import time

def blocker():
    while True:
        print ("Oh, sorry, am I in the way?")
        time.sleep(1)

t = threading.Thread(name='child procs', target=blocker)
t.start()

# Prove that we passed through the blocking call
print ("No, that's okay" )