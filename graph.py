import matplotlib.pyplot as pyplot

y_1 = [5.2, 5.3, 5.5, 6.0, 6.3, 7.0, 8.6, 8.3, 10.1, 10.5, 8.2, 7.0]
y_2 = [5.2, 5.5, 6.0, 6.7, 6.9, 7.7, 9.3, 9.0, 10.8, 11.2, 8.9, 7.7]
y_3 = [5.2, 5.7, 6.1, 6.8, 7.1, 7.8, 9.4, 9.1, 10.9, 11.3, 9.0, 7.8]
y_4 = [5.2, 6.0, 6.3, 7.0, 7.3, 8.0, 9.6, 9.3, 11.1, 11.5, 9.2, 8.0]


x =  []


for i in range(len(y_1)):
    x.append(i)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y_1, color='tab:blue')
ax.plot(x, y_2, color='tab:green')
ax.plot(x, y_3, color='tab:red')
ax.plot(x, y_4, color='tab:grey')

pyplot.show()