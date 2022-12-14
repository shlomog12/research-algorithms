def n_chose_c(c,n):
    if c > n:
        return 0
    if c == n:
        return 1
    if c == 0:
        return 9**n
    ans = 9*n_chose_c(c,n-1)
    ans += n_chose_c(c-1,n-1)
    return ans

def together(n):
    all = 10**n
    no_and_no = 8**n
    only_6 = 9**n - 8**n
    only_8 = 9**n - 8**n
    return all - no_and_no - only_6 - only_8


def at_least_once(n):
    ans = 0
    for i in range(1,n+1):
        ans+=n_chose_c(i,n)
    return ans

def sum_of_all_to_n(n):
    ans = 0
    for i in range(1,n+1):
        ans += sum_of_n(i)
    return ans



def sum_of_n(n):
    all_options = 9*10**(n-1)
    not_6_and_not_8 = 7*8**(n-1)
    together_first_is_6 = at_least_once(n-1)
    together_first_is_8 = at_least_once(n-1)
    together_first_other = 7*together(n-1)

    ans = all_options - not_6_and_not_8
    if n > 1:
        ans-= together_first_is_6 
        ans-= together_first_is_8
    if n > 2:
        ans-= together_first_other
    return ans

def get_first(num):
    return int(str(num)[0])

def len_of(num):
    return len(str(num))

def get_rest(num):
    if len_of(num) == 1:
        return 0
    return int(str(num)[1:])


def lucky_number_one_number(num):
    ans = 0
    if num >= 6:
        ans+=1
    if num >= 8:
        ans+=1
    return ans


def lucky_number(num):
    if num == 0:
        return 0
    first = get_first(num)
    n = len_of(num)
    ans = 0
    if n == 1:
        return lucky_number_one_number(num)
    start = 0
    for i in range(start,first):
        if i != 6 and i != 8:
            ans+= sum_of_all_to_n(n-1)
        else:
            ans += bli_8_by_len(n-1)
    if first == 6 or first == 8:
        ans += bli_8(get_rest(num),bed=14-first)
        return ans
    ans +=lucky_number(get_rest(num))
    return ans

        
def bli_8_by_len(n):
    return 9**n

def bli_8(num, bed=8):
    if num == 0:
        return 1
    n = len_of(num)
    ans = 0
    first = get_first(num)
    for i in range(first):
        if i != bed:
            ans += bli_8_by_len(n-1)
    if first == bed:
        return ans
    ans += bli_8(get_rest(num),bed)
    return ans


def best_lucky_number(L,R):
    return lucky_number(R) - lucky_number(L-1)