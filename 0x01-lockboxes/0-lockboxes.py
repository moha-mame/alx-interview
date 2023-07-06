from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False

    # Set to store the keys we have collected
    keys = set([0])

    # Queue to store the boxes we can currently open
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key not in keys and key < n:
                keys.add(key)
                queue.append(key)

    return len(keys) == n
