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

finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# Ergebnis : Fertig innerhalb von 0.0 Sekunden
# nicht wie erwartet!
# Grund: Unser Script ist in der Zwischenzeit weiter gelaufen
# hat also nicht auf die Threads gewartet

# goto: thread_4



