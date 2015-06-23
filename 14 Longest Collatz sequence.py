sequence = []
longest_seq = []

def even(n):
    return n/2

def odd(n):
    return (3*n)+1

def isLargest(x):
    if (len(x) > len(longest_seq)):
        return x
    else:
        return longest_seq
    
for curr in range(2, 1000000):
    while (curr != 1):
        sequence.append(curr)
        if (curr % 2 == 0):
            curr = even(curr)
        else:
            curr = odd(curr)

    sequence.append(1)
    longest_seq = isLargest(sequence)
    sequence = []

print "First term:" + str(longest_seq[0])
print "Length: " + str(len(longest_seq))
