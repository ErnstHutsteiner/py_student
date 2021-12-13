
my_list = [20, 1001, 123, 765, "80", 100, 99, 5343, 343]

counter = 0

while counter < len(my_list) and type(my_list[counter]) == int:
    print(my_list[counter])
    counter = counter + 1

