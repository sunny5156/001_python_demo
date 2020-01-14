#计算两点间的距离
def cal_distance(point_a, point_b):
    square_sum = 0
    for i in range(len(point_a)):
        square_sum += (point_a[i] - point_b[i])**2
    return math.sqrt(square_sum)