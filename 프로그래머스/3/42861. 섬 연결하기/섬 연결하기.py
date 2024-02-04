def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    network = set([costs[0][0]])  
    # Initialize with both vertices of the first edge
    
    while len(network) < n:
        for c in costs:
            if c[0] in network and c[1] in network:
                continue
            elif c[0] in network or c[1] in network:
                network.update([c[0], c[1]])  # Fix syntax error
                answer += c[2]
                break  
                # Break out of the inner loop after finding an edge to add to the network

    return answer
