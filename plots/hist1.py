import matplotlib.pyplot as plt
   
size = [593.432,834.116,1058.062,1278.528,1548.283]
time = [247.289,358.011,376.159,558.233,609.948]

#size = [1,2,3,4,5]
#time = [1,2,3,4,5]


New_Colors = ['green','blue','purple','brown','teal']

plt.bar(time, size, color=New_Colors, width = 10)
plt.title('Insert Time vs Size')
plt.xlabel('File Size in Kilo Bytes')
plt.ylabel('Time in s')

plt.grid(True)

plt.show()