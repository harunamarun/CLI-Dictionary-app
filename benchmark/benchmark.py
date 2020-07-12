import matplotlib.pyplot as plt
import time
import string
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))
from dictionaries import ListDictionary, HashDictionary, TrieDictionary

def random_str(str_len=10):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=str_len))


def measure_load_time(dictionary, word_data, desc_data):
    """mearesure time of load_from_file API"""
    filename = ".temp_benchmark"
    with open(filename, mode='w') as fileobj:
        for idx in range(len(word_data)):
            word = word_data[idx]
            desc = desc_data[idx]
            fileobj.write(word + "\t" + desc + "\n")
    start = time.time()
    dictionary.load_from_file(filename)
    duration = time.time()-start
    os.remove(filename)
    return duration


def measure_find(dictionary, word_data, desc_data):
    """measure time of find API"""
    for i in range(len(word_data)):
        dictionary.insert(word_data[i], desc_data[i])

    start = time.time()
    for word in word_data:
        dictionary.find(word)

    return (time.time()-start) / len(word_data)


def generate_test_date(record_num, word_len):
    word_data = []
    desc_data = []
    for i in range(record_num):
        word_data.append(random_str(word_len))
        desc_data.append(random_str())
    return word_data, desc_data


# relationship between record_num and time to load
test_backends = [(ListDictionary, range(100, 18000, 1000)),
                 (HashDictionary, range(10000, 160000, 10000)),
                 (TrieDictionary, range(10000, 160000, 10000))]
for test_backend in test_backends:
    x = []
    measured_times = []
    record_num_range = test_backend[1]
    for record_num in record_num_range:
        word_data, desc_data = generate_test_date(record_num, 10)
        backend = test_backend[0]()

        x.append(record_num)
        measured_time = measure_load_time(backend, word_data, desc_data)
        measured_times.append(measured_time)

    plt.plot(x, measured_times, label=backend.__class__.__name__)
plt.title("Relationship between number of records and time to load")
plt.xlabel("number of records")
plt.ylabel("time (s)")
plt.legend()
plt.show()

# relationship between record_num and time to find
test_backends = [(ListDictionary, range(100, 500, 100)),
                 (HashDictionary, range(10000, 160000, 10000)),
                 (TrieDictionary, range(10000, 160000, 10000))]
for test_backend in test_backends:
    x = []
    measured_times = []
    record_num_range = test_backend[1]
    for record_num in record_num_range:
        word_data, desc_data = generate_test_date(record_num, 10)
        backend = test_backend[0]()

        x.append(record_num)
        measured_time = measure_find(backend, word_data, desc_data)
        measured_times.append(measured_time)

    plt.plot(x, measured_times, label=backend.__class__.__name__)
plt.title("Relationship between number of records and time to find")
plt.xlabel("number of records")
plt.ylabel("time (s)")
plt.legend()
plt.show()

# relationship between word length and time to load
test_backends = [(ListDictionary, range(100, 901, 100)),
                 (HashDictionary, range(100, 901, 100)),
                 (TrieDictionary, range(100, 901, 100))]
for test_backend in test_backends:
    x = []
    measured_times = []
    word_len_range = test_backend[1]
    for word_len in word_len_range:

        word_data, desc_data = generate_test_date(5000, word_len)
        backend = test_backend[0]()

        x.append(word_len)
        measured_time = measure_load_time(backend, word_data, desc_data)
        measured_times.append(measured_time)

    plt.plot(x, measured_times, label=backend.__class__.__name__)
plt.title("Relationship between word length and time to load")
plt.xlabel("word length")
plt.ylabel("time (s)")
plt.legend()
plt.show()


# relationship between word length and time to find
test_backends = [(ListDictionary, range(100, 901, 100)),
                 (HashDictionary, range(100, 901, 100)),
                 (TrieDictionary, range(100, 901, 100))]
for test_backend in test_backends:
    x = []
    measured_times = []
    word_len_range = test_backend[1]
    for word_len in word_len_range:
        word_data, desc_data = generate_test_date(5000, word_len)
        backend = test_backend[0]()

        x.append(word_len)
        measured_time = measure_find(backend, word_data, desc_data)
        measured_times.append(measured_time)

    plt.plot(x, measured_times, label=backend.__class__.__name__)
plt.title("Relationship between word length and time to find")
plt.xlabel("word length")
plt.ylabel("time (s)")
plt.legend()
plt.show()
