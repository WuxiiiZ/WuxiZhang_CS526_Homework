import sys

def printSubstring(string, substrings = set()):
    if len(string) == 0:
        if len(substrings) == 0:
            print("There is no substrings for this input.")
        else: 
            print(', '.join(substrings),"=>",len(substrings))
        return
    else:
        for i in range(1, len(string)+1):
            substrings.add(string[0:i])
        printSubstring(string[1: ],substrings)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must type the command in the format ", "python3 Problem2.py 'STRING'")
    else:
        stringname = sys.argv[1]
        printSubstring(stringname)
    #printSubstring('abcab') => python3 Problem2.py 'abcab'
    #printSubstring('') => python3 Problem2.py ''
    #printSubstring('abcde') => python3 Problem2.py 'abcde'
    #printSubstring('qwedsa') => python3 Problem2.py 'qwedsa'

    #submit: screenshot of the console


