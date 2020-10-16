from hashtable import *
from random import randint
testList  =  []

TINI      =  1
LOW       =  10
STANDARD  =  100
HIGH      =  10000
MEGA      =  100000

# h0 = hashTable(TINI)
# h1 = hashTable(STANDARD, 97)
# h2 = hashTable(STANDARD, 97)
h3 = hashTable(HIGH, 9973)
# h4 = hashTable(MEGA)

# testList.append(h0)
# testList.append(h1)
# testList.append(h2)
testList.append(h3)
# NOTE: below hashTable takes roughly !!80!! seconds to initialize when profiled with cProfile. Not reccomended.
# testList.append(h4)


#fillTest fills hashtable to capacity; uses a determine the loadfactor.
def fillTest(h, a):
    for x in range(0, int(a * h.size)):
        n = randint(0,1000000)
        h.set(n, n) # Insert keys
    return True    


#randSetTest sets a value between 0 and 9 to that same value.
def randSetTest(h):
    i = randint(0,h.size - 1)
    j = i
    if(h.set(i,j)):
        return(h.get(i) == j)
    else:
        return False

#deleteTest randomly deletes a node whose key is between 0 and 9.
def deleteTest(h):
    i = randint(0,h.size - 1)
    if (h.delete(i) == None):
        return False
    else:
        return True

def randSearch(h):
    for x in range(0,5000):
        n = randint(0,1000000)
        h.get(n, n) # Insert keys
    return True    


def displayBuckets(h):
    for x in h.bucket:
        if(x != None):
            print(x.value)
        else:
            print('-')    


def runTests(h):
    print("TEST: Filling random key to all available key slots")
    if(fillTest(h, 0.75)):
        print("SUCCEEDED")
    else:
        print("FAILED")
        return False

    # Display all the keys in the buckets
    # displayBuckets(h)


    # Search random 5k keys
    # print("TEST: Search random key in all available key slots")
    # if(randSearch(h)):
    #     print("SUCCEEDED")
    # else:
    #     print("FAILED")
    #     return False
    


    h.statictic()

    # if(randSetTest(h)):
    #     print("SUCCEEDED")
    # else:
    #     print("FAILED")
    #     return False

    # print("TEST: Deleting existing key value pair")
    # if(deleteTest(h)):
    #     print("SUCCEEDED")
    # else:
    #     print("FAILED")
    #     return False

    return True

for h in testList:
    print("Starting test cases on hashtable of size: " + str(h.size))
    if((runTests(h))):
        print("TEST SUITE PASSED")
    else:
        print("TEST FAILED, TERMINATING EXECUTION")
        break
    print("")
