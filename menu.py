import mysql.connector
from tkinter import ttk, messagebox


def connect():
    try:
        conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
        cur=conn.cursor()
    except:
        messagebox.showerror('Error','System can\'t connect with database for some reason')

    cur.execute("CREATE TABLE IF NOT EXISTS menu(id char(20) not null , dish_name char(20) , cuisine char(20) , price int, num_sold int, chef_special boolean, primary key (id))")
    conn.commit()

####################################################### SHOW_ALL ##################################################################

def show_all_data(tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT * FROM menu")
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

########################################################## ADD #####################################################################

def add(id,dish_name,cuisine,price,num_sold,chef_special,tree_table):
	try:
		if (id and dish_name and cuisine and price and num_sold and chef_special) != '':
			try:
				conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
				cur=conn.cursor()
			except:
				messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

			cur.execute("INSERT INTO menu (id,dish_name,cuisine,price,num_sold,chef_special) VALUES ('%s','%s','%s','%s','%s','%s')"%(id,dish_name,cuisine,price,num_sold,chef_special))
			conn.commit()
			
			show_all_data(tree_table)
	except:
		messagebox.showerror('Error','An item with this ID already exists')

###################################################################################################################################

####################################################### DELETE ####################################################################

def delete(delete_id,tree_table):
	try:
		try:
			conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
			cur=conn.cursor()
		except:
			messagebox.showerror('Error','System can\'t connect with database for some reason')

		delete_id = delete_id['values'][0]
		cur.execute("DELETE FROM menu WHERE id='%s'"%(str(delete_id)))
		conn.commit()
		show_all_data(tree_table)
	except:
		pass

####################################################################################################################################

####################################################### UPDATE #####################################################################

def update(id,dish_name,cuisine,price,num_sold,chef_special,tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("UPDATE menu SET chef_special = '%s', dish_name = '%s', cuisine = '%s', price = '%s',num_sold = '%s' WHERE id = '%s'"%(chef_special,dish_name,cuisine,price,num_sold,id))
	conn.commit()
	show_all_data(tree_table)

####################################################################################################################################

def getTotalSales(tree_table):
	try: 
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT SUM(price*num_sold) from menu")
	sales = cur.fetchone()
	return sales

connect()
