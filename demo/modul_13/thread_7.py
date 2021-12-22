# wir steigen um auf concurrent.futures

import concurrent.futures
import time

start = time.perf_counter()

def test_func(sekunden):
    print(f'{sekunden} warten...')
    time.sleep(sekunden)
    return "fertig" # jetzt mit return statt mit print

with concurrent.futures.ThreadPoolExecutor() as executor:
    # jetzt mit einer list comprehension
    outcome = [executor.submit(test_func, 1) for _ in range(10)]

    for results in concurrent.futures.as_completed(outcome):
        print(results.result())


finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")


