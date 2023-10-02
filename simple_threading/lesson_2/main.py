import threading
import time

from typing import List


class MyThread(threading.Thread):
    def __init__(self, name: str, delay: int) -> None:
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay 
    
    def run(self) -> None:
        print(f'Starting {self.name} ...')
        threading_run(self.name, self.delay)
        print(f'Ending {self.name} ...')
        

def threading_run(name: str, delay: int) -> None:
    """Threading function. Does nothing LOL"""
    
    counter = 5
    
    while counter:
        time.sleep(delay)
        print(f'Thread {name} - {counter}')
        counter -= 1


if __name__ == "__main__":
    _threads: List[threading.Thread] = [
        MyThread('A', 1),
        MyThread('B', 0.5)
    ]
    
    for t in _threads:
        t.start()
    
    for t in _threads:
        t.join()
    
    print('Main finishes its tasks. Meow')
    
