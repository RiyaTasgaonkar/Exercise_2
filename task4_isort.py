# inserton sort
def insertion_sort(a,n):
    for i in range(1,n):
        j=i-1
        item =a[i]
        while j>=0 and a[j]>item:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=item
    print('Sorted array')
    print(a)        
        
n=int(input("Enter the no. of elements to be sorted: "))
a=[]
for i in range(n):
    a.append(int(input("Enter element: ")))
print('Unsorted array')
print(a)
insertion_sort(a,n)
