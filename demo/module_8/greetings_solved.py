
def guten_tag():
    print("Guten Tag")

def servus():
    print("Servus")
    print('Scope von Servus : ', __name__)

def moin():
    print("Moin")

if __name__ == '__main__':
    
    guten_tag()
    print('Scope des Aufrufs : ', __name__)
