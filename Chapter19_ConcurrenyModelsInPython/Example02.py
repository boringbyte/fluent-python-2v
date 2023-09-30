import time
import itertools
from multiprocessing import Process, Event, synchronize
from Chapter17_IteratorsGeneratorsAndCoroutines.Example01 import slow, spin


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
