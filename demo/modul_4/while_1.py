# while loops

loop_counter = 0
while loop_counter < 10:
    loop_counter += 1
    print(loop_counter)

# ...mit break
loop_counter = 0
while loop_counter < 10:
    loop_counter += 1
    if loop_counter == 5:
        break
    print(loop_counter)    

# .. mit continue
loop_counter = 0
while loop_counter < 10:
    loop_counter += 1
    if loop_counter == 5:
        continue
    print(loop_counter)    

# .. mit else
loop_counter = 0
while loop_counter < 10:
    loop_counter += 1
    print(loop_counter)
else:
    print("hier ist Ende")

# .. mit Benutzerinteraktion
loop_counter = 0
while loop_counter < 10:
    loop_counter += 1
    if loop_counter == 5:
        print("ich bin jetzt in der Mitte der Schleife")
        print("möchten Sie weiter machen? (j/n):")
        user_input = input("Ihre Eingabe")
        if user_input == "n":
            break
        if user_input == "j":
            continue
    print(loop_counter)