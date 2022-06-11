def sort(arr):
    low = 0
    high = len(arr)-1
    i = 0
    while(i<=high):
        if arr[i] ==0:
            arr[i],arr[low] = arr[low],arr[i]
            i+=1
            low+=1
        elif arr[i]==1:
            i+=1
        else:
            arr[i],arr[high] = arr[high],arr[i]
            high-=1

def main():
    arr = [2, 0, 2, 1, 1]
    print(str(arr) + " =sort=> ")
    sort(arr)
    print(arr)

main()