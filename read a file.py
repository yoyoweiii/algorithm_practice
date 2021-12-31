import os 
path=os.getcwd()
fp = open(path + "\\text.txt", "r")
print(fp.readline())
fp.close()
input()
