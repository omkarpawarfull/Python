import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='1trydatabase' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='1trydatabase' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()




def view():
    conn=psycopg2.connect("dbname='1trydatabase' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()             #to get the list of rows
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='1trydatabase' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE ITEM=%s",(item,))
    conn.commit()
    conn.close()

def update(qunatity,price,item):
    conn=psycopg2.connect("dbname='1trydatabase' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(qunatity,price,item))
    conn.commit()
    conn.close()

create_table()
insert("dish",20,15)
#update(4,4,"Plastic Glass")
#print(view())
