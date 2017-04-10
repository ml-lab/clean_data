''' input is a list'''

def gls_skill(input):
    import pandas as pd

    skill_ori = pd.DataFrame({"id": range(len(input)),
                              "skill": input})  
    # delete skill where any letter is not belong to alphabet
    skill_delete = []               
    for i in range(len(skill_ori)): 
        if any(x.lower() not in "qwertyuiopasdfghjklzxcvbnm " for x in str(skill_ori["skill"][i])):
            skill_delete.extend([i]) 
                
    skill_ori_alp = skill_ori.drop(skill_ori.index[skill_delete]).sort_values(['skill'], ascending=[True]).reset_index() 
    
    # convert all letter to lower    
    tem = []
    for i in range(len(skill_ori_alp)):
        tem.extend([str(skill_ori_alp["skill"][i]).lower()])
    skill_ori_alp["skill_new"] = tem    
    
    df_test_0 = pd.DataFrame({"id": skill_ori_alp["index"],"skill": skill_ori_alp["skill_new"]})
    df_tem = df_test_0[df_test_0["skill"].apply(lambda x: len(str(x).split(' ')) <= 4)].reset_index()
    df_test = pd.DataFrame({"id": df_tem["id"],"skill": df_tem["skill"]})
        
    #### Find job title
    job_title = pd.read_csv('C:/Users/dang van tien/Desktop/report/Job_title_full.csv', header = None)  
    job_title.rename(columns={0: 'id', 1: 'job_title'}, inplace=True)
    
    title_new = []
    for i in range(len(job_title)):
        title_new.extend([job_title["job_title"][i].lower().strip()])
    
    job_title["title_new"] = title_new
    
    c = list(job_title['title_new'])
    d = list(df_test['skill'])
    
    job_name = []
    for i in range(len(d)):
        if d[i] in c:
            job_name.append(d[i])
        else :
            job_name.append(" ")
    
    job_title_test = []
    for i in range(len(d)):
        if "er" in d[i][len(str(d[i]))-2:]:
            job_title_test.append(d[i])
        elif "or" in d[i][len(str(d[i]))-2:]:
            job_title_test.append(d[i])
        elif "ors" in d[i][len(str(d[i]))-2:]:
            job_title_test.append(d[i])
        elif "er" in d[i][len(str(d[i]))-2:]:
            job_title_test.append(d[i])
        else:
            job_title_test.append(" ")
    
    df_test["job_title"] = job_name
    df_test["job_title_test"] = job_title_test
    
    ##### Eliminate redundant words
    df_tem = pd.read_csv('C:/Users/dang van tien/Desktop/report/ky_tu_du_thua.csv')
    
    skill = df_test["skill"]
    list_redun = list(df_tem["skill"])
    
    redundancy = []
    for i in range(len(df_test)):
        if any(x in list_redun for x in skill[i].split(" ")):
            redundancy.append(skill[i])
        else:
            redundancy.append(" ")
        
    df_test["redundancy"] = redundancy
    df_test_new = df_test.sort_values(['id'], ascending=[True]).reset_index()
    
    # get skill standard
    return df_test_new[["id","skill"]][(df_test_new["job_title"] == " ") & (df_test_new["job_title_test"] == " ") & (df_test_new["redundancy"] == " ")]







