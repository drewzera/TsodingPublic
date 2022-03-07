def create_phone_number(n):
    res = ""
    res += "("
    for i in range(len(n)):
        if i<2:
            res += str(n[i])
            continue
        if i==2:
            res += str(n[i])
            res += ") "
            continue
        if i<5:
            res += str(n[i])
            continue
        if i==5:
            res += str(n[i])
            res += "-"
            continue
        else:
            res += str(n[i])
    return res



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

def divisors(integer):
    nums = list(range(2,integer))
    res = []
    for i in range(len(nums)):
        div = integer / nums[i]
        if div.is_integer():
            res.append(int(div))
    if res==[]:
        return str(integer) + " is prime"
    return res[::-1]
            

print(divisors(13))

def unique_in_order(iterable):
    res = []
    for i in range(len(iterable)):
        if i==0:
            res.append(iterable[i])
            continue
        if iterable[i] not in res:
            res.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            res.append(iterable[i])
    return res


print(unique_in_order('AAAABBBCCDAABBB'))

def is_valid_walk(walk):
    #any valid array has to be less than len 10
    directions = ['n','e','s','w']
    #s has to follow a n , w must follow e in order to return to origin. 
    seen = []
    if len(walk) > 10:
        return False
    for i in range(len(walk)):
        j = i + 1
        while(j <= len(walk) - 1):
            if walk[i] == 'n' and walk[j] == 's':
                walk.remove(walk[i])
                walk.remove(walk[j])
            if walk[i] == 'e' and walk[j] == 'w':
                walk.remove(walk[i])
                walk.remove(walk[j])
            if walk[i] == 'w' and walk[j] == 'e':
                walk.remove(walk[i])
                walk.remove(walk[j])
            if walk[i] == 's' and walk[j] == 'n':
                walk.remove(walk[i])
                walk.remove(walk[j])
    if walk == []:
        return True
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))