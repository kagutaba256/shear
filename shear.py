import numpy as np
import matplotlib.pyplot as plt
points = np.linspace(0, 50, 10000)


def construct(x):
    conds1 = [0 < x <= 10, 10 < x <= 40, 40 < x <= 50]
    funcs1 = [lambda x: 0,
              lambda x: -10,
              lambda x: -15]
    conds2 = [0 < x <= 25, 25 < x <= 50]
    funcs2 = [lambda x: -5 * x,
              lambda x: -125]
    return np.piecewise(x, conds1, funcs1) + np.piecewise(x, conds2, funcs2)


results = list(map(construct, points))

plt.plot(points, results)
plt.show()
