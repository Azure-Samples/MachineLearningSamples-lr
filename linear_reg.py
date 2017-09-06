# Linear regression on one-dimensional data using a closed form solution.
# Please make sure matplotlib is included in the conda_dependencies.yml file.

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plot
fig = plot.figure()

# load data
X = []
Y = []
for line in open('data.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))
    
# turn them into numpy arrays so we can apply matrix operations
X = np.array(X)
Y = np.array(Y)

# this is the common denominator
denominator = X.dot(X) - X.mean() * X.sum()

# value of a
a = (X.dot(Y) - Y.mean() * X.sum()) / denominator

# value of b
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

# Yhat is simply aX + b
Yhat = a * X + b
print ("Coefficient: {0}, intercept: {1}".format(a, b))

# Plot the data and the fitted line, then save it into a png file in the output directory.
ax = fig.gca()
ax.scatter(X, Y)
ax.plot(X, Yhat, color='magenta')
fig.savefig('./outputs/lin.png')

### compute r-squared ###
# residual error of the prediction
d1 = Y - Yhat
# intrinsic error to mean
d2 = Y - Y.mean()

# if r2 is 1 (i.e., d1 is 0), this is a perfect model with no errors.
# if r2 is 0 (i.e., d1 is the same as d2), this is a useless model as it is just the same as predicting mean.
# if r2 is less than 0 (i.e., d1 is larger that d2), you are doing worse than predicting mean!!
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print ("R-squared: {}.".format(r2))
