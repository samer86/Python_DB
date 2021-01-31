# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:29:22 2021

@author: salem
"""

# import welwel
from sqliteDB_SS import database
db = database('Northwind2020.db')
y = lambda x,**kwargs: db.query(x,**kwargs)



order = y('select * from [order] limit 10')


delete = db.query('delete from [order] where id < 10')

y('commit;')
y('rollback;')

customer = y('select * from customer where id =:UID',params={'UID':'7'})

christina= db.query('select * from customer where id =:UID',params={'UID':'5'})


customer_X = y('select firstname from customer where id <20')








