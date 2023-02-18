lst=[['sham',80],['ram',85],['don',75],['harsh',86]]
dict = dict(lst)
mrk = dict.values()
sett = sorted(set(mrk))
secondlage=sett[-2]

for ele in lst:
    if ele[1]==secondlage:
        print(ele[0])