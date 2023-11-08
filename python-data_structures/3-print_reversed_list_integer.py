#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
a=[]

for b in my_list:
    a.insert(0,b)
for b in a:
    print("{:d}".format(b))
