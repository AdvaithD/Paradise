def BFS(graph, start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        while node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

# What this code does?
# Create an explored list, and a queue vairable
# while the queue is not empty, pop the first element
# make sure its not already explored
# if its not explored, append it to the explored list
# find all the neighbors
# add each neighbour to the queue
# keeps looping if the queue is not empty


test2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['B', 'C'],
    'F': ['C']
}
visitedTest = BFS(test2, 'A')

print(visitedTest)
