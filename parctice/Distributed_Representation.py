import numpy as np

input = np.array([[0,1,2,4],
                  [1,5,7,9],
                  [2,7,9,6],
                  [4,9,6,7]])

def dr(x,positive):
    sum_row = x.sum(0)
    sum_col = x.sum(1)

    sum = sum_row.sum()

    expected = np.outer(sum_row,sum_col)/sum
    x = x/expected
    x = np.log2(x)


    x[np.isinf(x)] = 0.0
    x[x<0] = 0.0
    return expected

print(dr(input,1))