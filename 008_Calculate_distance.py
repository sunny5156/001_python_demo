
import math
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def closest(pt, others):
    return min(others, key = lambda i: distance(pt, i))


>>> closest((9, 2), {(0, 0), (10, 0), (10, 10)})
(10, 0)

#计算平均距离

def avgDistance(pt, others):
    dists = [distance(pt, i) for i in others]
    return sum(dists) / len(dists)

>>> avgDistance((9, 2), {(0, 0), (10, 0), (10, 10)})
6.505956727697075