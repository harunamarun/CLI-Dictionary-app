import sys
from dictionaries import DictionaryBase, HashDictionary, ListDictionary,\
    TrieDictionary
from utils import get_suggestions
import time


def show_help():
    print("")
    print("--- command list ---")
    print("| * SEARCH COMMAND")
    print("|\t> find [word]")
    print("|\t> find_word_by_prefix [word]")
    print("| * DICTIONARY COMMAND")
    print("|\t> insert [word] [description]")
    print("|\t> update [word] [description] [index]")
    print("|\t> delete [word] [index]")
    print("|\t> save [filename]")
    print("|\t> help")
    print("|\t> end")
    print("---------------------")
    print("")


def process_find(args):
    if len(args) != 1:
        print("invalid args")
        return
    word = args[0]
    desc_array = dictionary.find(word)
    if len(desc_array) == 0:
        suggested_words = get_suggestions(word, dictionary.get_all_words())
        if len(suggested_words) > 0:
            print("Did you mean: " + ", ".join(suggested_words))
            print("")
        else:
            print(word, "doesn't exist in this dictionary.")
            print("")
    else:
        print("     index | description")
        print("----------------------------")
        for index, desc in enumerate(desc_array):
            print("\t", index, "|", desc)
        print("")


def process_find_word_by_prefix(args):
    if len(args) != 1:
        print("invalid args")
        return
    prefix = args[0]
    word_array = dictionary.find_word_by_prefix(prefix)
    if len(word_array) == 0:
        print("no word has prefix: ", prefix)
        print("")
    else:
        print("     index | description")
        print("----------------------------")
        for index, word in enumerate(word_array):
            print("\t", index, "|", word)
        print("")


def process_delete(args):
    if len(args) != 2:
        print("invalid args")
        return
    word = args[0]
    index = int(args[1])
    if dictionary.delete(word, index):
        print("Successfly deleted")
        print("")
    else:
        print("Failed to delete")
        print("")


def process_insert(args):
    if len(args) != 2:
        print("invalid args")
        return
    word = args[0]
    description = args[1]
    if dictionary.insert(word, description):
        print("Successfly inserted")
        print("")
    else:
        print("Failed to insert")
        print("")


def process_update(args):
    if len(args) != 3:
        print("invalid args")
        return
    word = args[0]
    description = args[1]
    index = int(args[2])
    if dictionary.update(word, description, index):
        print("Successfly updated")
        print("")
    else:
        print("Failed to update")
        print("")


def process_save(args):
    if len(args) != 1:
        print("Invalid args")
        return
    filename = args[0]
    dictionary.save_to_file(filename)
    print("Save Completed")
    print("")


args = sys.argv
if len(args) != 3 or args[1] not in ["list", "hash", "trie"]:
    print("invalid args")
    print("usage: app.py [backend] [dictinary_file_path]")
    print("backend:")
    print("\t list :list_dictionary")
    print("\t hash :hash_dictionary")
    print("\t trie :trie_dictionary")
    print(
        "dictinary_file_path: path to the dictinary file.")
    exit(0)
backend = args[1]
file_path = args[2]

dictionary: DictionaryBase
if backend == "list":
    dictionary = ListDictionary()
elif backend == "hash":
    dictionary = HashDictionary()
elif backend == "trie":
    dictionary = TrieDictionary()

print("")
print("Using backend:", dictionary.__class__.__name__)
print("Using source:", file_path)
print("")
print("Loading....")
start = time.time()
dictionary.load_from_file(file_path)
loading_time = time.time() - start
print("Loading Completed🍻!!!! ", "{:.2f}".format(loading_time), "[sec]")
show_help()

while True:

    print(" > ", end='')
    user_input = input()
    user_input_arr = user_input.split()
    if len(user_input_arr) < 1:
        continue
    command = user_input_arr[0]

    if command == "find":
        process_find(user_input_arr[1:])
    elif command == "insert":
        process_insert(user_input_arr[1:])
    elif command == "update":
        process_update(user_input_arr[1:])
    elif command == "delete":
        process_delete(user_input_arr[1:])
    elif command == "find_word_by_prefix":
        process_find_word_by_prefix(user_input_arr[1:])
    elif command == "save":
        process_save(user_input_arr[1:])
    elif command == "help":
        show_help()
    elif command == "end":
        print("Bye!!")
        break
    else:
        print("invalid command")
        show_help()
