f = open('large_sum.txt', 'r')
total = 0

for line in f:
    print line,
    total += int(line)

answer = str(total)
print "Total: " + answer

print "Answer: " + answer[:10]
