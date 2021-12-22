import time
import numpy as np

def main():
    with open('input') as f:
        lines = f.read().splitlines()
    xstr,ystr = lines[0].removeprefix("target area:" ).split(",")
    
    xstr = xstr.removeprefix(" x=")
    xmin,xmax = xstr.split("..")
    xmin = int(xmin)
    xmax = int(xmax)

    ystr = ystr.removeprefix(" y=")
    ymin,ymax = ystr.split("..")
    ymin = int(ymin)
    ymax = int(ymax)
    
    x_start_speed = xmax
    y_start_speed = ymin


    heights = set()

    for x_start_speed in range(0,xmax+1):
        for y_start_speed in range(ymin,1000):
            pos_x,pos_y = 0,0
            x_speed = x_start_speed
            y_speed = y_start_speed
            max_h = 0
            while True:
                pos_x += x_speed
                pos_y += y_speed

                if x_speed > 0:
                    x_speed -= 1
                elif x_speed < 0:
                    x_speed += 1
                
                y_speed -= 1

                max_h = max(max_h,pos_y)
                
                if xmin <= pos_x <= xmax  and ymin <= pos_y <= ymax : # ce sm zadeu
                    heights.add(max_h)
                    break

                elif ymin > pos_y or xmax < pos_x: #miss
                    break

            
    print(max(heights))



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Time is : {end - start}') 