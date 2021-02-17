import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = size = ['593.432','834.116','1058.062','1278.528','1548.283']
a = [0.78, 1.53, 2.99, 3.73, 5.09]
b = [3.52, 5.65, 9.10, 13.29, 30.19]
c = [0.83, 2.14, 2.97, 5.23, 5.45]
d = [11.10, 22.30, 38.56, 48.44, 64.98]

x = np.arange(len(labels))  # the label locations
width = 0.10  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/2, a, width, label='a')
rects2 = ax.bar(x - width/2, b, width, label='b')
rects3 = ax.bar(x + width/2, c, width, label='c')
rects4 = ax.bar(x + 3*width/2, d, width, label='d')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time in s')
ax.set_xlabel('Size in kB')
ax.set_title('Insert time vs Size')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

#fig.tight_layout()
fig.set_size_inches(18.5, 10.5, forward=True)

plt.savefig('hist2.png', bbox_inches='tight')
plt.show()