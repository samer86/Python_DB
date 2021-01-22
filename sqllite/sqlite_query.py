# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:55:30 2021

@author: salem
"""
from IPython.display import display 
import sqlite3
from sqlite3 import Error
import pandas as pd
'''CONNECT USING sqlite3 '''
conn = sqlite3.connect('class.db')
cursor = conn.cursor()
print("Opened database successfully")
cursor.close()


class database():
    __query = ''
    results = []
    columns = []
    __data= ''
    __tables = ''
    auto_print = True


    def __init__(self):
        
        # it only needed to call (get) self.tables so it will issue a query that already in get method!
        self.tables
        
        # self.history = history()


    @property
    def query(self):

        print(self.__query)
        return self.__query

    @query.setter
    def query(self,stmt):
        self.__query = stmt
        #Create cursor and send stmt query to database
        try:
            cursor = conn.cursor()
            res = cursor.execute(stmt)
            rows =res.fetchall()
            #Save columns from the query into self.columns
            if isinstance(cursor.description,tuple):
                self.columns= [tuple[0] for tuple in cursor.description]
                # print(self.columns)
            else:
                self.columns=[]
                # print(self.columns)
            '''save results into self.results using generator method!'''
            results = [row for row in rows]
            if len(results)> 0 :
                self.results = results
            else:
                self.results = 'There are no data to show!'

            '''
            1. Make a dataframe from (rows and columns) if rows has data.
            2. Else assign (there are no data) to self.__data
                a. Check if there are columns, if yes its an empty dataframe
                    Then Query Successfully commer.
                b. Else just print the dataFrame.
            '''

            if len(results)>0:
                self.__data= pd.DataFrame(rows,columns=self.columns)
                if self.auto_print:
                    print(self.__data.to_string(index=False))
                # display(self.__data)
                self.save_history(stmt)
            else:
                self.__data = 'There are no data to show!'
                if len(self.columns) == 0:
                    print('Query Successfully Finished!')
                else :
                    # print('hello from else' )
                    self.__data = pd.DataFrame(rows,columns=self.columns)

                    if self.auto_print:
                        print(pd.DataFrame(rows,columns=self.columns))
                    # display(self.__data)
                    self.save_history(stmt)
                    
            ''' Add Affected Rows if there are any '''        
            if res.rowcount != -1:
                print(f'Affected rows: {res.rowcount}')

            #Closing connection: cursor
            cursor.close()
            
        except Error as e :
            print(e)
        

    def data(self):
        return self.__data
        
    def commit(self):
        conn.commit()
        
        # return 'There are no data to show!'
    @property
    def tables(self):
        # print('This is tables getter')
        self.query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.__tables = self.data()
     
    @tables.setter
    def tables(self,stmt):
        pass
    
    def save_history(self,stmt):
        pass
            




########## [####] ###########



class nc(database):
    
    __cmd_history = []
    saving_history = ''
    hi = 'Hello'
       
    
    def __init__(self):
        self.history = history()
        self.saving_history = input('yes/no : ')
        # print('Hello From class')
        
        
    def save_history(self,stmt):
        if self.saving_history == 'yes':
            temp = input('Please Enter CMD name: ')
            if temp !='':
                self.__cmd_history.append({"CMD_Name":temp,"CMD": stmt})

    @property
    def history(self):
        return pd.DataFrame.from_dict(self.__cmd_history)
    
    
    @history.setter
    def history(self):
        pass



def main():
    pass
    # db=nc()
    # newclass = nc()


if __name__ == "__main__":
    # main()
    db=nc()

