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

# #check
# print(seatcombsaslists)

#gotta find ones with only ONE match and filter those out
for comblist in seatcombsaslists:
    matching = 0
    for i in range(len(comblist)):
        if comblist[i] == placement[i]:
            matching = matching + 1
    if matching == 1:
        seatcombs1match.append(comblist)
# #check
# print(seatcombs1match)

# #gotta rotate now
# #rotate one first to make sure it works how I expect
# listtocheck = seatcombs1match[0]
#
# #this works for rotating one
# matchingamountlist = list()
# for j in range(len(listtocheck)):
#     matching = 0
#     rotatedlist = listtocheck[-j:] + listtocheck[:-j]
#     for k in range(len(rotatedlist)):
#         if rotatedlist[k] == placement[k]:
#             matching += 1
#     matchingamountlist.append(matching)
# if all(i < 2 for i in matchingamountlist):
#     successes.append(listtocheck)

#loop and do it for each one
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

#print one that works
# print(successes[0])

# #make sure its not lying. Check each rotation manually.
# listtocheck = successes[0]
# matchingamountlist = list()
# for j in range(len(listtocheck)):
#     matching = 0
#     rotatedlist = listtocheck[-j:] + listtocheck[:-j]
#     for k in range(len(rotatedlist)):
#         if rotatedlist[k] == placement[k]:
#             matching += 1
#     print(placement)
#     print(rotatedlist)
#     print()
#     matchingamountlist.append(matching)
# print(matchingamountlist)
# #yes it works

#all successes
for item in successes:
    print(item)