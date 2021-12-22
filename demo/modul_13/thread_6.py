# wir steigen um auf concurrent.futures

import concurrent.futures
import time

start = time.perf_counter()

def test_func(sekunden):
    print(f'{sekunden} warten...')
    time.sleep(sekunden)
    return "fertig" # jetzt mit return statt mit print

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor_1 = executor.submit(test_func, 1)
    executor_2 = executor.submit(test_func, 1)

    print(executor_1.result())
    print(executor_2.result())


finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# soweit so gut
# goto thread_7

