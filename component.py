import pandas as pd
import re
import sys


def match_strings(str1, str2):
    for i in range(len(str1)-3):
        for j in range(len(str2)-3):
            if str1[i:i+4] == str2[j:j+4]:
                return True
    return False


def match_string(str1, str2):
    for i in range(len(str1)-1):
        for j in range(len(str2)-1):
            if str1[i:i+2] == str2[j:j+2]:
                return True
    return False

def extract_substring(string):
    pattern = r'\d+\.\d+'
    matches = re.findall(pattern, string)
    if len(matches) >= 2:
        start = matches[0]
        new_string = string[string.index(start):]
        pattern2 = new_string.split('.')
        for i in range(len(pattern2)-1,-1,-1):
            if pattern2[i][0].isdigit():
                end = pattern2[i]
                break

        result = ''
        for j in range(i+1):
            result += pattern2[j]
            if j<i:
                result += '.'

        return result

    return None

filtered_file=sys.argv[1]
library_file=sys.argv[2]
df1 = pd.read_csv(filtered_file)
df2 = pd.read_csv(library_file)

match_dict = {}

j=0
for name in df1['Component Name']:
    match_found = False
    for i in range(len(df2)):
        if name.lower().strip() in df2.iloc[i,0].lower().strip() or df2.iloc[i,0].lower().strip() in name.lower().strip():
            if df1['Component Version Name'][j] in df2.iloc[i,0]:
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break

        if any(substring in df2.iloc[i,0].lower() for substring in name.lower().split()):
            if df1['Component Version Name'][j] in df2.iloc[i,0]:
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break

        if any(substring in name.lower().split() for substring in df2.iloc[i,0].lower()):
            if df1['Component Version Name'][j] in df2.iloc[i,0]:
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break
        
        if match_strings(name.lower().strip(), df2.iloc[i,0].lower()) and (df1['Component Version Name'][j] in df2.iloc[i,0] or (df1['Component Version Name'][j][1:] in df2.iloc[i,0] and not df1['Component Version Name'][j][0].isdigit())):
            match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
            match_found = True
            break

        if name.lower() == 'gnupg' or name.lower() == 'lz4' or name.lower() == 'vim':
            if match_string(name.lower().strip(), df2.iloc[i,0].lower()) and (df1['Component Version Name'][j] in df2.iloc[i,0] or (df1['Component Version Name'][j][1:] in df2.iloc[i,0] and not df1['Component Version Name'][j][0].isdigit())):
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break

        if name.lower() == 'zlib':
            if match_strings('libz', df2.iloc[i,0].lower()) and (df1['Component Version Name'][j] in df2.iloc[i,0] or (df1['Component Version Name'][j][1:] in df2.iloc[i,0] and not df1['Component Version Name'][j][0].isdigit())):
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break

        if any(substring in df2.iloc[i,0].lower() for substring in name.lower().split('-')):
            if df1['Component Version Name'][j] in df2.iloc[i,0]:
                match_dict[(name,df1['Component Version Name'][j])] = df2.iloc[i,0]
                match_found = True
                break
    
    if not match_found:
        match_dict[name] = None
    j = j+1
df1['Full Component Name'] = df1.apply(lambda row: match_dict.get((row['Component Name'], row['Component Version Name']), None), axis = 1)

df1['Full Component Name'] = df1.groupby('Component Name')['Full Component Name'].transform(lambda x: x.ffill().bfill())

df1['Full Component Name'] = df1['Full Component Name'].astype(str) 
df1['Filtered'] = df1['Full Component Name'].apply(extract_substring)
##df1['Filtered'] = df1['Full Component Name'].str.extract(r'(\d+\.\d+\.\d+-\d+.\d+.\d+.\d+.\d+)')


df1.to_csv("task1.csv", index = False)

