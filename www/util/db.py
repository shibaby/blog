import psycopg2
from DBUtils.PooledDB import PooledDB

Pool = PooledDB(psycopg2, host = 'localhost', database = 'tuji_plantapp', user = 'postgres', password = 'tuji2013', port = 5432)

def release(*args):
   for arg in args:
      if arg:
         arg.close()



