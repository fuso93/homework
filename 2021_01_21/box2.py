
temp = input().split()
for i in range(len(temp)): temp[i] = int(temp[i])
box1 = temp[:4]
box2 = temp[4:]

box1_left_up = [box1[0], box1[3]]
box1_left_down = [box1[0], box1[1]]
box1_right_up = [box1[2], box1[3]]
box1_right_down = [box1[2], box1[1]]

box2_left_up = [box2[0], box2[3]]
box2_left_down = [box2[0], box2[1]]
box2_right_up = [box2[2], box2[3]]
box2_right_down = [box2[2], box2[1]]

if ((box1_right_up == box2_left_down) or
   (box1_right_down == box2_left_up) or
   (box1_left_up == box2_right_down) or
   (box1_left_down == box2_right_up)):
	print("POINT")

elif ((box1_left_down[1] > box2_right_up[1]) or
	  (box1_right_up[0] < box2_left_down[0]) or
	  (box2_left_down[1] > box1_right_up[1]) or
	  (box2_right_up[0] < box1_left_down[0])):
	print("NULL")



