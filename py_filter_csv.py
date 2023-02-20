#pip install xlrd==1.2.0
#pip install openpyxl
import pandas as pd
import subprocess
#fname=str(input("Enter file name"))
import sys
from multiprocessing import Process

def spinup_docker(image_name):
    print(image_name)
    list1=image_name.split(" ")
    print(list1)
    subprocess.run(list1)

def sanitize(fname):
    df=pd.read_csv(fname)
    df_CVE=df[df['Vulnerability Name(s)'].str.contains('CVE',na=False)]
    df_hc=df_CVE[(df_CVE['Severity - cvss3']=='HIGH') | (df_CVE['Severity - cvss3']=='CRITICAL')]
    df_hc.loc[:,'Vulnerability Name(s)']=df_hc.loc[:,'Vulnerability Name(s)'].str.split(' ').str[0]
    df_to_save=df_hc[['Project Version','Component Name','Component Version Name','Package Path','Vulnerability Name(s)','Severity - cvss3','Upgrade Guidance - Short Term','Upgrade Guidance - Long Term']]
    df_to_save.to_csv(fname[:len(fname)-4]+'_filtered.csv',index=False)

fname=sys.argv[1]
sanitize(fname)

raw_name=fname.split('-')
index=-1
for i in range(0,len(raw_name)):
    if raw_name[i].__contains__('.'):
        index=i
        break
img_name=''
for i in range(1,len(raw_name)-2):
    if i==index-1:
        img_name+=raw_name[i]+':'
    elif i==len(raw_name)-3:
        img_name+=raw_name[i]
    else:
        img_name+=raw_name[i]+'-'
docker_img_name='devops-repo.isus.emc.com:8116/nautilus/'+img_name
img_alias='-'.join(raw_name[1:index])
print(index,docker_img_name,img_alias)
process = Process(target=spinup_docker , args=(("docker run --rm --name "+img_alias+" --entrypoint=/bin/sleep "+docker_img_name+" 180",)))
process.start()
subprocess.run(["sleep","120"])
with open(img_alias+"-report.csv", "a") as outfile:
        subprocess.run(["docker","exec",img_alias,"cat","/etc/os-release"],stdout=outfile)
with open(img_alias+"-report.csv", "a") as outfile:
            subprocess.run(["docker","exec",img_alias,"rpm","-qa"],stdout=outfile)
process.join()
