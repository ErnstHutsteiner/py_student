import threading
import time
start = time.perf_counter()

def test_func():
    print('kurz warten...')
    time.sleep(1)
    print('fertig')

# Threads bauen
thread_1 = threading.Thread(target=test_func)
thread_2 = threading.Thread(target=test_func)

# und ausführen
thread_1.start()
thread_2.start()

# mit join

thread_1.join()
thread_2.join()

finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# Ergebnis : Fertig innerhalb von 1.01 Sekunden
# wie erwartet!
# join hat dafür gesorgt, dass die Applikation den
# Threads nicht mehr "davonläuft"
# goto: thread_5



