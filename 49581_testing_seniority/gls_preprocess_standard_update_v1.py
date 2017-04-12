########## Class include 6 function which as
 # date
 # seniority = number of experience
 # movement  =  number of movement
 # country
 # company
 # school


class gls_preprocess:

  def __init__(self,date_time,diff_date_start,diff_date_end,candidate_id,country,company,school):
       self.date_time    = date_time
       self.date_start   = diff_date_start
       self.date_end     = diff_date_end
       self.candidate_id = candidate_id
       self.country      = country
       self.company      = company
       self.school       = school


       
############################ DATE_TIME #####################
       
  def gls_date(self):
    import pandas as pd
    import re
    import time
    from gls_constants import  Date_time
    
    month_of_year = Date_time['month_of_year']
    
    day_of_month = Date_time['day_of_month']
    
    total_day_of_month = Date_time['total_day_of_month']
    
    current_year = time.strftime("%Y")
    start_year_of = int(current_year[0:2])
    end_year_of= int(current_year[2:])
    date_diff = 3
    date = ""
    date_new_1 = []
    date_new_2 = []
        
    data_ori = self.date_time
    if type(data_ori) == str:
        data = data_ori.split(sep=',')
    else:
        data = list(data_ori)
        
#### split data to ["day","month","year"]
    for i in range(len(data)):
        if str(data[i]) == "nan" || "Nan":
            tem_1 = ["wrong_date"]
        else:
            tem_1 = re.sub(r'[^a-zA-Z0-9]', ' ',data[i]).lower().split(" ")
#### standardize data
    # Length of data == 3 after split (mm-dd-yyyy)
        if len(tem_1) == 3:     
            if any(c.isalpha() for c in str(data[i])):      # Data contains number and string
                if all(re.sub('[^a-zA-Z]+', '', str(data[i])).lower() != x for x in month_of_year.keys()):
                    date_1 = "wrong_date"
                    date = [date_1,""]
                else:
                    if re.sub('[^a-zA-Z]+', '', str(data[i])).lower() == tem_1[1]:  # Case 1: number/string/number
                        if len(tem_1[0]) == 4\
                            and any(tem_1[2] == y for y in day_of_month.keys()):       # Case 1.1('yyyy-mm-dd', ex: 2014 mar 02)
                            date_1 = str(day_of_month[tem_1[2]])\
                                     + "-"\
                                     + str(month_of_year[tem_1[1]])\
                                     + "-"\
                                     + str(tem_1[0])
                            date = [date_1,""]
                            
                        elif len(tem_1[2]) == 4\
                            and any(tem_1[0] == y for y in day_of_month.keys()):       # Case 1.2('dd-mm-yyyy', ex: 8 mar 2002)
                            date_1 = str(day_of_month[tem_1[0]])\
                                     + "-" +\
                                     str(month_of_year[tem_1[1]])\
                                     + "-" +\
                                     str(tem_1[2])
                            date = [date_1,""]
                            
                        elif len(tem_1[0]) <= 2\
                            and any(tem_1[0] == y_1 for y_1 in day_of_month.keys()):   # Case 1.3('dd-mm-yy', ex: 08 mar 02)
                            if int(tem_1[2]) > end_year_of + date_diff:                    # if tem_1[2] = 02 ==> year = 2002 (not 1902) 
                                date_1 = str(day_of_month[tem_1[0]])\
                                         + "-"\
                                         + str(month_of_year[tem_1[1]])\
                                         + "-" + str(start_year_of - 1)\
                                         + str(tem_1[2])
                                date = [date_1,""]
                            else:                                                          # If tem_1[2] = 68 ==> year: 1968 (not 2068)
                                date_1 = str(day_of_month[tem_1[0]])\
                                         + "-" +\
                                         str(month_of_year[tem_1[1]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[2])
                                date = [date_1,""]
                                
                        else:
                            date_1 = "wrong_date"
                            date = [date_1,""]
                            
                    elif re.sub('[^a-zA-Z]+', '', str(data[i])).lower() == tem_1[0]:  # Case 2: string/number/number
                        if len(tem_1[1]) == 4\
                            and any(tem_1[2] == y for y in day_of_month.keys()):          # Case 2.1('mm-yyyy-dd', ex: mar 2014 02)
                            date_1 = str(day_of_month[tem_1[2]])\
                                     + "-"\
                                     + str(month_of_year[tem_1[0]])\
                                     + "-"\
                                     + str(tem_1[1])
                            date = [date_1,""]
                            
                        elif len(tem_1[2]) == 4\
                            and any(tem_1[1] == y for y in day_of_month.keys()):          # Case 2.2('mm-dd-yyyy', ex: mar 02 2014)
                            date_1 = str(day_of_month[tem_1[1]])\
                                     + "-"\
                                     + str(month_of_year[tem_1[0]])\
                                     + "-"\
                                     + str(tem_1[2])
                            date = [date_1,""]
                            
                        elif len(tem_1[1]) <= 2\
                            and any(tem_1[1] == y_1 for y_1 in day_of_month.keys()):      # Case 2.3('mm-dd-yy', ex: mar 02 14)
                            if int(tem_1[2]) > end_year_of + date_diff:                       # Year: 1968 (not 2068)  
                                date_1 = str(day_of_month[tem_1[1]])\
                                         + "-"\
                                         + str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of - 1)\
                                         + str(tem_1[2])
                                date = [date_1,""]
                            else:                                                             # Year: 2002 (not 1902)
                                date_1 = str(day_of_month[tem_1[1]])\
                                         + "-"\
                                         + str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[2])
                                date = [date_1,""]
                                
                        else:
                            date_1 = "wrong_date"
                            date = [date_1,""]
                            
                    elif re.sub('[^a-zA-Z]+', '', str(data[i])).lower() == tem_1[2]:   # Case 3: number/number/string
                        if len(tem_1[0]) == 4\
                            and any(tem_1[1] == y for y in day_of_month.keys()):           # Case 3.1('yyyy-dd-mm', ex: 2014 02 mar)
                            date_1 = str(day_of_month[tem_1[1]])\
                                     + "-"\
                                     + str(month_of_year[tem_1[2]])\
                                     + "-"\
                                     + str(tem_1[0])
                            date = [date_1,""]
                            
                        elif len(tem_1[1]) == 4\
                            and any(tem_1[0] == y for y in day_of_month.keys()):           # Case 3.2('dd-yyyy-mm', ex: 2014 02 mar)
                            date_1 = str(day_of_month[tem_1[0]])\
                                     + "-"\
                                     + str(month_of_year[tem_1[2]])\
                                     + "-"\
                                     + str(tem_1[1])
                            date = [date_1,""]
                            
                        else:
                            date_1 = "wrong_date"
                            date = [date_1,""]
                            
                    else:
                        date_1 = "wrong_date"
                        date = [date_1,""]
                        
            else:     # data contains only number                               # Case 4: number/number/number       
                if len(tem_1[0]) == 4\
                    and any(tem_1[1] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[2] == y_2 for y_2 in month_of_year.keys()):       # Case 4.1('yyyy-//-//', ex: 2014 02 02)
                    date_1 = str(day_of_month[tem_1[2]])\
                             + "-"\
                             + str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[0])
                    date_2 = str(day_of_month[tem_1[1]])\
                             + "-"\
                             + str(month_of_year[tem_1[2]])\
                             + "-"\
                             + str(tem_1[0])
                    date = [date_1,date_2]
                    
                elif len(tem_1[0]) == 4\
                    and any(tem_1[1] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[2] == y_2 for y_2 in day_of_month.keys()):        # Case 4.2('yyyy-mm-dd', ex: 2014 02 22)
                    date_1 = str(day_of_month[tem_1[2]])\
                             + "-"\
                             + str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[0])
                    date = [date_1,""]
                    
                elif len(tem_1[0]) == 4\
                    and any(tem_1[2] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[1] == y_2 for y_2 in day_of_month.keys()):        # case 4.3('yyyy-dd-mm', ex: 2014 22 12)
                    date_1 = str(day_of_month[tem_1[1]])\
                             + "-"\
                             + str(month_of_year[tem_1[2]])\
                             + "-"\
                             + str(tem_1[0])
                    date = [date_1,""]
    
                elif len(tem_1[2]) == 4\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[1] == y_2 for y_2 in month_of_year.keys()):       # case 4.4('//-//-yyyy', ex: 02 02 2012)
                    date_1 = str(day_of_month[tem_1[0]])\
                             + "-"\
                             + str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[2])
                    date_2 = str(day_of_month[tem_1[1]])\
                             + "-"\
                             + str(month_of_year[tem_1[0]])\
                             + "-"\
                             + str(tem_1[2])
                    date = [date_1,date_2]
                    
                elif len(tem_1[2]) == 4\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[1] == y_2 for y_2 in day_of_month.keys()):        # Case 4.5('mm-dd-yyyy', ex: 02 22 2012)
                    date_1 = str(day_of_month[tem_1[1]])\
                             + "-"\
                             + str(month_of_year[tem_1[0]])\
                             + "-"\
                             + str(tem_1[2])
                    date = [date_1,""]
                    
                elif len(tem_1[2]) == 4\
                    and any(tem_1[1] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[0] == y_2 for y_2 in day_of_month.keys()):        # Case 4.6('dd-mm-yyyy', ex: 22 02 2012)
                    date_1 = str(day_of_month[tem_1[0]])\
                             + "-"\
                             + str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[2])
                    date = [date_1,""]
                    
                elif len(tem_1[0]) <= 2\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[1] == y_2 for y_2 in month_of_year.keys()):       # Case 4.7('dd-mm-yy', ex: 02 02 12)
                    if int(tem_1[2]) > end_year_of + date_diff:                         # Year: 1992 (not 2002)                
                        date_1 = str(day_of_month[tem_1[1]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[2])
                        date_2 = str(day_of_month[tem_1[0]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[1]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[2])
                        date = [date_1,date_2]
                        
                    else:                                                               # Year: 2002 (not 1902)
                        date_1 = str(day_of_month[tem_1[1]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[2])
                        date_2 = str(day_of_month[tem_1[0]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[1]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[2])
                        date = [date_1,date_2]
                        
                elif len(tem_1[0]) <= 2\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[1] == y_2 for y_2 in day_of_month.keys()):        # Case 4.8('mm-dd-yy', ex: 02 22 12)
                    if int(tem_1[2]) > end_year_of + date_diff:                         # Year: 1992 (not 2002)
                        date_1 = str(day_of_month[tem_1[1]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[2])
                        date = [date_1,""]
                    else:                                                               # Year: 2002 (not 1902)
                        date_1 = str(day_of_month[tem_1[1]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[2])
                        date = [date_1,""]
                elif len(tem_1[0]) <= 2\
                    and any(tem_1[1] == y_1 for y_1 in month_of_year.keys())\
                    and any(tem_1[0] == y_2 for y_2 in day_of_month.keys()):        # Case 4.9('dd-mm-yy', ex: 02 22 12)
                    if int(tem_1[2]) > end_year_of + date_diff:                         # Year: 1992 (not 2002)
                        date_1 = str(day_of_month[tem_1[0]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[1]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[2])
                        date = [date_1,""]
                        
                    else:                                                               # Year: 2002 (not 1902)
                        date_1 = str(day_of_month[tem_1[0]])\
                                 + "-"\
                                 + str(month_of_year[tem_1[1]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[2])
                        date = [date_1,""]
                        
                else:
                    date_1 = "wrong_date"
                    date = [date_1,""]
    
        elif len(tem_1) == 2:      # Length of data == 2 after split (mm-dd-yyyy)
            if any(c.isalpha() for c in str(data[i])):      # Data contains number and string
                if all(re.sub('[^a-zA-Z]+', '', str(data[i])).lower() != x for x in month_of_year.keys()):
                    date_1 = "wrong_date"
                    date = [date_1,""]
                else:
                    if re.sub('[^a-zA-Z]+', '', str(data[i])).lower() == tem_1[1]:    # Case 5: number/string
                        if len(tem_1[0]) == 4:                                            # Case 5.1('yyyy-mm', ex: 2002 mar)
                            date_1 = "01-"\
                                     + str(month_of_year[tem_1[1]])\
                                     + "-"\
                                     + str(tem_1[0])
                            date_2 = str(month_of_year[tem_1[1]])\
                                     + "-"\
                                     + str(tem_1[0])
                            date = [date_1,""]
                            
                        elif len(tem_1[0]) == 2:                                          # Case 5.2('yy-mm', ex: 02 mar)
                            if int(tem_1[0]) > end_year_of + date_diff:                       # Year: 1992 (not 2002)
                                date_1 = "01-"\
                                         + str(month_of_year[tem_1[1]])\
                                         + "-"\
                                         + str(start_year_of - 1)\
                                         + str(tem_1[0])
                                date_2 = str(month_of_year[tem_1[1]])\
                                         + "-"\
                                         + str(start_year_of - 1)\
                                         + str(tem_1[0])
                                date = [date_1,date_2]
                            else:                                                             #Year: 2002 (not 1902)
                                date_1 = "01-"\
                                         + str(month_of_year[tem_1[1]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[0])
                                date_2 = str(month_of_year[tem_1[1]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[0])
                                date = [date_1,date_2]
                                
                        else:
                            date_1 = "wrong_date"
                            date = [date_1,""]
                            
                    elif re.sub('[^a-zA-Z]+', '', str(data[i])).lower() == tem_1[0]:    # Case 6: string/number
                        if len(tem_1[1]) == 4:                                              # Case 6.1('mm-yyyy', ex: mar 2002)
                            date_1 = "01-"\
                                     + str(month_of_year[tem_1[0]])\
                                     + "-"\
                                     + str(tem_1[1])
                            date_2 = str(month_of_year[tem_1[0]])\
                                     + "-"\
                                     + str(tem_1[1])
                            date = [date_1,""]
                            
                        elif len(tem_1[1]) == 2:                                             # Case 6.2('mm-yy', ex: mar 02)
                            if int(tem_1[1]) > end_year_of + date_diff:                          # Year: 1992 (not 2002)
                                date_1 = "01-"\
                                         + str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of - 1)\
                                         + str(tem_1[1])
                                date_2 = str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of - 1)\
                                         + str(tem_1[1])
                                date = [date_1,date_2]
                            else:                                                                # Year: 2002 (not 1902)
                                date_1 = "01-"\
                                         + str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[1])
                                date_2 = str(month_of_year[tem_1[0]])\
                                         + "-"\
                                         + str(start_year_of)\
                                         + str(tem_1[1])
                                date = [date_1,date_2]
                                
                        else:
                            date_1 = "wrong_date"
                            date = [date_1,""]
                            
                    else:
                        date_1 = "wrong_date"
                        date = [date_1,""]
                        
            else:  
            # Data contains only number                      
            # Case 7: number/number
                if len(tem_1[0]) == 4\
                    and any(tem_1[1] == y_1 for y_1 in month_of_year.keys()):   # Case 7.1('yyyy-mm', ex: 2002 02)
                    date_1 = "01-"\
                             + str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[0])
                    date_2 = str(month_of_year[tem_1[1]])\
                             + "-"\
                             + str(tem_1[0])
                    date = [date_1,date_2]
                    
                elif len(tem_1[1]) == 4\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys()):   # Case 7.2('mm-yyyy', ex: 02 2002)
                    date_1 = "01-"\
                             + str(month_of_year[tem_1[0]])\
                             + "-"\
                             + str(tem_1[1])
                    date_2 = str(month_of_year[tem_1[0]])\
                             + "-"\
                             + str(tem_1[1])
                    date = [date_1,date_2]
                    
                elif len(tem_1[0]) <= 2\
                    and any(tem_1[0] == y_1 for y_1 in month_of_year.keys()):   # Case 7.3('mm-yy', ex: 02 02)
                    if int(tem_1[1]) > end_year_of + date_diff:                     # Year: 1992 (not 2002)
                        date_1 = "01-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[1])
                        date_2 = str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of - 1)\
                                 + str(tem_1[1])
                        date = [date_1,date_2]
                    else:                                                           # Year: 2002 (not 1902)
                        date_1 = "01-"\
                                 + str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[1])
                        date_2 = str(month_of_year[tem_1[0]])\
                                 + "-"\
                                 + str(start_year_of)\
                                 + str(tem_1[1])
                        date = [date_1,date_2]
                        
                else:
                    date_1 = "wrong_date"
                    date = [date_1,""]
        
        elif tem_1[0] == "current" or tem_1[0] == "present" :   # Current date
            date_1 = time.strftime("%d-%m-%Y")
            date_2 = ""
            date = [date_1, date_2]
                    
        elif len(tem_1) == 1:      # Length of data == 1 after split (mm-dd-yyyy)
            if any(c.isalpha() for c in str(data[i])): 
                    date_1 = "wrong_date"
                    date = [date_1,""]
            else:
                if len(tem_1[0]) == 4:   # Case 8: number
                    date_1 = "01-01-" + str(tem_1[0])
                    date_2 = str(tem_1[0])
                    date = [date_1,date_2]
                else:
                    date_1 = "wrong_date"
                    date = [date_1,""]
        else:
            date_1 = "wrong_date"
            date = [date_1,""]
        
        # Check if date exist.
        if date[0] != "wrong_date":
            test = date[0].split("-")    
            if int(test[2]) < int(current_year) + 4:
                if int(test[2]) % 400 == 0\
                    or (int(test[2]) % 4 == 0 and int(test[2]) % 100 != 0) and test[1] == "02":
                    if int(test[0]) < 30:
                        date_new_1.extend([date[0]])
                        date_new_2.extend([date[1]])
                    else:
                        date_new_1.extend(["wrong_date"])
                        date_new_2.extend([""])
                else:
                    if int(test[0]) <= int(total_day_of_month[test[1]]):
                        date_new_1.extend([date[0]])
                        date_new_2.extend([date[1]])
                    else:
                        date_new_1.extend(["wrong_date"])
                        date_new_2.extend([""])
            else:
                date_new_1.extend(["wrong_date"])
                date_new_2.extend([""])
                
        else:
            date_new_1.extend(["wrong_date"])
            date_new_2.extend([""])
    # Return result
    return pd.DataFrame({"date": data,
                         "date_modify_1": date_new_1,
                         "date_modify_2": date_new_2})

########################### SENIORITY ###############

  def gls_seniority(self):
       import pandas as pd
       from datetime import datetime

       date_start = list(self.date_start)
       date_end = list(self.date_end )
       diff_date_month = []
     
       for i in range(len(date_start)):
         if date_start[i] != "wrong_date" and date_end[i] != "wrong_date" and date_start[i] != "" and date_end[i] != "":
             date_start_1 = datetime.strptime(date_start[i] , '%d-%m-%Y')
             date_end_1 = datetime.strptime(date_end[i], '%d-%m-%Y')
             diff = int(round((date_end_1 - date_start_1).days/float(30)))     
             if date_start_1 <= date_end_1:
                 diff_date_month.append(diff)
             else:
                 diff_date_month.append(0)
         else:
            diff_date_month.append(0)
            
       return pd.DataFrame({"date_start" : date_start,
                          "date_end" : date_end,
                          "diff_date_(month)" : diff_date_month })

                         
######################### NUMBER OF MOVEMENT #################
                          
  def gls_movement(self):
    import pandas as pd
    from collections import Counter
    data_count = Counter(list(self.candidate_id))

    return pd.DataFrame({"Candidate_id": data_count.keys(),
                         "Movement": data_count.values()})                          
########################## COUNTRY NAME ################
                          
  def gls_country(self):
      import pandas as pd
      from gls_constants import Country_name

      tem = list(self.country)
      Acronym_name_2W = Country_name["Acronym_name_2W"]
      Acronym_name_3W = Country_name["Acronym_name_3W"]
      Country_fullname = Country_name["Country_fullname"]
      
      tem_1 = []            
      for i in range(len(tem)): tem_1.append(str(tem[i]).lower().split())
        
      tem_2 = []
      Standard_name = []
      Error_name =[]
      for i in range(len(tem_1)) : 
            if len(tem_1[i]) == 1 :
                for j in range(len(Acronym_name_2W)):
                    if tem_1[i][0] == Acronym_name_2W[j].lower() :
                             Standard_name.append(Country_fullname[j])
                             Error_name.append(" ")
                             tem_2.append(str(tem_1[i]))  
                             break
                    elif tem_1[i][0] == Acronym_name_3W[j].lower():
                             Standard_name.append(Country_fullname[j])
                             Error_name.append(" ")
                             tem_2.append(str(tem_1[i])) 
                             break
                    elif tem_1[i][0].upper() == Country_fullname[j] :
                             Standard_name.append(Country_fullname[j])
                             Error_name.append(" ")
                             tem_2.append(str(tem_1[i]))
                             break
                else :
                             Standard_name.append(" ")
                             Error_name.append(tem_1[i])
                             tem_2.append(str(tem_1[i]))
            elif len(tem_1[i]) >= 2:             
               for k in range(len(Country_fullname)):
                   if (tem_1[i][0] and tem_1[i][1]) in Country_fullname[k].lower():
                            Standard_name.append(Country_fullname[k])
                            Error_name.append(" ")
                            tem_2.append(str(tem_1[i])) 
                            break
               else :
                            Standard_name.append(" ")
                            Error_name.append(tem_1[i])
                            tem_2.append(str(tem_1[i]))
            else :
                Standard_name.append(" ")
                Error_name.append(tem_1[i])
                tem_2.append(str(tem_1[i]))
      return pd.DataFrame({"data_input" : tem_2, 
                           "error_name" : Error_name, 
                           "new_name":  Standard_name})                      

############################ COMPANY NAME ################################
                          
  def gls_company(self):
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import re
    
    # Convert data to list
    if type(self.company) == str:
        data = [self.company]
    else:
        data = list(self.company)
        
    company_name_new_1 = []
    company_name_new_2 = []
    company_name_new_3 = []
    company_name_new_4 = []
    company_name_new_5 = []
    
    # Search data on wikipedia
    for j in range(len(data)):
        r = requests.get("https://en.wikipedia.org/wiki/" + str(data[j]).strip())
        soup = BeautifulSoup(r.text, "lxml") 
        tem_1_1 = soup.find_all("caption", {"class": "fn org"})
        tem_1_2 = soup.find_all("th", {"class": "fn org"})
        
        # CASE 1: Get result from original keyword (2 format of result)
        if (len(tem_1_1)) > 0:
            company_name_tem = re.sub('<.*?>', '', str(tem_1_1[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            company_name_new_1.extend([company_name_tem])
            company_name_new_2.extend([""])
            company_name_new_3.extend([""])
            company_name_new_4.extend([""])
            company_name_new_5.extend([""])
        elif (len(tem_1_2)) > 0:
            company_name_tem = re.sub('<.*?>', '', str(tem_1_2[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            company_name_new_1.extend([company_name_tem])
            company_name_new_2.extend([""])
            company_name_new_3.extend([""])
            company_name_new_4.extend([""])        
            company_name_new_5.extend([""])
        
        # CASE 2: Can not find result from original keyword
        else: # split data by , and (
            company_name_tem = str(data[j]).replace(",(","___").replace(",","___").replace("(","___")\
                              .replace(")","").replace("-","___")
            if len(company_name_tem.split("___")) == 2:
                key_1 = company_name_tem.split("___")[0].strip()
                key_2 = company_name_tem.split("___")[1].strip()
            else:
                key_1 = company_name_tem.split("___")[0].strip()
                key_2 = ""
             
             # CASE 2.1: search the first part of the keyword after splitting
            r__2 = requests.get("https://en.wikipedia.org/wiki/" + str(key_1))
            soup__2 = BeautifulSoup(r__2.text, "lxml") 
            tem_2_1 = soup__2.find_all("caption", {"class": "fn org"})
            tem_2_2 = soup__2.find_all("th", {"class": "fn org"})
                     # Get result from new keyword
            if (len(tem_2_1)) > 0:
                company_name_tem = re.sub('<.*?>', '', str(tem_2_1[0])).replace("[","").replace("]","")\
                                  .replace("&amp;","&").strip()
                company_name_new_5.extend([company_name_tem])
            elif (len(tem_2_2)) > 0:
                company_name_tem = re.sub('<.*?>', '', str(tem_2_2[0])).replace("[","").replace("]","")\
                                  .replace("&amp;","&").strip()
                company_name_new_5.extend([company_name_tem])
            else:   # Can not find result from new key word
                company_name_new_5.extend([""])
            
            # CASE 2.2: Search by alternative link
            alternative_link =  soup.find_all("a", {"class": "external text"})
            if any("Wikipedia does not have an article with this exact name" in str(x) for x in soup.find_all("b")):
                alternative_link_new = alternative_link[0].get('href')
                r__3 = requests.get("https:" + str(alternative_link_new))
                soup__3 = BeautifulSoup(r__3.text, "lxml")
               
               # CASE 2.2.1: Search by the alternative keyword if the original keyword is wrong
                did_you_mean = soup__3.find_all("div", {"class": "searchdidyoumean"})
                if len(did_you_mean) == 1:
                    did_you_mean_link_3 = did_you_mean[0].find_all("a")
                    did_you_mean_link_new_3 = did_you_mean_link_3[0].get('href')
                    r__4 = requests.get("https://en.wikipedia.org" + str(did_you_mean_link_new_3))
                    soup__4 = BeautifulSoup(r__4.text, "lxml")
                    
                    # Get all keywords similar to original keyword or the first part of the keyword after splitting
                    did_you_mean_company_name_tem = soup__4.find_all("a")
                    did_you_mean_company_name = []
                    did_you_mean_company_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                                     for x in did_you_mean_company_name_tem])
                    did_you_mean_new = []
                    did_you_mean_new_1 = []
                    did_you_mean_new.extend([x for x in did_you_mean_company_name if\
                                             re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                             in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                             and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                             for y in ["http","listof"])])
                    did_you_mean_new_1.extend([x for x in did_you_mean_company_name if\
                                               re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                               in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                               and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                               and len(str(x)) > 10\
                                               and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                               for y in ["http","listof"])])
                   
                   # Remove keyword if it equal to similar keywords        
                    remove_mean = soup__4.find_all("i")
                    if len(remove_mean) > 0:
                        if "does not exist" in str(remove_mean[0]):
                            tem_4_1 = remove_mean[0].find_all("a")
                            remove_mean_new = re.sub('<.*?>', '', str(tem_4_1[0]))
                            
                    for i in range(len(did_you_mean_new)):
                        if re.sub('[^a-zA-Z]+','',str(remove_mean_new).replace("&amp;","&")).lower()\
                            == re.sub('[^a-zA-Z]+','',str(did_you_mean_new[i]).replace("&amp;","&")).lower():
                            del did_you_mean_new[i]
                            break
                    for i in range(len(did_you_mean_new_1)):
                        if re.sub('[^a-zA-Z]+','',str(remove_mean_new).replace("&amp;","&")).lower()\
                            == re.sub('[^a-zA-Z]+','',str(did_you_mean_new_1[i]).replace("&amp;","&")).lower():
                            del did_you_mean_new_1[i]
                            break                    
                   
                   # Find the nearest keyword to the original keyword
                    did_you_mean_name_1 = ""                    
                    if len(did_you_mean_new_1) > 0\
                        and any(re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                        == re.sub('[^a-zA-Z]+','', str(x)).lower() for x in did_you_mean_new_1):
                        for i in range(len(did_you_mean_new_1)):
                            if re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                               == re.sub('[^a-zA-Z]+','', str(did_you_mean_new_1[i])).lower():
                                did_you_mean_name_1 = did_you_mean_new_1[i]
                    elif len(did_you_mean_new_1) > 0:
                        did_you_mean_name_1 = did_you_mean_new_1[0]
                    else:
                        did_you_mean_name_1 = ""  
                    
                    # Search with the nearest keyword to find the final result
                    if len(did_you_mean_new_1) > 0:
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(did_you_mean_name_1))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2.extend([company_name_tem])
                        elif (len(tem_5_2)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2.extend([company_name_tem])     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(did_you_mean_new_1[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                company_name_new_2.extend([tem_tem])
                            else:
                                company_name_new_2.extend([""])
                        else:
                            company_name_new_2.extend([""])
                    else:
                        company_name_new_2.extend([""])
    
                    if len(did_you_mean_new) > 0 and company_name_new_2[j] == "":
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(did_you_mean_new[0]))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2[j] = company_name_tem
                        elif (len(tem_5_2)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2[j] = company_name_tem     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(did_you_mean_new[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                company_name_new_2[j] = company_name_tem
                            else:
                                company_name_new_2[j] = ""
                        else:
                            company_name_new_2[j] = ""
                        
                    company_name_new_1.extend([""])
                    company_name_new_3.extend([' / '.join(did_you_mean_new)])
                    company_name_new_4.extend([' / '.join(did_you_mean_new_1)])
               
               # CASE 2.2.1: Find all alternative keywords
                else:
                    alternative_company_name_tem = soup__3.find_all("a")
                    alternative_company_name = []
                    alternative_company_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                                    for x in alternative_company_name_tem])
                    alternative_new = []
                    alternative_new_1 = []
                    alternative_new.extend([x for x in alternative_company_name\
                                            if re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                            in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                            and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                            for y in ["http","listof"])])
                    alternative_new_1.extend([x for x in alternative_company_name\
                                              if re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                              in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                              and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                              and len(str(x)) > 10\
                                              and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                              for y in ["http","listof"])])
                   
                   # Remove keyword if it equal to alternative keywords   
                    remove_alternative = soup__3.find_all("i")
                    remove_alternative_new = ""
                    if len(remove_alternative) > 0:
                        if "does not exist" in str(remove_alternative[0]):
                            tem_4_1 = remove_alternative[0].find_all("a")
                            remove_alternative_new = re.sub('<.*?>', '', str(tem_4_1[0]))
                        
                    for i in range(len(alternative_new)):
                        if re.sub('[^a-zA-Z]+','',str(remove_alternative_new).replace("&amp;","&")).lower()\
                           == re.sub('[^a-zA-Z]+','',str(alternative_new[i]).replace("&amp;","&")).lower():
                            del alternative_new[i]
                            break
                    for i in range(len(alternative_new_1)):
                        if re.sub('[^a-zA-Z]+','',str(remove_alternative_new).replace("&amp;","&")).lower()\
                           == re.sub('[^a-zA-Z]+','',str(alternative_new_1[i]).replace("&amp;","&")).lower():
                            del alternative_new_1[i]
                            break                    
                    
                    # Find the nearest keyword to the original keyword
                    alternative_name_1 = ""                    
                    if len(alternative_new_1) > 0 and any(re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','', str(x)).lower() for x in alternative_new_1):
                        for i in range(len(alternative_new_1)):
                            if re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                               == re.sub('[^a-zA-Z]+','', str(alternative_new_1[i])).lower():
                                alternative_name_1 = alternative_new_1[i]
                    elif len(alternative_new_1) > 0:
                        alternative_name_1 = alternative_new_1[0]
                    else:
                        alternative_name_1 = ""  
                    
                    # Search with the nearest keyword to find the final result
                    if len(alternative_new_1) > 0:
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(alternative_name_1))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2.extend([company_name_tem])
                        elif (len(tem_5_2)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2.extend([company_name_tem])     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(alternative_new_1[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                company_name_new_2.extend([tem_tem])
                            else:
                                company_name_new_2.extend([""])
                        else:
                            company_name_new_2.extend([""])
                    else:
                        company_name_new_2.extend([""])
    
                    if len(alternative_new) > 0 and company_name_new_2[j] == "":
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(alternative_new[0]))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2[j] = company_name_tem
                        elif (len(tem_5_2)) > 0:
                                company_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                company_name_new_2[j] = company_name_tem     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(alternative_new[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                company_name_new_2[j] = company_name_tem
                            else:
                                company_name_new_2[j] = ""
                        else:
                            company_name_new_2[j] = ""
                                                    
                    company_name_new_1.extend([""])
                    company_name_new_3.extend([' / '.join(alternative_new)])
                    company_name_new_4.extend([' / '.join(alternative_new_1)])
            
            # Get keywords refer to ariginal keywords   
            else:
                refer_to_shool_name_tem = soup.find_all("a")
                refer_to_shool_name = []
                refer_to_shool_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                            for x in refer_to_shool_name_tem])
                refer_to_new = []
                refer_to_new_1 = []
                refer_to_new.extend([x for x in refer_to_shool_name\
                                     if re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                     in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                     and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                     for y in ["http","listof"])])
                refer_to_new_1.extend([x for x in refer_to_shool_name\
                                       if re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                       in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                       and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                       and len(str(x)) > 10\
                                       and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                       for y in ["http","listof"])])
             
             # Find the nearest keyword to the original keyword
                for i in range(len(refer_to_new)):
                    if re.sub('[^a-zA-Z]+','',str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','',str(refer_to_new[i])).lower():
                        del refer_to_new[i]
                        break
                for i in range(len(refer_to_new_1)):
                    if re.sub('[^a-zA-Z]+','',str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','',str(refer_to_new_1[i])).lower():
                        del refer_to_new_1[i]
                        break
                                                    
                company_name_new_1.extend([""])
                company_name_new_2.extend([""])
                company_name_new_3.extend([' / '.join(refer_to_new)])
                company_name_new_4.extend([' / '.join(refer_to_new_1)])
       
            # Get the best keywords if can not find the result
        if company_name_new_1[j] != "" or company_name_new_2[j] != "":
            company_name_new_2[j] = company_name_new_2[j]
        elif company_name_new_1[j] == ""\
             and company_name_new_2[j] == ""\
             and company_name_new_3[j] == ""\
             and company_name_new_4[j] == "":
            company_name_new_2[j] = company_name_new_5[j]
        elif company_name_new_1[j] == "" and company_name_new_2[j] == "":
            if any("Inc." in str(x) for x in company_name_new_3)\
               or any("Corporation" in str(y) for y in company_name_new_3):
                company_name_new_3_tem = company_name_new_3[j].split("/")
                for i in range(len(company_name_new_3_tem)):
                    if "Inc." in str(company_name_new_3_tem[i])\
                       or "Corporation" in str(company_name_new_3_tem[i]):
                        company_name_new_2[j] = company_name_new_3_tem[i].strip()
                        break
            else:
                company_name_new_4_tem = company_name_new_4[j].split("/")
                if any("Inc." in str(x) for x in company_name_new_4_tem)\
                   or any("Corporation" in str(y) for y in company_name_new_4_tem)\
                   or any("Co." in str(x) for x in company_name_new_4_tem)\
                   or any("Ltd." in str(y) for y in company_name_new_4_tem):
                    for i in range(len(company_name_new_4_tem)):
                        if "Inc." in str(company_name_new_4_tem[i])\
                           or "Corporation" in str(company_name_new_4_tem[i])\
                           or "Co." in str(company_name_new_4_tem[i])\
                           or "Ltd." in str(company_name_new_4_tem[i]):
                            company_name_new_2[j] = company_name_new_4_tem[j].strip()
                            break
                else:
                    company_name_new_2[j] = company_name_new_5[j]
        else:
            company_name_new_2[j] = company_name_new_5[j]
        
        # Searching to find the result by the best keyword
        r__6 = requests.get("https://en.wikipedia.org/wiki/" + str(company_name_new_2[j]).strip())
        soup__6 = BeautifulSoup(r__6.text, "lxml") 
        tem_6_1 = soup__6.find_all("caption", {"class": "fn org"})
        tem_6_2 = soup__6.find_all("th", {"class": "fn org"})
        
        if (len(tem_6_1)) > 0:
            company_name_tem = re.sub('<.*?>', '', str(tem_6_1[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            company_name_new_2[j] = company_name_tem
        elif (len(tem_6_2)) > 0:
            company_name_tem = re.sub('<.*?>', '', str(tem_1_2[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            company_name_new_2[j] = company_name_tem
        else:
            company_name_new_2[j] = company_name_new_2[j]
    
    return pd.DataFrame({'company_name_a_ori': data,
                       "company_name_new_1": company_name_new_1,
                       "company_name_new_2": company_name_new_2,
                       "company_name_new_3": company_name_new_3,
                       "company_name_new_4": company_name_new_4,
                       "company_name_new_5": company_name_new_5})                          

############################## SCHOOL NAME #################################

  def gls_school(self):
      
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import re
    
    # Convert data to list
    if type(self.school) == str:
        data = [self.school]
    else:
        data = list(self.school)
        
    school_name_new_1 = []
    school_name_new_2 = []
    school_name_new_3 = []
    school_name_new_4 = []
    school_name_new_5 = []

    # Search data on wikipedia
    for j in range(len(data)):
        r = requests.get("https://en.wikipedia.org/wiki/" + str(data[j]).strip())
        soup = BeautifulSoup(r.text, "lxml") 
        tem_1_1 = soup.find_all("caption", {"class": "fn org"})
        tem_1_2 = soup.find_all("th", {"class": "fn org"})
        
        # CASE 1: Get result from original keyword (2 format of result)
        if (len(tem_1_1)) > 0:
            school_name_tem = re.sub('<.*?>', '', str(tem_1_1[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            school_name_new_1.extend([school_name_tem])
            school_name_new_2.extend([""])
            school_name_new_3.extend([""])
            school_name_new_4.extend([""])
            school_name_new_5.extend([""])
        elif (len(tem_1_2)) > 0:
            school_name_tem = re.sub('<.*?>', '', str(tem_1_2[0])).replace("[","").replace("]","")\
                              .replace("&amp;","&").strip()
            school_name_new_1.extend([school_name_tem])
            school_name_new_2.extend([""])
            school_name_new_3.extend([""])
            school_name_new_4.extend([""])        
            school_name_new_5.extend([""])
            
        # CASE 2: Can not find result from original keyword
        else: # split data by , and (
            school_name_tem = str(data[j]).replace(",(","___").replace(",","___").replace("(","___")\
                              .replace(")","").replace("-","___")
            if len(school_name_tem.split("___")) == 2:
                key_1 = school_name_tem.split("___")[0].strip()
                key_2 = school_name_tem.split("___")[1].strip()
            else:
                key_1 = school_name_tem.split("___")[0].strip()
                key_2 = ""
                
             # CASE 2.1: search the first part of the keyword after splitting
            r__2 = requests.get("https://en.wikipedia.org/wiki/" + str(key_1))
            soup__2 = BeautifulSoup(r__2.text, "lxml") 
            tem_2_1 = soup__2.find_all("caption", {"class": "fn org"})
            tem_2_2 = soup__2.find_all("th", {"class": "fn org"})
                     # Get result from new keyword
            if (len(tem_2_1)) > 0:
                school_name_tem = re.sub('<.*?>', '', str(tem_2_1[0])).replace("[","").replace("]","")\
                                  .replace("&amp;","&").strip()
                school_name_new_5.extend([school_name_tem])
            elif (len(tem_2_2)) > 0:
                school_name_tem = re.sub('<.*?>', '', str(tem_2_2[0])).replace("[","").replace("]","")\
                                  .replace("&amp;","&").strip()
                school_name_new_5.extend([school_name_tem])
            else:   # Can not find result from new key word
                school_name_new_5.extend([""])
                
             # CASE 2.2: Search by alternative link
            alternative_link =  soup.find_all("a", {"class": "external text"})
            if any("Wikipedia does not have an article with this exact name" in str(x) for x in soup.find_all("b")):
                alternative_link_new = alternative_link[0].get('href')
                r__3 = requests.get("https:" + str(alternative_link_new))
                soup__3 = BeautifulSoup(r__3.text, "lxml")
                
                # CASE 2.2.1: Search by the alternative keyword if the original keyword is wrong
                did_you_mean = soup__3.find_all("div", {"class": "searchdidyoumean"})
                if len(did_you_mean) == 1:
                    did_you_mean_link_3 = did_you_mean[0].find_all("a")
                    did_you_mean_link_new_3 = did_you_mean_link_3[0].get('href')
                    r__4 = requests.get("https://en.wikipedia.org" + str(did_you_mean_link_new_3))
                    soup__4 = BeautifulSoup(r__4.text, "lxml")
                    
                    # Get all keywords similar to original keyword or the first part of the keyword after splitting
                    did_you_mean_school_name_tem = soup__4.find_all("a")
                    did_you_mean_school_name = []
                    did_you_mean_school_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                                     for x in did_you_mean_school_name_tem])
                    did_you_mean_new = []
                    did_you_mean_new_1 = []
                    did_you_mean_new.extend([x for x in did_you_mean_school_name if\
                                             re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                             in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                             and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                             for y in ["http","listof"])])
                    did_you_mean_new_1.extend([x for x in did_you_mean_school_name if\
                                               re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                               in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                               and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                               and len(str(x)) > 10\
                                               and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                               for y in ["http","listof"])])
                    
                    # Remove keyword if it equal to similar keywords        
                    remove_mean = soup__4.find_all("i")
                    if len(remove_mean) > 0:
                        if "does not exist" in str(remove_mean[0]):
                            tem_4_1 = remove_mean[0].find_all("a")
                            remove_mean_new = re.sub('<.*?>', '', str(tem_4_1[0]))
                            
                    for i in range(len(did_you_mean_new)):
                        if re.sub('[^a-zA-Z]+','',str(remove_mean_new).replace("&amp;","&")).lower()\
                            == re.sub('[^a-zA-Z]+','',str(did_you_mean_new[i]).replace("&amp;","&")).lower():
                            del did_you_mean_new[i]
                            break
                    for i in range(len(did_you_mean_new_1)):
                        if re.sub('[^a-zA-Z]+','',str(remove_mean_new).replace("&amp;","&")).lower()\
                            == re.sub('[^a-zA-Z]+','',str(did_you_mean_new_1[i]).replace("&amp;","&")).lower():
                            del did_you_mean_new_1[i]
                            break     
                        
                    # Find the nearest keyword to the original keyword
                    did_you_mean_name_1 = ""                    
                    if len(did_you_mean_new_1) > 0\
                        and any(re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                        == re.sub('[^a-zA-Z]+','', str(x)).lower() for x in did_you_mean_new_1):
                        for i in range(len(did_you_mean_new_1)):
                            if re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                               == re.sub('[^a-zA-Z]+','', str(did_you_mean_new_1[i])).lower():
                                did_you_mean_name_1 = did_you_mean_new_1[i]
                    elif len(did_you_mean_new_1) > 0:
                        did_you_mean_name_1 = did_you_mean_new_1[0]
                    else:
                        did_you_mean_name_1 = ""  
                        
                    # Search with the nearest keyword to find the final result
                    if len(did_you_mean_new_1) > 0:
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(did_you_mean_name_1))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2.extend([school_name_tem])
                        elif (len(tem_5_2)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2.extend([school_name_tem])     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(did_you_mean_new_1[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                school_name_new_2.extend([tem_tem])
                            else:
                                school_name_new_2.extend([""])
                        else:
                            school_name_new_2.extend([""])
                    else:
                        school_name_new_2.extend([""])
    
                    if len(did_you_mean_new) > 0 and school_name_new_2[j] == "":
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(did_you_mean_new[0]))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2[j] = school_name_tem
                        elif (len(tem_5_2)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2[j] = school_name_tem     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(did_you_mean_new[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                school_name_new_2[j] = school_name_tem
                            else:
                                school_name_new_2[j] = ""
                        else:
                            school_name_new_2[j] = ""
                        
                    school_name_new_1.extend([""])
                    school_name_new_3.extend([' / '.join(did_you_mean_new)])
                    school_name_new_4.extend([' / '.join(did_you_mean_new_1)])
                # CASE 2.2.1: Find all alternative keywords
                else:
                    alternative_school_name_tem = soup__3.find_all("a")
                    alternative_school_name = []
                    alternative_school_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                                    for x in alternative_school_name_tem])
                    alternative_new = []
                    alternative_new_1 = []
                    alternative_new.extend([x for x in alternative_school_name\
                                            if re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                            in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                            and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                            for y in ["http","listof"])])
                    alternative_new_1.extend([x for x in alternative_school_name\
                                              if re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                              in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                              and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                              and len(str(x)) > 10\
                                              and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                              for y in ["http","listof"])])

                    # Remove keyword if it equal to alternative keywords   
                    remove_alternative = soup__3.find_all("i")
                    remove_alternative_new = ""
                    if len(remove_alternative) > 0:
                        if "does not exist" in str(remove_alternative[0]):
                            tem_4_1 = remove_alternative[0].find_all("a")
                            remove_alternative_new = re.sub('<.*?>', '', str(tem_4_1[0]))
                        
                    for i in range(len(alternative_new)):
                        if re.sub('[^a-zA-Z]+','',str(remove_alternative_new).replace("&amp;","&")).lower()\
                           == re.sub('[^a-zA-Z]+','',str(alternative_new[i]).replace("&amp;","&")).lower():
                            del alternative_new[i]
                            break
                    for i in range(len(alternative_new_1)):
                        if re.sub('[^a-zA-Z]+','',str(remove_alternative_new).replace("&amp;","&")).lower()\
                           == re.sub('[^a-zA-Z]+','',str(alternative_new_1[i]).replace("&amp;","&")).lower():
                            del alternative_new_1[i]
                            break            
                        
                    # Find the nearest keyword to the original keyword
                    alternative_name_1 = ""                    
                    if len(alternative_new_1) > 0 and any(re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','', str(x)).lower() for x in alternative_new_1):
                        for i in range(len(alternative_new_1)):
                            if re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                               == re.sub('[^a-zA-Z]+','', str(alternative_new_1[i])).lower():
                                alternative_name_1 = alternative_new_1[i]
                    elif len(alternative_new_1) > 0:
                        alternative_name_1 = alternative_new_1[0]
                    else:
                        alternative_name_1 = ""  
                        
                    # Search with the nearest keyword to find the final result
                    if len(alternative_new_1) > 0:
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(alternative_name_1))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2.extend([school_name_tem])
                        elif (len(tem_5_2)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2.extend([school_name_tem])     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(alternative_new_1[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                school_name_new_2.extend([tem_tem])
                            else:
                                school_name_new_2.extend([""])
                        else:
                            school_name_new_2.extend([""])
                    else:
                        school_name_new_2.extend([""])
    
                    if len(alternative_new) > 0 and school_name_new_2[j] == "":
                        r__5 = requests.get("https://en.wikipedia.org/wiki/" + str(alternative_new[0]))
                        soup__5 = BeautifulSoup(r__5.text, "lxml") 
                        tem_5_1 = soup__5.find_all("caption", {"class": "fn org"})
                        tem_5_2 = soup__5.find_all("th", {"class": "fn org"})
    
                        if (len(tem_5_1)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_1[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2[j] = school_name_tem
                        elif (len(tem_5_2)) > 0:
                                school_name_tem = re.sub('<.*?>', '', str(tem_5_2[0])).replace("[","")\
                                                  .replace("]","").replace("&amp;","&").strip()
                                school_name_new_2[j] = school_name_tem     
                        elif len(soup__5.find_all("a")) > 0:
                            tem_tem = re.sub('<.*?>', '', str(soup__5.find_all("a")[0])).replace("[","")\
                                      .replace("]","").replace("&amp;","&").strip()
                            if re.sub('[^a-zA-Z]+','', str(alternative_new[0])).lower()\
                               in re.sub('[^a-zA-Z]+','', str(tem_tem)).lower():
                                school_name_new_2[j] = school_name_tem
                            else:
                                school_name_new_2[j] = ""
                        else:
                            school_name_new_2[j] = ""
                                                    
                    school_name_new_1.extend([""])
                    school_name_new_3.extend([' / '.join(alternative_new)])
                    school_name_new_4.extend([' / '.join(alternative_new_1)])
           
           # Get keywords refer to ariginal keywords   
            else:
                refer_to_shool_name_tem = soup.find_all("a")
                refer_to_shool_name = []
                refer_to_shool_name.extend([re.sub('<.*?>', '', str(x)).replace("&amp;","&").strip()\
                                            for x in refer_to_shool_name_tem])
                refer_to_new = []
                refer_to_new_1 = []
                refer_to_new.extend([x for x in refer_to_shool_name\
                                     if re.sub('[^a-zA-Z]+','', str(key_1)).lower()\
                                     in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                     and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                     for y in ["http","listof"])])
                refer_to_new_1.extend([x for x in refer_to_shool_name\
                                       if re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                       in re.sub('[^a-zA-Z]+','', str(data[j])).lower()\
                                       and re.sub('[^a-zA-Z]+','', str(x)).lower() != ""\
                                       and len(str(x)) > 10\
                                       and all(y not in re.sub('[^a-zA-Z]+','', str(x)).lower()\
                                       for y in ["http","listof"])])
               
         # Find the nearest keyword to the original keyword
                for i in range(len(refer_to_new)):
                    if re.sub('[^a-zA-Z]+','',str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','',str(refer_to_new[i])).lower():
                        del refer_to_new[i]
                        break
                for i in range(len(refer_to_new_1)):
                    if re.sub('[^a-zA-Z]+','',str(data[j])).lower()\
                       == re.sub('[^a-zA-Z]+','',str(refer_to_new_1[i])).lower():
                        del refer_to_new_1[i]
                        break
                                                    
                school_name_new_1.extend([""])
                school_name_new_2.extend([""])
                school_name_new_3.extend([' / '.join(refer_to_new)])
                school_name_new_4.extend([' / '.join(refer_to_new_1)])
        
        # Get the best keywords if can not find the result
        if school_name_new_1[j] != "" or school_name_new_2[j] != "":
            school_name_new_2[j] = school_name_new_2[j]
        elif school_name_new_1[j] == ""\
             and school_name_new_2[j] == ""\
             and school_name_new_3[j] == ""\
             and school_name_new_4[j] == "":
            school_name_new_2[j] = school_name_new_5[j]
        else:
            school_name_new_2[j] = school_name_new_5[j]
    
    return pd.DataFrame({'school_name_a_ori': data,
                       "school_name_new_1": school_name_new_1,
                       "school_name_new_2": school_name_new_2,
                       "school_name_new_3": school_name_new_3,
                       "school_name_new_4": school_name_new_4,
                       "school_name_new_5": school_name_new_5})





x = gls_preprocess('01 march 2016', None,None,None,None,None,None)
print("Result: ", x.gls_date())