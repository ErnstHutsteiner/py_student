import os

def open_file(filename):
    return open(filename, "r")

def read_lines(file):
    lines = file.readlines()
    count = lines.__len__()
    return lines, count


def new_file(file):
    try: 
        if os.path.exists(file):
            os.remove(file)      
        this_file = open(file, "w")
        this_file.close()
        return True
    except:
        return False


def append_line(file, line):
    this_file = open(file, "a")
    this_file.write(line)
    this_file.close

new_file_name = "new_file.txt"
counter = 0

my_file = open_file("module.txt")
my_lines_lines, my_lines_count  = read_lines(my_file)
my_file.close()
my_new_file = new_file(new_file_name)


for lines in my_lines_lines:
    if counter % 2 == 0:
        append_line(new_file_name, lines)
    counter += 1    


