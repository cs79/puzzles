# puzzle - september

# borrowed
def factors(n):
    return list(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

# helper function to get product of a list
from operator import mul
def listproduct(list):
    return reduce(mul, list, 1)


# my code
import itertools
import collections

def get_threes(num):
    facs = factors(num)
    facs = [n for n in facs if n < 19] * 3  # full possible set of ages to draw combinations from
    temp = itertools.combinations(facs, 3)
    threes = list(set([cand for cand in temp if listproduct(cand) == num])) # need to sort these
    threes = set([tuple(sorted(item)) for item in threes])  # get unique triples
    three_sums = {x: sum(x) for x in threes}
    match_sum = [item for item, count in collections.Counter(three_sums.values()).items() if count > 1]
    # only exactly one match is valid, else the "knowing the address" logic fails:
    if len(match_sum) == 1:
        match_sum = match_sum[0]
    # pull out the age triples with (unique) matching sums:
    matches = []
    for key, value in three_sums.iteritems():
        if value == match_sum:
            matches.append(key)
    # ensure that we have a single "oldest child"
    top_tuple_counts = [match.count(max(match)) for match in matches]
    # if 1 is a unique top tuple count, we satisfy the logical condition
    one_count = top_tuple_counts.count(1)
    if one_count == 1:
        return(True)
    else:
        return(False)

test = [get_threes(i) for i in range(72,1000)]
for i in range(len(test)):
    if test[i] == True:
        print i + 72

# 288 is the next largest value for which this condition holds, then 576
