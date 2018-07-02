#!/usr/bin/env python

import matplotlib.pyplot as plt
labels = ["< 5 years","5 to 10 years", "> 10 years"]
data=[6,16,2,5,8,6,2,10,10,5,12,10,10,8,6,6,6,3,6,9,20,5,10,10,8,3,10,4,20,6,11,14,2,1,5,10,7,7,1,10]
print(len(data))
less_than_five= len(list(filter(lambda x: x<5, data)))
between_five_and_ten= len(list(filter(lambda x: x>=5 and x <10, data)))
larger_than_ten= len(list(filter(lambda x: x>=10, data)))
print(less_than_five, between_five_and_ten, larger_than_ten)

sizes=[less_than_five, between_five_and_ten, larger_than_ten]

explode=[0, 0.1, 0]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()