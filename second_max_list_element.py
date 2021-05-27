def second_largest_element(num):
    for i in range(0,num+1):
        for j in range(i+1,num):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    print("After Sorting the list:",list1)
    print("Second Largest Element in the List:",list1[-2])

num = int(input("How many elements needs to add to list:"))
list1 = []
for i in range(0,num):
    elem = int(input("Enter list elements:"))
    list1.append(elem)
print("Original List:",list1)
second_largest_element(num)