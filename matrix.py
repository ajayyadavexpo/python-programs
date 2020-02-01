m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
m3 = []
for row in 	range(0,len(m1)):
	for column in range(0,len(m1)):
			result = m1[row][column]+m2[row][column]
			m3.append(result)
			# m3[row][column] = result



print(m3)