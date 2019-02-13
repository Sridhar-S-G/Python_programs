s=input()
year=s[0:4]
day=s[6:8]
def mon(m):
    if m=='01':
        return('January')
    elif m=='02':
        return('February')
    elif m=='03':
        return ('March')
    elif m=='04':
        return('April')
    elif m=='05':
        return('May')
    elif m=='06':
        return('June')
    elif m=='07':
        return('July')
    elif m=='08':
        return('August')
    elif m=='09':
        return('September')
    elif m=='10':
        return('October')
    elif m=='11':
        return('November')
    elif m=='12':
        return('December') 
month=mon(s[4:6])
print(year,month,day)
