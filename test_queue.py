import collections
import random

D = collections.deque()

for i in xrange(1, 11):
    D.append(i)
# for j in xrange(5):
#     D.popleft()

# print D
# print random.sample(D, 3)

d = collections.deque(maxlen=2)
d.append(1)
d.append(2)
d.append(3)
# print d

