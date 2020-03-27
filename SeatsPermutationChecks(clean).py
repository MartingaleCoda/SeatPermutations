from itertools import permutations

placement = list(range(1,8))
seatcombs = list(permutations(range(2,8)))
seatcombsaslists = list()
seatcombs1match = list()
successes = list()

# change the permutation tuples into lists (and append the missing 1 to the front) for ease of use
for comb in seatcombs:
    combaslist = list(comb)
    combaslist.insert(0,1)
    seatcombsaslists.append(combaslist)

#filter out permutations that start with only one match
for comblist in seatcombsaslists:
    matching = 0
    for i in range(len(comblist)):
        if comblist[i] == placement[i]:
            matching = matching + 1
    if matching == 1:
        seatcombs1match.append(comblist)

#check all rotations
for item in seatcombs1match:
    listtocheck = item
    matchingamountlist = list()
    for j in range(len(listtocheck)):
        matching = 0
        rotatedlist = listtocheck[-j:] + listtocheck[:-j]
        for k in range(len(rotatedlist)):
            if rotatedlist[k] == placement[k]:
                matching += 1
        matchingamountlist.append(matching)
    if all(i < 2 for i in matchingamountlist):
        successes.append(listtocheck)

#print successes
for item in successes:
    print(item)