import mysql.connector
from tkinter import ttk, messagebox


def connect():
    try:
        conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
        cur=conn.cursor()
    except:
        messagebox.showerror('Error','System can\'t connect with database for some reason')

    cur.execute("CREATE TABLE IF NOT EXISTS employees(code char(20) not null , e_name char(20) , e_hours int, e_salary int, primary key (code))")
    conn.commit()

####################################################### SHOW_ALL ##################################################################

def show_all_data(tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT * FROM employees")
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

########################################################## ADD #####################################################################

def add(code, e_name, e_hours, e_salary,tree_table):
	try:
		if (code and e_name and e_hours and e_salary) != '':
			try:
				conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
				cur=conn.cursor()
			except:
				messagebox.showerror('Error','System can\'t connect with database for some reason')

			cur.execute("INSERT INTO employees (code, e_name, e_hours, e_salary) VALUES ('%s','%s','%s','%s','%s','%s')"%(code, e_name, e_hours, e_salary))
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
		cur.execute("DELETE FROM employees WHERE id='%s'"%(str(delete_id)))
		conn.commit()
		show_all_data(tree_table)
	except:
		pass

####################################################################################################################################

####################################################### UPDATE #####################################################################

def update(code, e_name, e_hours, e_salary,tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("UPDATE employees SET e_name = '%s', e_hours = '%s', e_salary = '%s' WHERE code = '%s'"%(e_name, e_hours, e_salary,code))
	conn.commit()
	show_all_data(tree_table)

####################################################################################################################################

def getSalCost(tree_table):
	try: 
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with database for some reason')

	cur.execute("SELECT SUM(salary) from employees")
	cost = cur.fetchone()
	return cost

connect()
