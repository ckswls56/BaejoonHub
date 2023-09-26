def solution(k, score):
    answer = []
    honor = []
    for i in score:
        honor.append(i)
        honor.sort()
  
        if len(honor)>k:
            del(honor[0])
        answer.append(honor[0])
    return answer