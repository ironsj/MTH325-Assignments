inf = float('inf') #setting inf for vertices that do not connect to another


def Floyd_Warshall(input):
    numV = 0 #numV is the number of vertices in the graph
    for element in input: #loop to set numV equal to number of vertices in the graph
        numV = numV + 1
    for m in range(numV): #nested loop to set all '0' values in matrix equal to inf (does not change meaning)
        for n in range(numV):
            if input[m][n] == 0:
                input[m][n] = inf
    for k in range(numV): #go through each vertex to see if it is on the path shortest path from i to j
        for i in range(numV): #go through vertex as the start vertex
            for j in range(numV): #go through each vertex as the destination from the start vertex
                input[i][j] = min(input[i][j], input[i][k] + input[k][j]) #if k is on shortest path from i to j, update list
    return input #returns original input but with shortest weighted directed path between pair of vertices


matrix = [[0, 7, 0, 5], [0, 2, 0, 0], [0, 3, 0, 4], [1, 0, 0, 0]]
#[[6,7,inf,5],[inf,2,inf,inf],[5,3,inf,4],[1,8,inf,6]]
print(Floyd_Warshall(matrix))
