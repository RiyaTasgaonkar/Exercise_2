#nselection sort
def selection_sort(a,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(a[j] < a[min_index]):
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]        
    print('sorted array: ')
    print(a)
n=int(input("Enter the no. if elements to be sorted:  "))
a=[]
for i in range(n):
    a.append(int(input("Enter element:  ")))
print('Unsorted array')
print(a)
selection_sort(a,n)