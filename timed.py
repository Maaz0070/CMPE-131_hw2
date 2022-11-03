import time

def timeme(func):
    
    def total():
        begin = time.time()
        func()
        end = time.time()
        
        print("Total time ", end-begin)
        
    return total()

def timer():
    time.sleep(2)
