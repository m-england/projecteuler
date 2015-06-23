a = 1
b = 1
c = 0
index = 1
goal_digs = 1000

while (len(str(a)) < goal_digs):
    c = a + b
    a = b
    b = c
    index += 1

print "Index of the first term with %s digits is %s" % (goal_digs, index)

