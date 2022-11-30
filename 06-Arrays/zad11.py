def month(n):
    if n == 1:
        return 'styczen'
    elif n == 2:
        return 'luty'
    elif n == 3:
        return 'marzec'
    elif n == 4:
        return 'kwiecien'
    elif n == 5:
        return 'maj'
    elif n == 6:
        return 'czerwiec'
    elif n == 7:
        return 'lipiec'
    elif n == 8:
        return 'sierpien'
    elif n == 9:
        return 'wrzesien'
    elif n == 10:
        return 'pazdziernik'
    elif n == 11:
        return 'listopad'
    elif n == 12:
        return 'grudzien'
arr = [1,2,11,12]
for n in arr:
    print(month(n))
