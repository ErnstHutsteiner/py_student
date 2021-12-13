import random


names = ['Finished Parts Shop','Sepps Handel','Paris Velo','Aussi Cycles']
country = ['Australien','Deutschland','Frankreich', 'USA']


def people_list(num_people):
    results = []
    for i in range(num_people):
        person = (
                    random.choice(names),
                    random.choice(country)
                  )
        results.append(person)
    return results

ret = people_list(30)
print(ret)