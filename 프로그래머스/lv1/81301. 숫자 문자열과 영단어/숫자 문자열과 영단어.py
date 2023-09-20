def solution(s):
    string = ''
    en = ['zero','one','two','three','four','five','six','seven','eight','nine']
    i = 0
    while i < len(s):
        if s[i].isdigit():
            string += s[i]
        else:
            temp = ''
            while i < len(s) and temp not in en:
                temp += s[i]
                i += 1
            i-=1
            if temp in en:
                string += str(en.index(temp))

        i += 1
    answer = int(string)
    return answer