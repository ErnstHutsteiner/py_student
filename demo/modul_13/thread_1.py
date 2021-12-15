import time
start = time.perf_counter()

def test_func():
    print('kurz warten...')
    time.sleep(1)
    print('fertig')

test_func()

finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# Ergebnis : Dauer ca. 1s
# goto thread_2
