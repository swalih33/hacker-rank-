if __name__ == '__main__': 
    students=[]  
    user_size=int(input())
    for y in range(user_size):
        user_name=input()
        user_mark=float(input())
        students.append([user_name,user_mark])
        
    students.sort(key=lambda x: x[1])
    second_lowest_grade=students[1][1]
    names=[]
    for student in students:
        if student[1]==second_lowest_grade:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)
    


