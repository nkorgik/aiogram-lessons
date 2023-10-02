import concurrent.futures

from math import sqrt
from timeit import default_timer as timer


def is_prime(x: int) -> bool:
    """The funciton calculates if given number is integer

    Args:
        x (int): the input value
    """

    if x < 2 or x % 2 == 0:
        return False

    if x == 2:
        return True
    
    limit = int(sqrt(x)) + 1

    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    
    return True


def main() -> None:
    """Entry Point"""
    
    _input = [i for i in range(10**13, 10**13 + 500)]
    output = []
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(is_prime, x) for x in _input]
        
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                output.append(_input[i])
    
    return output


if __name__ == "__main__":
    start = timer()
    result = main()
    print(result)
    print(f'Executed in {timer() - start}')

# In sequence execution - Executed in 1.247336040949449
# In parallel execution - Executed in 0.6263990000588819
