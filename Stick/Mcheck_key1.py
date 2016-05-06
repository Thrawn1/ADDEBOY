def check_key(k, l):
        print(k,l)
        if k == 1 and l == 1:
                #x_speed_left = -3
                #x_speed_right = 0
                #y_speed_down = -3
                #y_speed_up = 0
                z = (-3, 0 , -3, 0)
        elif k == 2 and l == 2:
                #x_speed_left = 0
                #x_speed_right = 3
                #y_speed_up = 0
                #y_speed_down = 3
                z = (0, 3, 0, 3)
        elif k ==1 and l == 2:
                #x_speed_left = -3
                #x_speed_right = 0
                #y_speed_up = 0
                #y_speed_down = 3
                z = (-3, 0, 0, 3)
        elif k == 2 and l == 1:
                #x_speed_left = 0
                #x_speed_right = 3
                #y_speed_down = -3
                #y_speed_up = 0
                z = (0, 3, -3, 0)
        elif k == 1 and l == 0:
                #x_speed_left = -3
                #x_speed_right = 0
                #y_speed_down = -3
                #y_speed_up = 0
                z = (-3, 0 , 0, 0)
        elif k == 2 and l == 0:
                #x_speed_left = 0
                #x_speed_right = 3
                #y_speed_up = 0
                #y_speed_down = 3
                z = (0, 3, 0, 0)
        elif k ==0 and l == 1:
                #x_speed_left = -3
                #x_speed_right = 0
                #y_speed_up = 0
                #y_speed_down = 3
                z = (0, 0, -3, 0)
        elif k == 0 and l == 2:
                #x_speed_left = 0
                #x_speed_right = 3
                #y_speed_down = -3
                #y_speed_up = 0
                z = (0, 0, 3, 0)
        else:
                z = (0,0,0,0)
        return z
        #x_speed_left, x_speed_right, y_speed_down, y_speed_up