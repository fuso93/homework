box = [3, 4, 9, 8]
dot = [[3, 6],
	   [6, 5],
	   [12, 6]]

for i in range(len(dot)):
	x = dot[i][0]
	y = dot[i][1]
	if (x > box[0] and x < box[2]) and (y > box[1] and y < box[3]):
		print(x, y, "in")
	elif (x < box[0]) or (x > box[2]) or (y < box[1]) or (y > box[3]):
		print(x, y, "out")
	else :
		print(x, y, "on")

'''
for i in dot: 3 6
    if j in box: 3 4 9 8 j[0] i[0]
        if (i[0] < j[0]) or (i[0]>j[2]) or (i[1]<j[1]) or (i[1]>j[3]):
            print('out')
        else :
            print('in')
'''
