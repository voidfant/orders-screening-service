from os import getenv
from dotenv import load_dotenv, set_key
import gspread
# from dataMonitoring.tools import convertDate
from time import sleep
from psqlActions import PsqlActions
from datetime import date, timedelta, datetime
from notifier import sendTelegram


def readData():
    load_dotenv(override=True)
    gc = gspread.oauth(credentials_filename=getenv('OAUTH_PATH'))
    table = gc.open_by_key(getenv('GSPREAD_ID'))
    return table.sheet1.get_all_values()[1:]

def compareDates():
    count = 0
    load_dotenv(override=True)
    latestDate=getenv('LAST_UPDATE')
    gc = gspread.oauth(credentials_filename=getenv("OAUTH_PATH"))
    while latestDate == getenv('LAST_UPDATE'):
        latestDate = gc.open_by_key(getenv('GSPREAD_ID')).lastUpdateTime
        count += 1
        if count == 99:
            sleep(100)
            count = 0
            checkDate()
            continue
        sleep(4)
    set_key(dotenv_path='dataMonitoring/.env', key_to_set='LAST_UPDATE', value_to_set=latestDate)
    load_dotenv(override=True)
    print(latestDate)
    
def checkDate():
    # count = 0
    load_dotenv(override=True)
    lastDate = getenv('DATE')
    if lastDate != str(date.today()):
        yesterday = date.today() - timedelta(days=1)
        # PsqlActions().findOutdated(yesterday.strftime('%d.%m.%Y'))
        data = PsqlActions().getAllArrivalDates()
        users = PsqlActions().getAllUsers()
        for val in data:
            if convertDate(val[1]) < date.today():
                sendTelegram(user_ids=users, data=val)
                # print(val)
                # count += 1
        # print(count)
        # print(lastDate, str(date.today()), sep='\t\t')
        set_key(dotenv_path='dataMonitoring/.env', key_to_set='DATE', value_to_set=str(date.today()))
    

def convertDate(date):
    template = "%d.%m.%Y"
    date = datetime.strptime(date, template)
    return date.date()

if __name__ == '__main__':
    checkDate()