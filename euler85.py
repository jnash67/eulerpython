import numpy as np


# for the purposes of this problem an m x num grid is the same as an num x m grid
# the same number of rectangles will fit in either, regardless of rotation
def num_rect(maxm, maxn):
    assert (maxm >= maxn, "Rows should be bigger than columns, otherwise rotate")
    rcount = 0
    for n in range(1, maxn + 1):
        for m in range(n, maxm + 1):
            # see how many m x num rectangles fit going across and down
            valmn = (maxm - m + 1) * (maxn - n + 1)
            #print("For {}x{} we have {}".format(m, num, valmn))
            rcount += valmn
            if (m != n):
                if (m <= maxn):
                    # do it for num x m as well if we can
                    valnm = (maxm - n + 1) * (maxn - m + 1)
                    #print("For {}x{} we have {}".format(num, m, valnm))
                    rcount += valnm
    return rcount


# all the subrectangles are consecutive subsequences of length of some factor or multiple of a factor
# factors of 6 are 1,2,3,

# so for an m x num grid, we expect m to be the bigger or else m == num
# grid = (3, 2)
# grid_area = 3*2
# arealist = list(range(1,grid_area+1))
#
# result = [arealist[i:j] for i in range(0,len(arealist)) for j in range(i+1, len(arealist)+1)]
# for r in result:
#     print(r)
# print(len(result))

# print(num_rect(3, 2))
# print(num_rect(3, 3))
# print(num_rect(5, 4))

size = 2500
twomil = 2000000
nearest_size = (1,1)
nearness = twomil

rects = np.zeros((size, size))
for n in range(1, size + 1):
    for m in range(n, size + 1):
        val = num_rect(m, n)
        if val > twomil+nearness:
            break
        if abs(twomil - val) < nearness:
            nearness = abs(twomil - val)
            nearest_size = (m,n)
        rects[m-1,n-1] = val
    print("Nearest is currently {} with nearest {}".format(nearest_size,nearness))

print("The nearest grid is {} with nearness {}".format(nearest_size, nearness))
print("The it has {} rects and area {}".format(rects[nearest_size[0]-1,nearest_size[1]-1], nearest_size[0]*nearest_size[1]))
