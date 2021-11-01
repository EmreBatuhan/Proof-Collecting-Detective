# ["id","weight","time","value"]
import copy

def seperator(lst , newlist = []):
    if len(lst) == 0:
        return newlist
    newlist.append(lst[:4])
    seperator(lst[4:],newlist)
    return newlist

def printer(lst):
    if len(lst) == 0:
        return ""
    return (str(lst[0])+" ") + printer(lst[1:])

def sorter(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst[0][0]]
    leftside,rightside = [],[]
    for i in range(1,len(lst)):
        if int(lst[0][0])<int(lst[i][0]):
            rightside.append(lst[i])
        else:
            leftside.append(lst[i])
    return sorter(leftside)+[lst[0][0]]+sorter(rightside)


def output(filename,total_value,list_of_picked_ids):
    file = open(filename,"w")
    file.write(str(total_value)+"\n")
    file.write(printer(sorter(list_of_picked_ids)))
    file.close()

def not_picked_to_picked(sublist,mainlist):
    if len(sublist) == 0:
        return mainlist
    mainlist.remove(sublist[0])
    not_picked_to_picked(sublist[1:],mainlist)
    return mainlist

def sum_value(not_picked,j,i=0):
    if i == len(not_picked):
        return 0
    return int(not_picked[i][j]) + sum_value(not_picked,j,i+1)

def picker(weight,time,not_picked, i = 0 ):
    global best_not_picked ,min_value

    if weight < 0 or time < 0:
        return

    if min_value == None or sum_value(not_picked,3) < min_value:
        best_not_picked , min_value = not_picked , sum_value(not_picked,3)

    if i < len(not_picked):
        picker(weight - int(not_picked[i][1]) ,time - int(not_picked[i][2]) ,not_picked[:i] + not_picked[i+1:])

    if i+1 < len(not_picked):
        picker(weight,time,not_picked,i+1)


file = open("crime_scene.txt","r")
file = file.read().split()
max_weight,max_time = int(file[0]),int(file[1])
all_ids = seperator(file[3:])

best_not_picked , min_value = None , None
picker(max_weight,sum_value(all_ids,2),all_ids)
taken_ids = not_picked_to_picked(best_not_picked,copy.deepcopy(all_ids))
output("solution_part1.txt",sum_value(taken_ids,3),taken_ids)

best_not_picked , min_value = None , None
picker(sum_value(all_ids,1),max_time,all_ids)
taken_ids = not_picked_to_picked(best_not_picked,copy.deepcopy(all_ids))
output("solution_part2.txt",sum_value(taken_ids,3),taken_ids)

best_not_picked , min_value = None , None
picker(max_weight,max_time,all_ids)
taken_ids = not_picked_to_picked(best_not_picked,copy.deepcopy(all_ids))
output("solution_part3.txt",sum_value(taken_ids,3),taken_ids)




