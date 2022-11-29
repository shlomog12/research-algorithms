# Python program to find
# maximal Bipartite matching.
 
class GFG:
    def __init__(self,graph):
         
        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])


        
 
    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, seen):
 
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:
                 
                # Mark v as visited
                seen[v] = True
 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if self.matchR[v] == -1 or self.bpm(self.matchR[v], seen):
                    self.matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching
    def getMatch(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        self.matchR = [-1] * self.jobs
         
        # Count of jobs assigned to applicants
        count = 0
        for i in range(self.ppl):
             
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
             
            # Find if the applicant 'u' can get a job
            if self.bpm(i, seen):
                count += 1
        if count == self.jobs:
            return self.matchR    
        return False



        
 

def proportional_division(items, preferences):
    k = len(items)
    n = k
    threshold = (k-1)/2
    graph = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if preferences[i][j] >= threshold:
                graph[i][j] = 1
    ans = GFG(graph).getMatch()
    # print(ans)
    if ans:
        return list(map(lambda x: items[x],ans))
    else:
        return 'not exists match'


preferences = [[0,1,2,3],
               [2,0,1,3],
               [2,0,1,3],
               [3,2,1,0]]
preferences2 = [[0,1,2,3],
               [0,1,2,3],
               [0,1,2,3],
               [0,1,2,3]]

preferences3 = [[0]]              
t1 = proportional_division(['A','B','C','D'], preferences)
print(t1)
t2 = proportional_division(['A','B','C','D'], preferences2)
print(t2)
t3 = proportional_division(['A'], preferences3)
print(t3)