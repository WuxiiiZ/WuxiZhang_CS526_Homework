import sys

def readfile(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    n = int(lines[0])

    men_pref = {}
    women_pref = {}
    for i in range(1, n+1):
        arr = lines[i].split()
        man = arr[0]
        preference = arr[1:]
        men_pref[man] = preference  # man preference lst
    
    for i in range(n+1,2*n+1):
        arr = lines[i].split()
        woman = arr[0]
        preference = arr[1:]
        women_pref[woman] = preference
    return n, men_pref, women_pref

def women_preference(women_pref):
    women_rankings = {}     # {woman: {man: rank}}
    for woman, pref in women_pref.items():
        rank = {}           # {man : rankIndex}
        for i, man in enumerate(pref):
            rank[man] = i
        women_rankings[woman] = rank
    return women_rankings

def gale_shapley(n, men_pref, women_rankings):
    unpaired_men = list(men_pref.keys())
    paired = {}    # paired[woman] = man
    next_proposal = {}
    for man in men_pref:
        next_proposal[man] = 0
    while unpaired_men:
        man = unpaired_men.pop(0)
        pref = men_pref[man]
        woman = pref[next_proposal[man]] # the next woman in this man's preference list
        next_proposal[man] += 1  # man will propose to the next woman next time
        if woman not in paired:
            paired[woman] = man  # woman hasn't been paired
        else:   # woman has been paired: compares this man with her current partner
            chosen_man = paired[woman]
            # prefer the new man over current partner
            if women_rankings[woman][man] < women_rankings[woman][chosen_man]: 
                paired[woman] = man
                unpaired_men.append(chosen_man)
            else:
                unpaired_men.append(man)
    return paired

# python3 Problem3.py ./marriage/marraige_ten.txt
# python3 Problem3.py ./marriage/marraige_thousand.txt
# python3 Problem3.py ./marriage/marriage_hundred.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    n, men_pref, women_pref = readfile(filename)
    women_rankings = women_preference(women_pref)
    pairs = gale_shapley(n, men_pref, women_rankings)
    for woman, man in pairs.items():
        print(man, woman)

