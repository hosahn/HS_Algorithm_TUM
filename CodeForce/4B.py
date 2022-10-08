# d = days
# studying time >= minTime
# studying time <= maxTime

d, sumTime = map(int, input().split())
time_list = []

max_sum = 0
min_sum = 0
for i in range(d) :
    a, b = map(int, input().split())
    time_list.append((a,b,i))
    max_sum += b
    min_sum += a
if sumTime > max_sum or sumTime < min_sum :
    print("NO")
else :
    result = []
    for i in time_list :
        result.append([i[2], i[0]])
    sumTime -= min_sum
    for i in range(len(time_list)) :
        if sumTime > 0 :
            tmp = time_list[i]
            diff = tmp[1] - tmp[0]
            if sumTime >= diff :
                result[i][1] += diff
                sumTime -= diff
            elif sumTime < diff :
                result[i][1] += sumTime
                sumTime -= sumTime
                break
    print("YES")
    for i in range(len(result)) :
        print(result[i][1], end=" ")








