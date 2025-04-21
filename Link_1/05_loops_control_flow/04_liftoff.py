# count down
import time
countdown_time = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def countdown():
    for i in countdown_time:
        print(i)
        time.sleep(10)
    print("Liftoff!")
    
    
    
if __name__ == '__main__':    
    countdown()