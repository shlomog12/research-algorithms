def proportional_division_equal_number_of_items_and_players(agents, items):
    k = len(items)
    n = k    
    threshold = (k-1)/2
    graph = [n][n]
    for i in n:
        for j in n:
            if agents[i][j] >= threshold:
                graph[i][j] = 1

    ans = GFG(graph).getMatch()
    if ans:        
        return ans.map(lambda i: {i: items[i]})