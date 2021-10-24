# https://www.geeksforgeeks.org/changing-one-clock-time-time-minimum-number-operations/

def solve(org, new, count=0):
    org = [int(i) for i in org.split(":")]
    new = [int(i) for i in new.split(":")]

    if len(org) != len(new): return None
    for i in range(3):
        dif = max(org[i], new[i]) - min(org[i], new[i])
        if i == 0:
            if dif > 12: dif = 24 - dif
        else:
            if dif > 30: dif = 60 - dif
        count += dif
    return count


org_time = "10:10:10"
new_time = "05:02:58"

org_time = "13:12:21"
new_time = "11:10:18"

org_time = "10:05:04"
new_time = "02:34:12"

print(solve(org_time, new_time))
