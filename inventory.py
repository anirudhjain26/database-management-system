import mysql.connector
from tkinter import ttk, messagebox


def connect():
    try:
        conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
        cur=conn.cursor()
    except:
        messagebox.showerror('Error','System can\'t connect with database for some reason')

    cur.execute("CREATE TABLE IF NOT EXISTS inventory(id char(20) not null , material_name char(20) , material_type char(20) , cost int, quantity int, date_purchase DATE, primary key (id))")
    conn.commit()

####################################################### SHOW_ALL ##################################################################

def show_all_data(tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT * FROM inventory")
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

########################################################## ADD #####################################################################

def add(id, material_name, material_type, cost, quantity, date_purchase,tree_table):
	try:
		if (id and material_name and material_type and cost and quantity and date_purchase) != '':
			try:
				conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
				cur=conn.cursor()
			except:
				messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

			cur.execute("INSERT INTO inventory (id, material_name, material_type, cost, quantity, date_purchase) VALUES ('%s','%s','%s','%s','%s','%s')"%(id, material_name, material_type, cost, quantity, date_purchase))
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
		cur.execute("DELETE FROM inventory WHERE id='%s'"%(str(delete_id)))
		conn.commit()
		show_all_data(tree_table)
	except:
		pass

####################################################################################################################################

####################################################### UPDATE #####################################################################

def update(id, material_name, material_type, cost, quantity, date_purchase,tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("UPDATE inventory SET material_name = '%s', material_type = '%s', cost = '%s', quantity = '%s',date_purchase = '%s' WHERE id = '%s'"%(material_name, material_type, cost, quantity, date_purchase,id))
	conn.commit()
	show_all_data(tree_table)

####################################################################################################################################

def getInvCost(tree_table):
	try: 
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT SUM(cost*quantity) from inventory")
	cost = cur.fetchone()
	return cost


connect()
