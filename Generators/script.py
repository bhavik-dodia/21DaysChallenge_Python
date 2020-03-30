import tracemalloc
import random
import time

names = ['John', 'Coret', 'Adam', 'Steve', 'rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id': i, 'name': random.choice(names), 'major': random.choice(majors)}
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {'id': i, 'name': random.choice(names), 'major': random.choice(majors)}
        yield person

tracemalloc.start()
t1 = time.process_time()
people = people_list(10**6)
t2 = time.process_time()
current, peak = tracemalloc.get_traced_memory()
print('List Memory usage: {} MB'.format(current / 10**6))
print('List Took {} Seconds'.format(t2-t1))
tracemalloc.stop()

tracemalloc.start()
t1 = time.process_time()
people = people_generator(10**6)
t2 = time.process_time()
current, peak = tracemalloc.get_traced_memory()
print('Generator Memory Usage: {} MB'.format(current / 10**6))
print('Generator Took {} Seconds'.format(t2-t1))
tracemalloc.stop()