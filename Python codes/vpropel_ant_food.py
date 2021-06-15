import math
height_of_tree=int(input())
dist_up=int(input())
dist_straight=int(input())
dist_down=int(input())
speed_up_mount=int(input())
speed_down_mount=int(input())
speed_straight=int(input())
speed_up_tree=int(input())
speed_down_tree=int(input())

time=(height_of_tree/speed_down_tree)+(height_of_tree/speed_up_tree) +((dist_straight*2)/speed_straight)+(dist_down/speed_down_mount) +(dist_down/speed_up_mount)+(dist_up/speed_up_mount)+(dist_up/speed_down_mount)
x=math.ceil(time)
y=int(x)//60
z=int(x)%60
print(y,z)