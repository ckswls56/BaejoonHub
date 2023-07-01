from collections import deque

def flush_queue(queue, result):
    while queue:
        result += queue.pop()
    return result

def flush_queue_reverse(queue,result):
    while queue:
        result += queue.popleft()
    return result

string = input()

characters = list(string)
result = ''
queue = deque()
is_tag = False

for char in characters:
    if char == '<':
        result = flush_queue_reverse(queue, result)  # 이전까지의 큐 내용을 출력 문자열에 추가
        result += char
        is_tag = True
    elif char == '>':
        result += char
        is_tag = False
    elif char == ' ':
        result = flush_queue_reverse(queue, result)  # 이전까지의 큐 내용을 출력 문자열에 추가
        result += char
    else:
        if is_tag:
            result += char
        else:
            queue.appendleft(char)

result = flush_queue_reverse(queue, result)  # 큐에 남아 있는 내용을 출력 문자열에 추가

print(result)
