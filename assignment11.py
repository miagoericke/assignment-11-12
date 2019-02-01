In [1]: import numpy as np

In [2]: import matplotlib

In [3]: matplotlib.use('Agg')

In [4]: import matplotlib.pyplot as plt

In [5]: import pymongo

In [6]: from pymongo import MongoClient

In [7]: x = np.linspace(0,10,11)

In [8]: y = x**2

In [9]: print(x)
[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

In [10]: print(y)
[  0.   1.   4.   9.  16.  25.  36.  49.  64.  81. 100.]

In [11]: figure, axis = plt.subplots(1, 1)

In [12]: axis.plot(x, y)
Out[12]: [<matplotlib.lines.Line2D at 0x7f53c6a1c6d8>]

In [13]: figure.savefig("x_squared.svg")

In [14]: db = MongoClient("mongodb://mongo0.scitecha.com,mongo1.scitecha.com,mongo2.mrocha.org/mrocha?replicaSet=rs0").mrocha 

In [15]: user_data = list(db.users.find({}, {"profile.TracyProgress": 1}))

In [16]: tprogress = [user["profile"]["TracyProgress"] for user in user_data]

In [17]: figure, axis = plt.subplots(1, 1)

In [18]: axis.hist(tprogress, bins=10)
Out[18]: 
(array([3., 1., 5., 7., 2., 3., 5., 3., 0., 1.]),
 array([ 3. , 11.8, 20.6, 29.4, 38.2, 47. , 55.8, 64.6, 73.4, 82.2, 91. ]),
 <a list of 10 Patch objects>)

In [19]: figure.savefig('TracyProgress_histogram.svg')
In [21]: figure.savefig('TracyProgress_histogram.svg'