def solution(wallpaper):
    answer = []
    
    top_left,bottom_right = [len(wallpaper),len(wallpaper[-1])],[0,0]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                top_left = [min(top_left[0],i),min(top_left[1],j)]
                bottom_right = [max(bottom_right[0],i),max(bottom_right[1],j)]
                
    
    answer.append(top_left[0])
    answer.append(top_left[1])
    answer.append(bottom_right[0]+1)
    answer.append(bottom_right[1]+1)
    
                
    return answer