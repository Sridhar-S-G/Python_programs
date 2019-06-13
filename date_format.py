s=input() #Provide input in format 20160302 (i.e) YYYYMMDD
year=s[0:4]
st=['01','31','21']
nd=['02','22']
rd=['03','23']
th=['04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','24','30']
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
def da(d):
    if d in st:
        return('st')
    elif d in nd:
        return('nd')
    elif d in rd:
        return('rd')
    elif d in th:
        return('th')
month=mon(s[4:6])
sub=da(s[6:8])
day=s[6:8]
if day[0]=='0':
    day=day[1]
print("%s, %s%s of %s"%(year,day,sub,month))
#output will be in the format "2016, 2nd of March"
