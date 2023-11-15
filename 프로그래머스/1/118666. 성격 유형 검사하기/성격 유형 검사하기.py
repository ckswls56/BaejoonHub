def solution(survey, choices):
    # Initialize the map with default values
    map = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    
    # Calculate the values in the map based on survey responses and choices
    for i in range(len(survey)):
        map[survey[i][0]] += 4 - choices[i]
    
    # Form the answer string based on the calculated values
    answer = ''
    if map['R'] >= map['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if map['F'] > map['C']:
        answer += 'F'
    else:
        answer += 'C'
        
    if map['M'] > map['J']:
        answer += 'M'
    else:
        answer += 'J'
        
    if map['A'] >= map['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer
