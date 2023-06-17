sum = 0
grade_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": 0.0
}

total = 0

for i in range(20):
    input_str = input()
    values = input_str.split()
    subject = values[0]
    credit = float(values[1])  # 두 번째 요소는 학점
    grade = values[2]  # 세 번째 요소는 학점 등급
    if(grade != 'P'):
        total += credit
    sum += credit*grade_map[grade]
    
print(sum/total)
