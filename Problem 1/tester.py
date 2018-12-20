import importlib
import os
import chromosome

# get all the tests
test_path = os.getcwd() + "/tests/"
test_names = set()
for filename in os.listdir(test_path):
    filebase = filename.split(".")[0]
    test_names.add(filebase)

# go through each test
for test in sorted(test_names):
    result = ""
    with open(test_path+test+".txt") as f:
        dict = {}
        for line in f:
            split = line.split(" ")
            organism = " ".join(split[:-1])
            chromosomes = int(split[-1])
            dict[organism] = chromosomes
        result = str(chromosome.most_chromosomes(dict))
    with open(test_path+test+".out") as f:
        answer = f.readline().strip()
        if answer == result:
            print(test + ": PASS")
        else:
            print(test + ": FAIL")
