#
# TIM BUCHALKA'S COMPLETE PYTHON MASTERCLASS Created by Tim Buchalka, Jean-Paul Roberts, Tim Buchalka's Learn Programming Academy.
# This is a collection of my codes, generated by myself for learning Python
# his challenge is about understanding shelves in Python.
# Here is a link to the course: https://www.udemy.com/python-the-complete-python-developer-course/
# START OF CHALLENGE (TIM BUCHALKA)
#
# Modify the program from the Second Dictionary challenge of lecture 56
# to use shelves instead of dictionaries.
#
# Do this by creating two programs. cave_initialise.py should create the two
# shelves (locations and vocabulary) with the appropriate keys and values.
#
# START OF MY OWN CODE
import shelve

locations = shelve.open("locations")

locations["0"] = {"desc": {"You are sitting in front of a computer learning Python"},
                  "exits": {},
                  "namedExits": {}}

locations["1"] = {"desc": {"You are standing at the end of a road before a small brick building"},
                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}}

locations["2"] = {"desc": {"You are at the top of a hill"},
                  "exits": {"N": 5, "Q": 0},
                  "namedExits": {"5": 5}}

locations["3"] = {"desc": {"You are inside a building, a well house for a small stream"},
                  "exits": {"W": 1, "Q": 0},
                  "namedExits": {"1": 1}}

locations["4"] = {"desc": {"You are in a valley beside a stream"},
                  "exits": {"N": 1, "W": 2, "Q": 0},
                  "namedExits": {"1": 1, "2": 2}}

locations["5"] = {"desc": {"You are in the forest"},
                  "exits": {"W": 2, "S": 1, "Q": 0},
                  "namedExits": {"2": 2, "1": 1}}

print(locations)
print(locations["1"])
print(locations["2"])
print(locations["3"])
print(locations["4"])
print(locations["5"])
locations.close()

vocabulary = shelve.open("vocabulary")
vocabulary["vocabulary"] = {"QUIT": "Q",
                            "NORTH": "N",
                            "SOUTH": "S",
                            "EAST": "E",
                            "WEST": "W",
                            "ROAD": "1",
                            "HILL": "2",
                            "BUILDING": "3",
                            "VALLEY": "4",
                            "FOREST": "5"}

print(vocabulary)
for direction in vocabulary:
    print(direction, vocabulary[direction])

vocabulary.close()
