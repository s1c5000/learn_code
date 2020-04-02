


def bfs(data,start):
    que = []
    visit = {}
    que.append(start)

    while que:
        print(visit.values(), '  que :', que)
        node = que.pop(0)
        if node not in visit:
            visit[node] = node
            que.extend(data[node])
    return visit.values()

def dfs(data,start):
    stack = []
    visit = {}
    stack.append(start)

    while stack:
        print(visit.values(), '    stack :', stack)
        node = stack.pop()
        if node not in visit:
            visit[node] = node
            stack.extend(reversed(data[node]))
    return visit.values()

data = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A'],
    'D' : ['B'],
    'E' : ['B','F'],
    'F' : ['E']
}
print(type(data))
print(bfs(data,'A'))
print(dfs(data,'A'))