
# coding: utf-8

# In[8]:

import pandas as pd
import datetime as dt
import time
import datetime


# In[9]:

def clean_datetime(date_text):
    def is_present(date_text):
        for t in ["Present", "Current", "Now", "c", "p"]:
            if date_text.upper() == t.upper():
                return True
        return False

    if isinstance(date_text, datetime.date): #  or type(date_text) is pd.tslib.Timestamp:
        return date_text
    
    # NaTType
    if not isinstance(date_text, str):
        return None

    # Parse from text
    date_text = date_text.strip()

    # Replace &nbsp;
    date_text = date_text.replace('&nbsp;', ' ')
    date_text = date_text.replace('&ndash;', '-')
    date_text = date_text.rstrip('-')  # May 2012 -

    date_text = date_text.replace('Sept ', 'Sep ')
    date_text = date_text.replace('Febr ', 'Feb ')
    date_text = date_text.replace('Sept ', 'Sep ')
    date_text = date_text.replace('Octo ', 'Oct ')

    date_text = date_text.strip()

    # date_text is empty?
    if not date_text:
        return None

    # Current or present
    if is_present(date_text):
        # _date = dt.datetime.now()
        # return _date.date()
        return 'Current'

    # try:
    #     _date = dateparser.parse(date_text)
    # except:
    #     pas

    _date = date_text
    dateFormats = (
        '%B %Y', '%b %y', '%b %Y', '%Y %B', '%Y %b', '%B%Y', '%b%Y', '%B%y',
        '%Y',
        '%b %d, %Y', '%B %d, %Y',
        '%Y - %m', '%m/%y', '%m-%y', '%b. %Y', '%b, %Y',
        '%b %d,%Y',
        '%m/%d/%Y', '%m/%d/%y', '%d/%m/%Y', '%d/%m/%y', '%Y/%m', '%m/%Y',
        '%m-%d-%Y', '%m-%d-%y', '%d-%m-%Y', '%d-%m-%y', '%Y-%m', '%m-%Y',
        '%Y-%m-%d', '%Y-%M-%d', '%y-%m-%d', '%y-%M-%d',
        '%b-%y')
    for dateformat in dateFormats:
        try:
            _date = dt.datetime.strptime(date_text, dateformat)
            break
        except ValueError as err:
            pass

    try:
        _date = _date.date()
    except AttributeError as err:
        # logging.error("Error when validateDateTime %s" % err)
        print ("Error when validateDateTime ",  err)
        return None
    return _date


    def check_date_time(_date):

        year = _date.year
        #print year
        month = _date.month
        day = _date.day
        if year < 1016:
        #new_year=year+1000

        #_date.replace(year=new_year)
            _date=_date+relativedelta(years=1000)
        if year >3000:
            _date=_date-relativedelta(years=1000)
        if month not in range(1, 12):
            _date.replace(month=6)
        if day not in range(1, 31):
            _date.replace(day=15)
        date = _date

        return date

    for fmt in dateFormats:
        try:

            _date = check_date_time(dt.strptime(date_text,fmt))
            break
        except:
            pass        


    _date=_date.date()
    return _date


# In[ ]:




# In[12]:

def current_to_date(x):
    return datetime.datetime.now().date() if x == 'Current' else x


# In[ ]:



