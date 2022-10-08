from getData import pullData
from tools import *
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import defaultdict

def saveGraph():
    
    data = pullData(internal=True)
    dates = []
    values = []

    blob = defaultdict(int)
    for el in data:
        blob[convertToDatetime(el['order_date'])] += el['cost_usd']
    
    blob = list(blob.items())

    blob.sort(key=lambda x: x[0])
    for el in blob:
        dates.append(el[0])
        values.append(el[1])

    for k, v in enumerate(dates):
        dates[k] = convertFromDatetime(v)
    
    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(dates, values)
    ax.fmt_xdata = mdates.DateFormatter('%d.%m.%Y')
    plt.tick_params(axis='x', which='major', labelsize=7)
    plt.tick_params(axis='y', which='major', labelsize=7)
    plt.tight_layout()
    plt.grid(axis='y', color='0.95')
    plt.gcf().autofmt_xdate()
    fig.savefig('test.png')
