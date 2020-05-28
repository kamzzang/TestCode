def maxlimitcalc(price, diff, market):
    maxlimit = price * 1.3

    if maxlimit < 1000:
        hogaunit = 1
    elif maxlimit < 5000:
        hogaunit = 5
    elif maxlimit < 10000:
        hogaunit = 10
    elif maxlimit < 50000:
        hogaunit = 50
    elif maxlimit < 100000 and market == "KOSPI":
        hogaunit = 100
    elif maxlimit < 500000 and market == "KOSPI":
        hogaunit = 500
    elif maxlimit >= 500000 and market == "KOSPI":
        hogaunit = 1000
    elif maxlimit >= 50000 and market == "KOSDAQ":
        hogaunit = 100

    maxlimit = int(maxlimit / hogaunit) * hogaunit + (hogaunit * diff)

    return maxlimit

if __name__ == '__main__':
    price = 100010
    market = 'KOSDAQ'

    print('상한가 :', maxlimitcalc(price, 0, market))
    print('상한가 -1호가:', maxlimitcalc(price, -1, market))
