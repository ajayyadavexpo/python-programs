import matplotlib.pyplot as plt 
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1,y1,label="Label 1")
x2 = [1,2,3]
y2 = [1,2,4]
plt.plot(x2,y2,label="Label 2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Graph is showing with two line")
plt.legend()
plt.show()






