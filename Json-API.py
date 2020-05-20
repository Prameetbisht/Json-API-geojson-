import urllib.request, urllib.parse, urllib.error, urllib.response
import re

#Extracting Digits and Summing them
hand = open(r"C:\Users\mypra\PycharmProjects\pyproject\dumps\regex_sum_404889.txt")
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))