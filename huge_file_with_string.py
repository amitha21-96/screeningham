import re
def tot_lines():
    count = 0
    with open("fname.txt","r"):
        for l in fname:
            count += 1
    print("Total number of lines:", count)

def no_lines():
    fname = open("fname.txt",'r')
    f = int(input("Enter the number of lines to be read :"))
    fname1 = open("fname1.txt", "w")
    for i in range(0,f):
        contents=fname.readline()
        c1=contents.lower()
        fname1.write(c1)
    fname1.close()

def matchings():
    count = 0
    with open("fname1.txt", "r") as f1:
        for l in f1:
            count += 1
    pattern = input("Enter a string:")
    f1 = open("fname.txt", "r")
    i=0
    while i<count:
        i = i + 1
        line = f1.readline()
        r1 = len(re.findall(pattern, line))
        print(r1,"matches found in line:",line)
        r2 = re.findall(pattern,line)
        # print(r2)

fname = open("fname.txt","r")
tot_lines()
no_lines()
matchings()





