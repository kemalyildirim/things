import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class stat_params:
    circle_radius = 600
    map_width = 16000
    map_height = 9000

class cor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class dynamic_params:
    def __init__(self, x, y, n_check_x, n_check_y, n_check_dist, n_check_angle):
        self.p_cor = cor(x, y)
        self.c_cor = cor(n_check_x, n_check_y)
        self.dist = n_check_dist
        self.angle = n_check_angle

class intelly:
    def __init__(self):
        None

t_flag = True

while True:
    # next_checkpoint_angle: angle between your pod orientation
    # and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    op = cor(opponent_x, opponent_y)
    d = dynamic_params(x, y, next_checkpoint_x, next_checkpoint_y,
     next_checkpoint_dist, next_checkpoint_angle)
    
    print("Angle: ", d.angle, file=sys.stderr)
    print("Distance: ", d.dist, file=sys.stderr)
    # i.e.: "x y thrust"
    def f(x):
        p = math.sqrt(x)
        return 5 * math.asin(p) / math.pi
        
    ll = len(str(d.dist))
    divide = '10' + (ll-1) * '0'
    t = f(d.dist / int(divide)) 
    print("t value: ", t, file=sys.stderr)
    speed = t * 100
    print("Speed: ", speed, file=sys.stderr)
    if speed >= 100:
        speed = 100
    elif speed <= 0:
        speed = 1
    if d.dist > 3000 and t_flag:
        speed = "BOOST"
        #print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(speed))
        t_flag = False
        #continue
    if type(speed) is str:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(speed))
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(int(speed)))
    """
    if d.dist < 3000:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(int(80)))
    if d.dist < 1000:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(int(40)))
    else:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(int(100)))
    """
