import threading
import time

def download_file():
    print("Downloading.....")
    time.sleep(3)
    print("Finished Downloading!")
    

t1 = threading.Thread(target=download_file)
t2 = threading.Thread(target=download_file)

t1.start()
t2.start()


t1.join()
t2.join()
print('succesfully completed')