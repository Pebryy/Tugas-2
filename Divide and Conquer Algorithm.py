# Binary Search

def binary_search(arr, kiri, kanan, target):
    if kanan >= kiri:
        mid = (kiri + kanan) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, kiri, mid-1, target)
        else:
            return binary_search(arr, mid+1, kanan, target)
    else:
        return -1

data = [2,4,6,8,10,12]
hasil = binary_search(data, 0, len(data)-1, 8)

print("Index ditemukan:", hasil)