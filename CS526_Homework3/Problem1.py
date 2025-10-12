import sys

def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[-1] != str[0]:
        return False
    return isPalindrome(str[1:-1])

def checkPalindrome(file):
    num = 0
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            ans = isPalindrome(line)
            if ans == True:
                num += 1
            print(ans)
    print(num)

# example: python3 Problem1.py ./Test_1/palendrome_0.txt RETURN result of checkPalindrome("./Test_1/palendrome_0.txt")
if __name__ == '__main__':
    filename = sys.argv[1]
    checkPalindrome(filename)

    