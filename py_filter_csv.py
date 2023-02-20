#pip install xlrd==1.2.0
#pip install openpyxl
import pandas as pd
#fname=str(input("Enter file name"))
import sys
fname=sys.argv[1]
df=pd.read_csv(fname)
df_CVE=df[df['Vulnerability Name(s)'].str.contains('CVE',na=False)]
df_hc=df_CVE[(df_CVE['Severity - cvss3']=='HIGH') | (df_CVE['Severity - cvss3']=='CRITICAL')]
df_hc.loc[:,'Vulnerability Name(s)']=df_hc.loc[:,'Vulnerability Name(s)'].str.split(' ').str[0]
df_to_save=df_hc[['Project Version','Component Name','Component Version Name','Package Path','Vulnerability Name(s)','Severity - cvss3','Upgrade Guidance - Short Term','Upgrade Guidance - Long Term']]
df_to_save.to_csv(fname[:len(fname)-4]+'_filtered.csv',index=False)

