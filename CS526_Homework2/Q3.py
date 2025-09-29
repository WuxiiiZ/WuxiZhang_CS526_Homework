# Inplement this function
def doIt(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return doIt(n-1) + doIt(n-2) - doIt(n-3)

# Output
print(doIt(1))  # print 1
print(doIt(3))  # print 2
print(doIt(6))  # print 4