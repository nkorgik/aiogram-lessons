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
    for i in _input:
        is_prime(i)


if __name__ == "__main__":
    start = timer()
    main()
    print(f'Executed in {timer() - start}')


