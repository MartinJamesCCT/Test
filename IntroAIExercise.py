#Exercise 1
graph = {
    '1' : ['2', '3', '4', '9'],
    '2' : ['4', '8', '9'],
    '3' : ['4', '6', '5', '7'],
    '4' : ['6', '7'],
    '5' : [],
    '6' : ['8'],
    '7' : [],
    '8' : [],
    '9' : []
}
#Exercise 2
graph1 = {
    'John' : ['David', 'Dorothy'],
    'Dorothy' : ['David'],
    'David' : ['Arlene', 'Nancy'],
    'Arlene' : ['Rudy'],
    'Rudy' : [],
    'Nancy' : ['Anna', 'James', 'Larry'],
    'Anna' : ['James', 'Elisabeth', 'Linda'],
    'Elisabeth' : [],
    'James' : ['Larry', 'Linda'],
    'Linda' : ['Michael', 'Nora', 'Julia', 'Larry'],
    'Michael' : ['Nora', 'Julia'],
    'Julia' : ['Nora'],
    'Nora' : [],
    'Larry' : ['Ben', 'Carol', 'Oscar'],
    'Ben' : ['Carol', 'Oscar'],
    'Carol' : ['Oscar'],
    'Oscar' : ['Felicia'],
    'Felicia' : []
}

visited = []

queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
    
  while queue:
    print (queue)
    s = queue.pop(0) 
    print (s, end = " ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, graph1, 'John')
bfs(visited, graph, '1')

visited = set()

queue = []

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dfs(visited, graph1, 'John')

visited = set() 

dfs(visited, graph, '1')
