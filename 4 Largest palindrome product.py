answer = 0

def isPalindrome(num):
    if (str(num) == str(num)[::-1]):
        return True
    else:
        return False


def isLargest(pal):
    if (pal > answer):
        return pal
    else:
        return answer

for i in range(100,1000):
    for j in range(100,1000):
        h = i * j
        if (isPalindrome(h)):
            answer = isLargest(h)

print answer
