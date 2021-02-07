# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:19:44 2021

@author: salem
"""

from IPython.display import display
import sqlite3
from sqlite3 import Error
import pandas as pd
import sys

c = sqlite3.connect('Northwind2020.db')
print("Opened database successfully")


class database():
    __c = ''
    stmt = ''
    results = []
    columns = []
    __data = ''
    __tables = ''
    auto_print = True

    def __init__(self, db_name):
        ''' Starting point:
            1. create sqlite connector and save in __c '''
        self.__c = sqlite3.connect(db_name)
        # TODO: Add Table Function.
        self.tables

    @property
    def stmt(self):
        print(self.__query)
        return self.__query

    def query(self, stmt, **kwargs):
        ''' Query landing point:
            1. Get query body plus (**kwarg as params...)
            2. if statement will take 2 paths:
                a. select: exrcute directly & save data in data().
                b. all other commands 




         '''
        self.__query = stmt
        try:
            if stmt.lower().strip()[0:6] == 'select':
                self.__data = pd.read_sql_query(stmt, self.__c, **kwargs)
                print(self.__data)
            else:
                # TODO: catch pragma table!
                res = self.__c.execute(stmt)
                print('Query Successfully Finished!')
                self.__data = 'No Returned Data'
                if res.rowcount != -1:
                    print(f'Affected rows: {res.rowcount}')

        except:
            '''Print out the Error message.'''
            print(sys.exc_info()[1])

        finally:
            return self.__data

    def data(self):
        return self.__data

    def commit(self):
        c.commit()

    @property
    def tables(self):
        pass

    @tables.setter
    def tables(self, stmt):
        pass

    def save_history(self, stmt):
        pass

    def __setattr__(self, name, value):
        ''' Prevent (query) method from being changed! '''
        if name == "query":
            print(''' Protected Method! \ln
                      Cant Modify this method ''')

        else:
            super().__setattr__(name, value)

# db = database()


''' Importing this lines: '''
# from sqliteDB_SS import database
# db = database('Northwind2020.db')
# q = lambda x,**kwargs: db.query(x,**kwargs)
