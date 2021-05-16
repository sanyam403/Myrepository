list0 = input("enter the list: ")
list1 = list0.split(",")
list2 = list()
n = len(list1)
i=0
while(i < n):
    if int(list1[i]) > 0:
        print(str(list1[i]), end = ",")
        list2.append(int(list1[i]))
    i = i+1
print("\nOutput:",list2)
