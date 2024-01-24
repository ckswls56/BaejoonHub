
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
def solution(jobs):

    answer = 0
    jobs.sort()

    wait = []
    work = []
    idx = 0
    for t in range(0, 500000):
        while idx<len(jobs) and jobs[idx][0] == t:
            wait += [jobs[idx]]
            idx += 1


        if work:
            if work[0][1] == t:
                w = work.pop()
                answer += t - w[0]

        if not work:
            if wait:
                wait.sort(key=lambda x: -x[1])
                w2 = wait.pop()
                work += [[w2[0], t+w2[1]]]



    return answer//len(jobs)