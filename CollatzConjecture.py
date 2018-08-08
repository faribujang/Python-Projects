def CollatzConjecture(x):
        seq = [x]
        if x < 0:
                return []
        while x > 1:
                if x % 2 == 0:
                        x = x/2
                else:
                        x = 3*x+1
                seq.append(x)
        return seq
print (CollatzConjecture(20))

