# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:06:42 2021

@author: salem
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:11:26 2021

@author: salem
"""
# import numpy as np
# from tabulate import tabulate
# import pymysql
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.automap import automap_base 
# from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, Boolean , exc
import os
import pandas as pd
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, MetaData, Table, exc
from sqlalchemy.inspection import inspect

'''Class can add attributes DYNAMICALY'''

'''
Functionalities: 
    1. Class adding Tables variables dynamiclly.
    2. Using attributes as tables and methods as CRUD.

Areas to enhance: 
    General: add tables to it's own attribute and not just general attribute to the object.
    
    
Updating method:
    1. Choose what column to match.
    2. Add option for updating the primary key.
'''

class c():
    
    def __init__(self,class_name):

        '''CREATE ENGINE'''
        global engine,conn
        engine=create_engine(f'sqlite:///{class_name}.db')
        conn = engine.connect()
        
        '''START SESSION'''
        global session
        session = Session(engine)
        
        '''INIT MetaData'''
        global metadata
        metadata = MetaData()
        
        '''Get tables names Dynamically'''
        global tables
        tables={}
        for i in engine.table_names():
            tables[f'{i}'] = Table( i , metadata, autoload=True, autoload_with=engine)
        
        global data
        data={}
        for k,v in tables.items():
            query = session.query(v)
            data[k] = pd.read_sql(query.statement, engine)
            
            
    def add_tables(self):
        ''' Adding Tables as attributes'''
        for key, value in tables.items():
            self.__dict__[key] = value
            
            
    def read(self,*tab):
        ''' Reading from tables, serving 2 options:
            1. reading general will list all tables to choose from.
            2. read with table name as variable will directly read that table.
            '''
        if len(tab)>0:
            print(self.__dict__[tab[0]].columns.keys())
            query = session.query(self.__dict__[tab[0]])
            df=pd.read_sql(query.statement, engine)
            print(df.to_string(index=False))
        else:
            print('Table Names: ')
            for k in self.__dict__.keys():
                print(k)
            db = input('Read from table: ')
            print(self.__dict__[db].columns.keys())
            query = session.query(self.__dict__[db])
            df=pd.read_sql(query.statement, engine)
            print(df.to_string(index=False))
            
    def update(self):
        ''' Update Method
            - Using The first column as matching point. 
            - Will scape any column if its a primary.
        '''
        print('Table Names: ')
        for k in self.__dict__.keys():
            print(k)
        print('!METHOD IS UPDATING!')
        db = self.choose_table()
        if db != 'Exit' and db != 'exit':
            self.read(db)
        # print(db)
        updated = input('Enter ID Nr to update: ')
        prime = inspect(self.__dict__[db]).primary_key.columns.keys()
        temp_dict={}
        for i in self.__dict__[db].columns.keys():
            if i not in prime:
                val = input(f'Insert {i}: ')
                temp_dict[i]=val
        ins = self.__dict__[db].update().where(self.__dict__[db].c[f'{self.__dict__[db].c.keys()[0]}']==updated).values(temp_dict)
        # print(ins)
        # conn = engine.connect()
        conn.execute(ins)
        self.read(db)
        
        
    def insert(self):
        print('Table Names: ')
        for k in self.__dict__.keys():
            print(k)
        print('!METHOD IS INSERION!')
        db = self.choose_table()
        if db != 'Exit' and db != 'exit':
            clear()
            self.read(db)
            # print(self.__dict__[db].columns.keys())
            val = ''
            prime = inspect(self.__dict__[db]).primary_key.columns.keys()
            # if len(prime)==0:
            #     prime=''
            
            while True:
                temp_dict={}
                for i in self.__dict__[db].columns.keys():
                    if i not in prime:
                        val = input(f'Insert {i}: ')
                        temp_dict[i]=val
                print(temp_dict)
                ins = self.__dict__[db].insert().values(temp_dict)
                conn.execute(ins)
                self.read(db)
                choice = input('Add more entry? Please answer with y/n: ')
                if choice =='n' or choice == 'N':
                    break
        
        
    def delete(self):
        print('Table Names: ')
        for k in self.__dict__.keys():
            print(k)
        # db = input('Insert table name: ')
        db = self.choose_table()
        while True:
            if db != 'Exit' and db !='exit':
                self.read(db)
                # print(self.__dict__[db].columns.keys())
                Nr= int(input('Enter ID number to delete: '))
                D = f"delete from {self.__dict__[db]} where {self.__dict__[db].columns.keys()[0]} = {Nr}"
                conn.execute(D)
                self.read(db)
                choice = input('Deleting more rows y/n : ')
                if choice == 'n':
                    return
        
    def choose_table(self):
        while True:
            print('Please Enter Table Name or Exit')
            db = input('Insert table name: ')
            if db in self.__dict__.keys():
                return db
            elif db =='Exit' or db =='exit':
                return db
            
        
    def manual(self):
        while True:
            ins = input('Insert SQL Query:\n')
            if ins =='Exit':
                break
            try: 
                res = conn.execute(ins)
                print(res.keys())
                for i in res:
                    print(i)
            except exc.SQLAlchemyError  as e:
                print(e)
def clear():
    os.system( 'cls' )
        
def main():
   
    # inspect(Teacher).primary_key[0].name
    class_name = input('Please Enter Database name: ')
    db= c(class_name)
    db.add_tables()
    while True:
        try:
            Ch = int(input('Your choise(0 for help): '))
            if Ch == 0:
                clear()
                print('Enter a method number: \n 0. Help list \n 1. Read \n 2. Insert \n 3. Update \n 4. Delete \n 5. Manuel \n 6. Exit prog.')
            if Ch ==6:
                break
            if Ch == 1:
                clear()
                db.read()
            if Ch == 2:
                clear()
                db.insert()
            if Ch == 3:
                clear()
                db.update()
            if Ch == 4:
                clear()
                db.delete()
            if Ch == 5:
                clear()
                db.manual()
        except:
            print('Please Enter a valid choice.')
            
       
    
        


if __name__ == "__main__":
    main()




