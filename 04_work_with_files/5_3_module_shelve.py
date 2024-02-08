import shelve

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
    for state in states.items():
        print(state)

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])