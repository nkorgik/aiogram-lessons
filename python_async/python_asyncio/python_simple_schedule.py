import schedule 
import datetime
import time


def job():
    print('Hello, this is kinda job')
    

schedule.every(5).seconds.do(job) # define a time-based trigger
    

def main() -> None:
    while True:
        schedule.run_pending()
        
    
    
if __name__ == "__main__":
    main()

