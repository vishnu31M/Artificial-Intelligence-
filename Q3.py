from collections import deque
def waterjug(a, b, c):
    q = deque([((0, 0), [])])
    seen = set()
    while q:
        (x, y), path = q.popleft()
        if (x, y) in seen: continue
        seen.add((x, y))
        if x == c or y == c: return path + [(x, y)]
        nxt = [(a, y), (x, b), (0, y), (x, 0),
               (x - min(x, b - y), y + min(x, b - y)),
               (x + min(y, a - x), y - min(y, a - x))]
        for state in nxt:
            q.append((state, path + [(x, y)]))
res = waterjug(1, 3, 2)
for s in res: print(s)
