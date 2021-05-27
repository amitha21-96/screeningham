def nth_largest_element(num):
    for i in range(0,num+1):
        for j in range(i+1,num):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    print("Sorted list:",list1)
    m = int(input("Enter value for m largest in the list(choose a value less than n):"))
    list2=[]
    for i in range(0,m):
        large = 0
        for j in range(len(list1)):
            if list1[j]>large:
                large =list1[j]
        list1.remove(large)
        list2.append(large)
    print(m,"th largest elements of list will be:",list2)

list1=[]
num = int(input("How many elements needs to add to list:"))
for i in range(0,num):
     elem = int(input("Enter list elements:"))
     list1.append(elem)
print("Orginal List:",list1)
nth_largest_element(num)