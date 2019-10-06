def binaryfunc(arr, l, r, x):
    while l<=r:
        
        #finding the mid values
        mid = int(l+(r-l) / 2)

        #print(mid)
        #print(type(mid))
        
        #checking condition if mid value is equal to search value or not
        if(arr[mid] == x):
            return mid

        #if not and value is greater than mid value ignore left part and increase its value 
        elif arr[mid] < x:
            l = mid+1


        # if value less than mid value ignore right part and decrease right value by -1
        else: 
            r= mid-1
       
    return -1

#declaring an array
arr=[1,2,3,4,5]
r=len(arr)-1
x=2



result = binaryfunc(arr,0, r, x)
