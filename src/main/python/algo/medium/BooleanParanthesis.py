def find_rec(s, left, right, is_true=True):
    if left > right: return 0
    if left == right:
        if is_true:
            return 1 if s[right] == 'T' else 0
        else:
            return 1 if s[right] == 'F' else 0
    result = 0
    for k in range(left + 1, right, 2):
        ltc = find_rec(s, left, k - 1, True)
        rtc = find_rec(s, k + 1, right, True)

        lfc = find_rec(s, left, k - 1, False)
        rfc = find_rec(s, k + 1, right, False)

        if is_true:
            if s[k] == '&':
                result += ltc * rtc
            elif s[k] == '|':
                result += (ltc * rtc) + (ltc * rfc) + (lfc * rtc)
            elif s[k] == '^':
                result += (ltc * rfc) + (lfc * rtc)
        else:
            if s[k] == '&':
                result += (ltc * rfc) + (lfc * rtc) + (lfc * rfc)
            elif s[k] == '|':
                result += (lfc * rfc)
            elif s[k] == '^':
                result += (lfc * rfc) + (ltc * rtc)
    return result


def find_rec_mem(s, left, right, is_true=True):
    if left > right: return 0
    if left == right:
        if is_true:
            return 1 if s[right] == 'T' else 0
        else:
            return 1 if s[right] == 'F' else 0
    result = 0
    for k in range(left + 1, right, 2):
        ltc = find_rec_mem(s, left, k - 1, True)
        rtc = find_rec_mem(s, k + 1, right, True)

        lfc = find_rec_mem(s, left, k - 1, False)
        rfc = find_rec_mem(s, k + 1, right, False)

        if is_true:
            if s[k] == '&':
                result += ltc * rtc
            elif s[k] == '|':
                result += (ltc * rtc) + (ltc * rfc) + (lfc * rtc)
            elif s[k] == '^':
                result += (ltc * rfc) + (lfc * rtc)
        else:
            if s[k] == '&':
                result += (ltc * rfc) + (lfc * rtc) + (lfc * rfc)
            elif s[k] == '|':
                result += (lfc * rfc)
            elif s[k] == '^':
                result += (lfc * rfc) + (ltc * rtc)
    return result


def find_wrap(s):
    return find_rec(s, 1, len(s) - 1)


def find_mem_wrap(s):
    l = len(s)
    dp = [[[-1 for _ in range(l)] for _ in range(l)] for _ in range(2)]
    return find_rec_mem(s, 0, l - 1, True, dp)


s = "T|T&F^T"

print(find_wrap(s))
