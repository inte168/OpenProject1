import operator

train = [('토마스', 5), ('헨리', 8),('에드워드', 9),('에밀리', 5),('토마스', 4),('헨리', 7),('토마스', 3),('에밀리', 8),('퍼시', 5),('고든', 13)]
t_dic, t_list = {},[]
tmpTup = None
tot_rank, cur_rank = 1, 1


if __name__ == '__main__' :

    print('-----2021041047 허정윤-----')
    
    for tmpTup in train :
        tName = tmpTup[0]
        tWeight = tmpTup[1]
        if tName in t_dic:
            t_dic[tName] += tWeight
        else :
            t_dic[tName] = tWeight


    train = sorted(t_dic.items(), key = operator.itemgetter(1), reverse = True)
    print('기차 수송량 목록 ==>', train)
    print("---------------------")
    print('기차\t 총수송량\t순위')
    print('---------------------\n')

    for i in range(len(train)):
        if train[i][1] == train[i-1][1]: pass
        else : cur_rank = tot_rank
        tot_rank+=1
        print(train[i][0],'\t', train[i][1],'\t',cur_rank)
        
