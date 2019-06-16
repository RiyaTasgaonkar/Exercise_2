#bubble sort
def bubble_sort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print('Sorted array')
    print(a)
a=[]
n=int(input("Enter no. of elements to be sorted  "))
for i in range(n):
    a.append(int(input("Enter element  ")))
print('Original array')
print(a)
bubble_sort(a,n)7