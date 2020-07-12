# CLI-Dictionary-app
This is a CLI based dictionary app.
This was created during my time as a student at [Build@Mercari 2020](https://mercan.mercari.com/articles/19631/) Week3.
## Demo
<img src="https://user-images.githubusercontent.com/56245555/84596325-f57b1380-ae97-11ea-8180-baa0b3319dda.gif" width="700px">


## How to run
```
cd src
```
```
python3 app.py [backend] [filename]
```
[backend]   
+ `hash`   
+ `list`   
+ `trie`   

[filename]   
+ `words.txt`

For example   
```
python3 app.py hash words.txt
```
   
## Features
+ exact mach search   
    + suggest similar words when word does not exist in dictionary   
+ prefix search
+ insert 
+ update
+ delete
+ load from file
+ save to file
+ non ascii words support   
   
## What I focused on
**Three dictionary implementations**   
I used abstracted base class for dictionary and defined well designed APIs.   
I implemented dictionary in three ways using following data structures.   
• Hash Table(dict in python)   
• List   
• Trie Tree   
I provided well covering testcases and reuse them between all the implementations.


**Awesome CLI**   
• Accept arguments when start CLI   
• Usefull help command   

**Word suggestion**   
When the word users try to find does not exist in the dictionary, CLI shows similar words in the dictionary.   
For example, when user tried to find "aple", CLI show the message "Did you mean: able, ale, ample, ape, apple".   
I implemented this feature using edit distance algorithm.   
This is my first time :ghost:   

## Discussion
I supported three backend implementations (List, Trie Tree, and Hash).   
In this section, I will compare these implementations.

### Comptation Complexity
|          |  Hash      | List        | Trie Tree   |
|:---------|:----------:|:-----------:|:-----------:|
| load     | O(n)       | O(n * n)    | O(n * l)    |
| find     | O(1)       | O(n)        | O(l)        |
| insert   | O(1)*      | O(n)        | O(l)        |
| delete   | O(1)*      | Worst:O(n+m)| O(l)        |
| update   | O(1)       | O(n)        | O(l)        |   
   
m = number of descriptions for target word   
n = number of records   
l = len(word)   
*In general O(1) but if we we support prefix search, Comptation Complexity is O(l)   


### Benchmark
To verify above Comptation Complexity analysis, I conducted benchmark.   
In this benchmark, I disabled prefix search feature in HashDictionary.   


(In this measurement, I used random words which length is 10.)   
<img src="https://user-images.githubusercontent.com/56245555/84610007-078a9f80-aef4-11ea-8378-f3d770247647.png" width="300px">   
As you forcus on gradient, ListDictionary is very steep slope.   
TrieDictionary is steeper than HashDictionary.   

(In this measurement, I used random words which length is 10.)   
<img src="https://user-images.githubusercontent.com/56245555/84610004-048faf00-aef4-11ea-9853-1174ae6bbd72.png" width="300px">   
As for ListDictionary, when number of records increase, time to find also increase a lot.   
In contrast, time to find of HashDictionary and TrieDicationry does not change much.  

(In this measurement, I used 5000 record)   
<img src="https://user-images.githubusercontent.com/56245555/84607837-74993780-aeea-11ea-8242-5b15d5f8673e.png" width="300px"> <img src="https://user-images.githubusercontent.com/56245555/84607836-7400a100-aeea-11ea-8a47-7d47c814eddd.png" width="300px">   
As you can see, time to load/find of TrieDictionary increases when word length got Increase.   
In contrast, time to load/find of HashDictionary and ListDicationry is constant.   


### Hash v.s. Trie Tree
From the benchmark List looks not appropriate implementation.   
Because of that, in this section I will compare Hash and Trie Tree.   
Discussion is limited to my implementation.   
There are many more effecient implementation. (e.g. LOUDS)
#### Hash
Pros.   
+ Compitation complexity of APIs(e.g. find) doesn't depend on number of dictionary and word length.   
+ Hash is prepared in programing language such as dict of Python.   

Cons.   
+ Some features are difficult to implement. (e.g. using dictionary's order)

#### Trie Tree
Pros.   
+ Compitation complexity of APIs(e.g. find) doesn't depend on number of dictionary.   
+ We can implement functions using dictionary order in Trie Tree, which is difficult to implement in Hash.   

Cons.   
+ Compitation complexity of APIs(e.g. find) depend on word length.   
+  when word length is long, memory usage tends to be wasted.
