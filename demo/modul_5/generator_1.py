import memory_profiler as mem_profile
import random
import time

names = ['Sepp','Resi','Lola','Hannes']
hobbies = ['schwimmen','lesen','schlafen']

init_memory = mem_profile.memory_usage()
print(f'Memory (Before): {init_memory}')

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(hobbies)
                  }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(hobbies)
                  }
        yield person


people = people_list(10000000)

# people = people_generator(10000000)


after_memory = mem_profile.memory_usage()
print(f'Memory (After): {after_memory}')
# print(f'Took {} Seconds'.format(t2-t1))


