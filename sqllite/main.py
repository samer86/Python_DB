# import welwel
from welwel import database

samer = database('Northwind2020.db')

x = samer.query('select * from [order] limit 6;')
samer.query('delete from [order] where id <5;')

# samiha = welwel.database('Northwind2020.db')
# samiha.query('delete from [order] where id <5;')
# samiha.query('select * from [order] limit 6;')


def y(x): return samer.query(x)


x = 'select * from [order] where id = 1;'


d = y('delete from [order] where id > 400')
d = y('select * from customer limit 10;')

d = d.set_index('Id')
database('Northwind2020')
eee = database('Northwind2020')
eee.query('select * from [order] limit 10;')
