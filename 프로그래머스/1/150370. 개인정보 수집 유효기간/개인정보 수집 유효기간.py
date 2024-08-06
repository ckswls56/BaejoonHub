def get_time(date):
    return (date[0]*12*30)+(date[1] * 30) + date[2]


def solution(today, terms, privacies):
    answer = []
    date_map = {}
    terms_map = {}
    
    for t in terms:
        key,hours = t.split()
        terms_map[key] = int(hours)
        
    today_time=get_time(list(map(int,today.split('.'))))
    
    i = 1
    
    for p in privacies:
        date,key = p.split()
        date = list(map(int,date.split('.')))
        date[1] += terms_map[key]
        
        if today_time >= get_time(list(map(int,date))):
            answer.append(i)
        
        i+=1
        
    return answer