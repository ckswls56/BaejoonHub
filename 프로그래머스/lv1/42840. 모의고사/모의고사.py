def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            score[0] += 1
        if answers[i] == two[i%len(two)]:
            score[1] += 1
        if answers[i] == three[i%len(three)]:
            score[2] += 1
            
    highst_score = max(score)
    answer = []
    for i in range(len(score)) :
        if score[i] == highst_score :
            answer.append(i+1)
        
    return answer