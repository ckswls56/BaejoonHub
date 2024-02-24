def get_total_min(a):
    h, m = a.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    answer = 0
    book_time.sort()
    
    while book_time:
        before_e = -10
        new_room = []
        for slot in book_time:
            s, e = slot
            if get_total_min(s) - before_e >= 10:
                before_e = get_total_min(e)
            else:
                new_room.append(slot)
        
        answer += 1
        book_time = new_room
            
    return answer
