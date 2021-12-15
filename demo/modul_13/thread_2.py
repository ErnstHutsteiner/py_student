import time
start = time.perf_counter()

def test_func():
    print('kurz warten...')
    time.sleep(1)
    print('fertig')

# jetzt lassen wir die test_func 2x laufen
test_func()
test_func()

finish = time.perf_counter()
timediff = round(finish - start, 2)
print(f"Fertig innerhalb von {timediff} Sekunden")

# Ergebnis : Dauer ca. 2s
# wie erwartet ein typischer sync task

