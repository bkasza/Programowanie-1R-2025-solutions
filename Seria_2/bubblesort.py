import sys

"link do grafiki https://miro.medium.com/1*qC2DXyBZtyG5a__Zd5AlZg.gif"

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    sys = sys.argv[1:]
    arr = list(map(int, sys))
    sorted_arr = bubble_sort(arr)
    print("Posortowana tablica:", sorted_arr)