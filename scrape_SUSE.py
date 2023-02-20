import requests
import pandas as pd
import sys

def check_if_affected(df_list):
    df_status=df_list[-1]
    #print(df_status.columns)
    index,status=-1,""
    for i in range(0,len(df_status)):
        if df_status.loc[i,'Product(s)'][0] == 'SUSE Linux Enterprise Server 15 SP4':
            index,status=i,df_status.loc[i,'State'][0]
            break
    return index,status
    #print(df_status['Product(s)'])
    #print(df_status.loc[46,'Product(s)'])
    #for i in range(0,len(df_status)):
     #   print(df_status.loc[i,'Product(s)'])
    #df_status_SUSE=df_status[df_status['Product(s)'].str.contains('SUSE Linux Enterprise Server 15 SP3',na=False)]
    #print(df_status_SUSE)
    #if df_status[df_status['Product(s)'].str.contains('SUSE Linux Enterprise Server 15 SP4',na=False)]:
    #    print("SUSE found")
    #else:
    #    print("SUSE not found")
    #df_status_SUSE=df_[df_SUSE['Product(s)'].str.contains('SUSE Linux Enterprise Server 15 SP4',na=False)]

def retrieve_version(df_list):
    df_release = df_list[-2]
    raw_version = ""
    for i in range(0,len(df_release)):
        if df_release.loc[i,'Product(s)'].find('SUSE Linux Enterprise Server 15 SP4') != -1:
            raw_version = df_release.loc[i,'Fixed package version(s)']
    return raw_version

#cve_name=sys.argv[1]
fname=sys.argv[1]
df=pd.read_csv(fname)
fp_list,status_list,release_version_list=[],[],[]
for cve,img_version in zip(df['Vulnerability Name(s)'],df['Full Component Name']):
    #print(cve)
    cv_url = 'https://www.suse.com/security/cve/'+cve+'.html'
    html = requests.get(cv_url).content
    try:
        df_list = pd.read_html(html)
        #print(cve)
        index,status=check_if_affected(df_list)
        #print(index,status)
        if index == -1:#SUSE Enterp... not found on advisory page
            #print("FP")
            fp_list.append("Yes")
            status_list.append("")
            release_version_list.append("")
        elif status == "Released" or status=="Affected":
            version=retrieve_version(df_list)
            #print(version)
            adv_version=""
            version_list=version.split(" ")
            version_list_ne=[e for e in version_list if e]
            for i in range(0,len(version_list_ne),3):
                    if img_version.find(version_list_ne[i]) != -1:
                        adv_version = version_list_ne[i+2]
                        break
            #print(adv_version)
            fp_list.append("")
            status_list.append(status)
            release_version_list.append(adv_version)
        else:
            fp_list.append("Yes")
            status_list.append(status)
            release_version_list.append("")
            
    except ValueError:
        fp_list.append("Yes")
        status_list.append("")
        release_version_list.append("")
        #print("No table on advisory page FP")
df["FP"]=fp_list
df["Status"]=status_list
df["Release Version"]=release_version_list
df.to_csv('task3.csv',index=False)
#cv_url = 'https://www.suse.com/security/cve/'+cve_name+'.html'
#html = requests.get(cv_url).content
#df_list = pd.read_html(html)
#print(str(len(df_list))+' tables found')
#print(df_list)
#df1=df_list[1]
#patch_content=None
#df_SUSE=df1[df1['Product(s)'].str.contains('SUSE Linux Enterprise Server 15 SP4',na=False)]
#print(df_SUSE['Fixed package version(s)'])
#for i in range(0,len(df1)):
   # print(type(df1.loc[i,'Product(s)']))
   #print(df1.loc[i,'Product(s)'].contains('SUSE Linux Enterprise Server 15 SP4'))
    #if df1.loc[i,'Product(s)'].contains('SUSE Linux Enterprise Server 15 SP4')
     #   patch_content=df1.loc([i,'Fixed package version(s)'])
#if patch_content == None:
#    print("SLES not found")
#else:
#    print(patch_content)
#print(df1.loc[3,'Fixed package version(s)'])
