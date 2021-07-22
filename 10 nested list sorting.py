# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
    
    list.sort(key=lambda list:list[1])
    second_low=[]
    for i in range(len(list)):
        if list[i][1]!=list[0][1]:
            second_low.append(list[i][0])
            for j in range(i+1,len(list)):
                if list[j][1]==list[i][1]:
                    second_low.append(list[j][0])
                else:
                    break
            break
        else:
            continue
    second_low.sort()
    for i in second_low:
        print(i)