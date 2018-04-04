def ascending(a):
    if sorted(a) == a:
        return True
    else:
        return False

def alternating(b): 
    if len(b) == 0 or len(b) == 1:
        return True
    
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            return False
  
    for i in range(2,len(b)):
        if b[i-2] > b[i-1] :
            if  (b[i] < b[i-1]):
                return False
        elif b[i-2] < b[i-1]:
            if  (b[i] > b[i - 1]):
                return False
    return True


  
def matmult (m1, m2):
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    cols_m2 = len(m2[0])


    res = [[0 for row in range(cols_m2)] for col in range(rows_m1)]

    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                res[i][j] += m1[i][k] * m2[k][j]
    return res
  
