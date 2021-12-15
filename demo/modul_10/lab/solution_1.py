import pickle

# pickle

file = 'maria'

my_sample = {
    "Name" : "Maria",
    "Alter" : 21,
    "ledig" : True,
    "student" : False,
    "eltern" : ["Karla", "Manfred"],
    "rente" : None,
    "ausbildung" : {
        "schule" : "Abitur",
        "beruf" : "Polizistin"
    }
 }

outfile = open(file, 'wb')
pickle.dump(my_sample, outfile)
outfile.close()

# unpickle

infile = open(file, 'rb')
this_dictionary = pickle.load(infile)
infile.close()
print(this_dictionary)