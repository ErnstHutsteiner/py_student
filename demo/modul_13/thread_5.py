import threading
import time
start = time.perf_counter()

# jetzt mit mehreren Threads und Argumenten

def test_func(sekunden):
    print(f'{sekunden} warten...')
    time.sleep(sekunden)
    print(f'{sekunden} sind um')


# Threads bauen
threads = []

for _ in range(10):
    thread = threading.Thread(target=test_func, args=[2])
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()    


finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# wow nur 2 Sekunden statt 20!


