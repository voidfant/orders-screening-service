from dataManagers import *
from psqlActions import PsqlActions
import sys


if len(sys.argv) == 1:
    while True:
        compareDates()
        PsqlActions().clearTable()
        PsqlActions().insertData(readData())
elif sys.argv[1] == '--up' or sys.argv[1] == '-u':
    try:
        PsqlActions().initDatabase()
        print('Successfully initialized database.')
    except Exception as e:
        print('Failed to initialize database: {}'.format(e))
elif sys.argv[1] == '--down' or sys.argv[1] == '-d':
    print('Are you sure? This action will erase all the data from the database. (y/n):', end=' ')
    decision = input()
    if decision.lower() == 'y' or decision.lower() == 'yes':
        try:
            PsqlActions().downDatabase()
            print('Succesfully dropped database.')
        except Exception as e:
            print('Failed to drop database: {}'.format(e))
    else:
        print('Operation aborted.')



