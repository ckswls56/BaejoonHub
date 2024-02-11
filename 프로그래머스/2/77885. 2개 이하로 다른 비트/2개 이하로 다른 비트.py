def solution(numbers):
    answer = []
    # numbers = [i for i in range(16)]
    for number in numbers:
        binary = list(bin(number)[2:])
        is_one = False
        is_process = False
        res = 0
        for i in range(len(binary)-1,-1,-1):
            if binary[i] == '0' and not is_one:
                binary[i] = '1'
                is_process = True
                break
            elif binary[i] == '0' and is_one :
                binary[i] = '1'
                binary[i+1] = '0'
                is_process = True
                break
            elif binary[i] =='1' and is_one and i>0 and binary[i-1] != '1':
                binary[i] = '0'
                binary[i-1] = '1'
                is_process = True
                break
            else :
                is_one = True
                
        if not is_process :
            binary[0] = '0'
            binary.insert(0,'1')
                
        res = int(''.join(binary),2)
        
        answer.append(res)
        
    # for i,n in enumerate(answer):
    #     print(i,n)
    
        
    return answer