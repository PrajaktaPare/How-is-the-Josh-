def find_duplicate(arr):
    # Phase 1: find intersection point
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: find entrance to cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

# Example
arr = [1, 3, 4, 2, 2]
print(find_duplicate(arr))  # Output: 2
