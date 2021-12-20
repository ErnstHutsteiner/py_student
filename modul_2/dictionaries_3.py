# verschachtelte Dictionaries

my_bikes = {
    "MTB" : {
        "Marke" : "Cube", 
        "Schaltung" : "Kette", 
        "Bremse" : "Disk", 
        "Laufrad": 26
    },
    "Trekking" : {
        "Marke" : "vsf", 
        "Schaltung" : "Kette", 
        "Bremse" : "Felge", 
        "Laufrad": 28
    },
    "Renner" : {
        "Marke" : "Cannondale", 
        "Schaltung" : "Kette", 
        "Bremse" : "Felge", 
        "Laufrad": 28
    }
}

# loop through
for nodes in my_bikes:
    print(my_bikes[nodes])