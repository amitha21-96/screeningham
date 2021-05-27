def first_largest_element(num):
    print("sorting the list without sort function")
    for i in range(0,num+1):
        for j in range(i+1,num):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    print("After Sorting the list:",list1)
    print("First Largest Element in the  List:",max(list1))

list1 = []
num = int(input("How many elements needs to add to list:"))
for i in range(0,num):
    elem = int(input("Enter list elements:"))
    list1.append(elem)
print("List Elements:",list1)
first_largest_element(num)

