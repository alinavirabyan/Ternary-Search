arr = [1, 4, 7, 11, 12, 15, 16, 20]
target = 11

low = 0
high = len(arr) - 1

while low <= high:
    m1 = low + (high - low) // 3
    m2 = high - (high - low) // 3

    if arr[m1] == target:
        print(f"Որոնվող արժեքը՝ {target}, գտնվել է ինդեքսում՝ {m1}")
        break
    elif arr[m2] == target:
        print(f"Որոնվող արժեքը՝ {target}, գտնվել է ինդեքսում՝ {m2}")
        break
    elif target < arr[m1]:
        high = m1 - 1
    elif target > arr[m2]:
        low = m2 + 1
    else:
        low = m1 + 1
        high = m2 - 1
else:
    print("Արժեքը չի գտնվել")
