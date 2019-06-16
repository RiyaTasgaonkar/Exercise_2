# quick sort
def partition(a,start,end):
    pivot=a[end]
    i= start-1
    for j in range(start,end):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[end]=a[end],a[i+1]
    return (i+1)
            


def quick_sort(a,x,y):
    if x<y:
        part=partition(a,x,y)
        quick_sort(a,x,part-1)
        quick_sort(a,part+1,y)
    

n=int(input("Enter the no. of elements to be sorted: "))
a=[]
for i in range(n):
    a.append(int(input("Enter element: ")))
print('Unsorted array')
print(a)
quick_sort(a,0,n-1)
print('Sorted array')
print(a)
