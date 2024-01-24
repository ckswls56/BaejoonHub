def solution(jobs):

    answer = 0
    jobs.sort()

    wait = []
    work = []
    idx = 0
    for t in range(0, 1000000):
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