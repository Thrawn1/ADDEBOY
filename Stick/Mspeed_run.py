from Mcheck_key1 import *
def speed_run(x_coord, y_coord,k,l):
        print (x_coord, y_coord)
        if x_coord > 785 or x_coord < 0 or y_coord > 570 or y_coord < 0:
                z = (0, 0, 0, 0)
        else:
                z = check_key(k, l)
        return z
