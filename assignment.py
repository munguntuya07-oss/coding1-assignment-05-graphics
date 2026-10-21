import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 3], [2, 4, 6], "r--")
ax.plot([1, 2, 3], [3, 2, 1], "g-")
ax.set_title("Example plot")
plt.show()

# 1. Does this code create one plotting panel (Axes object) or two?
# Explain briefly. A panel is a plotting area, not an individual x-axis or y-axis.
# Your answer:
# it will create one plotting panel because plt.sublots(1,1) will create one axes object and both lines are plotted on same panel using ax.plot()


# 2. How many data lines are drawn? What are the y-values of the red dashed line?
# Your answer:
# 2 data lines will be drawn, red dashed line has y-values 2,4 and 6 x-values 1,2 and 3, and also green solid line will be drawn