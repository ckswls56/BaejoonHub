alpha = ['A', 'E', 'I', 'O', 'U']

def solution(word):
    answer = 1
    string = alpha[0]

    while word != string:
        if len(string) < len(alpha):
            string += alpha[0]
        else:
            while string[-1] == alpha[-1]:
                string = string[:-1]
            next_alpha = alpha[alpha.index(string[-1]) + 1]
            string = string[:-1] + next_alpha

        answer += 1

    return answer