# Have a look at the following numbers.

#  n | score
# ---+-------
#  1 |  50
#  2 |  150
#  3 |  300
#  4 |  500
#  5 |  750

#Can you find a pattern in it? If so, then write a function 
# getScore(n)/get_score(n)/GetScore(n) which returns the score 
# for any positive number n.

from imp import get_suffixes


def get_score(n):
    return sum(range(n+1))*50

print(get_score(2))