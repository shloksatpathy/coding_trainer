import heapq
ids, names, adj = {}, [], []

def city(name):
    if name not in ids:
        ids[name] = len(names)
        names.append(name)
        adj.append([])
    return ids[name]

for _ in range(int(input())):
    a, b, w = input().split()
    u, v = city(a), city(b)
    adj[u].append((v, int(w)))
    adj[v].append((u, int(w)))

for _ in range(int(input())):
    s, t = map(city, input().split())
    dist = [float("inf")] * len(names)
    parent = [-1] * len(names)
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v], parent[v] = d + w, u
                heapq.heappush(heap, (dist[v], v))
    if dist[t] == float("inf"):
        print("No route")
        continue
    path = [t]
    while path[-1] != s:
        path.append(parent[path[-1]])
    print(f"{dist[t]}: " + " -> ".join(names[x] for x in reversed(path)))
