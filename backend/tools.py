from datetime import datetime, date

def convertToDatetime(date):
    template = "%d.%m.%Y"
    date = datetime.strptime(date, template)
    return date.date()

def convertFromDatetime(date):
    template = "%d.%m.%Y"
    date = datetime.strftime(date, template)
    return date


# print(convertFromDatetime(date.today()))
