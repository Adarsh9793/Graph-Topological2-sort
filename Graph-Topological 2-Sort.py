
from queue import Queue


adjMatrix = [[0,1,1,0] , [0,0,1,1] , [0,0,0,0] , [0,0,0,0]]

def topoSort(adjMatrix):
    
    nodes = Queue()
    inDegree = dict()

    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            if adjMatrix[i][j] == 1:
                if inDegree.get(j+1) == None:
                    inDegree[j+1] = 0
                    

                inDegree[j+1] += 1
    for i in range( len(adjMatrix)):
        if inDegree.get(i+1) == None:
            nodes.put(i+1)

    ans = []
            

    while nodes.empty() == False:
        currNode = nodes.get()
        ans.append(currNode)
        
        for i in range(len(adjMatrix)):
           if adjMatrix[currNode-1][i] == 1:
                inDegree[i+1] -= 1
                if inDegree[i+1] == 0:
                    nodes.put(i+1)

    return ans

print(topoSort(adjMatrix))