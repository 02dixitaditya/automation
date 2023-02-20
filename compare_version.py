import pandas as pd
import sys
from itertools import zip_longest

def compareVersion(v1,v2):
    #v1, v2 = list(map(int, v1.split('.'))), list(mapi(int, v2.split('.')))  
    print(v1,v2)
    v1, v2 = list(v1.split('.')), list(v2.split('.'))
    print(v1,v2)
    for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
        if rev1.isnumeric() and rev2.isnumeric():
            rev1_int,rev2_int=int(rev1),int(rev2)
            if rev1_int == rev2_int:
                continue
            return -1 if rev1_int <rev2_int else 1
        else:
            if rev1 == rev2:
                continue
            return -1 if rev1 < rev2 else 1 
    return 0

fname=sys.argv[1]
df=pd.read_csv(fname)
fp_list=[]
for img_ver,fp,fix_ver in zip(df['Filtered'],df['FP'],df['Release Version']):
    if fp == "Yes" or pd.isna(fix_ver):
        print(img_ver,"skipped")
        fp_list.append(fp)
        continue
    elif img_ver and fix_ver:
        print(img_ver,fix_ver)
        temp_img_ver='.'.join(img_ver.split('-'))
        temp_fix_ver='.'.join(fix_ver.split('-'))
        cmp=compareVersion(temp_img_ver,temp_fix_ver)
        #print(temp_img_ver,temp_fix_ver,cmp)
        #print()
        if img_ver == '1.9.9-150400.4.9.1':
            print(cmp)
        if cmp >= 0:
            fp_list.append("Yes")
        else:
            fp_list.append("No")
        #print(len(img_ver),len(fix_ver))
df["FP"]=fp_list
df.to_csv('task4.csv',index=False)
