

# get the suffix of a given stock

def getSuffix(stock):
    ch = '.'
    if ch in stock:
        ind = stock.index(ch)
        return stock[ind:]
    return "usd"
    """  
    ch = '=x'
    if ch in stock:
        return "usd"
    return "usd"
    """


# create a list of all known suffixes

def setSuffix():
    wb = openpyxl.load_workbook("curr.xlsx")
    sheet = wb["Sheet1"]

    str = ""
    for i in range(2, sheet.max_row+1):
        try:
            country = sheet[f"A{i}"].value
            suffix = sheet[f"B{i}"].value
            str = str + f"\n'{suffix.lower()}': '{country}',"
        except AttributeError:
            continue
    with open('str.txt', 'w') as f:
        f.write(str)


# switch function the determine which currency to use for each function

def getCurr(suffix):
    switcher = {

        'usd': 'usd',
        '.ba': 'ars',
        '.ax': 'aud',
        '.vi': 'eur',
        '.br': 'eur',
        '.sa': 'brl',
        '.cn': 'cad',
        '.ne': 'cad',
        '.to': 'cad',
        '.v': 'cad',
        '.sn': 'clp',
        '.ss': 'cny',
        '.sz': 'cny',
        '.pr': 'czk',
        '.co': 'Denmark',
        '.ca': 'Egypt',
        '.tl': 'Estonia',
        '.he': 'eur',
        '.nx': 'eur',
        '.pa': 'eur',
        '.be': 'eur',
        '.bm': 'eur',
        '.du': 'eur',
        '.f': 'eur',
        '.hm': 'eur',
        '.ha': 'eur',
        '.mu': 'eur',
        '.sg': 'eur',
        '.de': 'eur',
        '.at': 'eur',
        '.hk': 'hkd',
        '.bd': 'huf',
        '.ic': 'isk',
        '.bo': 'inr',
        '.ns': 'inr',
        '.jk': 'idr',
        '.ir': 'eur',
        '.ta': 'ils',
        '.ti': 'eur',
        '.mi': 'eur',
        '.t': 'jpy',
        '.rg': 'eur',
        '.vs': 'eur',
        '.kl': 'myr',
        '.mx': 'mxn',
        '.as': 'eur',
        '.nz': 'nzd',
        '.ol': 'nok',
        '.ls': 'eur',
        '.qa': 'qr',
        '.me': 'rub',
        '.si': 'sgd',
        '.jo': 'zar',
        '.ks': 'krw',
        '.kq': 'krw',
        '.mc': 'eur',
        '.sau': 'sar',
        '.st': 'sek',
        '.sw': 'chf',
        '.two': 'twd',
        '.tw': 'twd',
        '.bk': 'thb',
        '.is': 'try',
        '.l': 'gbp',
        '.il': 'gbp',
        '.cbt': 'usd',
        '.cme': 'usd',
        '.nyb': 'usd',
        '.cmx': 'cad',
        '.nym': 'cad',
        '.cr': 'ves',
    }
    return switcher.get(suffix, "nothing")