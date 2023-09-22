def solution(strings, n):
    def sort(s):
        return (s[n],s)
    return sorted(strings,key=sort)