
# Submitted by Samy Vilar <samy_vilar> on 06/20/2026

# For the sake of simplicity assume 1-indexing, for 
# each distinct symbol keep track of the last the 
# occurrence, assuming we initialize all last
# occurrences to 0, it would suffice to take
# the minima among all other symbols last 
# witnessed;

# In general O(n * log(|alpha|)) time w/ O(|alpha|) 
# additional-space if we where to use a (ideally a priority)
# min heap to keep track of said minimas
# though given our contraints it would suffice
# to "manually" check;

# version 1.1 vectorized

import numpy

ids = bytearray(256)
ids[98:100] = 1, 2

def numberOfSubstrings(
    s: str, ids=bytes(ids),
    indices=numpy.arange(1, 50_001, dtype=numpy.uint16)
) -> int:
    s = numpy.frombuffer(s.encode().translate(ids), dtype=numpy.uint8)
    places = numpy.zeros((3, s.size + 1), dtype=numpy.uint16)
    indices = indices[:s.size]
    places[s, indices] = indices
    return numpy.maximum.accumulate(places, axis=1, out=places)\
        .min(axis=0)\
        .sum()\
        .item()    
    
    # total = last_a = last_b = last_c = 0    
    # for at, ch in enumerate(s, 1):
    #     if ch == 'a':
    #         total += last_b if last_b <= last_c else last_c
    #         last_a = at
    #     elif ch == 'b':
    #         total += last_a if last_a <= last_c else last_c
    #         last_b = at
    #     else:
    #         total += last_a if last_a <= last_b else last_b
    #         last_c = at
    # return total


Solution = repeat(namedtuple('Solution', ('numberOfSubstrings',))(
    numberOfSubstrings
)).__next__
        