def check_key(k, l):
        print(k,l)
        if k == 1 and l == 1:
                z = (-3, 0 , -3, 0)
        elif k == 2 and l == 2:
                z = (0, 3, 0, 3)
        elif k ==1 and l == 2:
                z = (-3, 0, 0, 3)
        elif k == 2 and l == 1:
                z = (0, 3, -3, 0)
        else:
                z = (0,0,0,0)
        return z
