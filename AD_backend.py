import mysql.connector
from tkinter import ttk, messagebox

#NOTES:
#roll
#name
#gender
#dob
#email
#phone

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

def update(roll,name,gender,dob,email,phone,tree_table):
	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

	cur.execute("UPDATE student SET name = '%s', gender = '%s', dob = '%s', email = '%s',phone = '%s' WHERE roll = '%s'"%(name,gender,dob,email,phone,roll))
	conn.commit()
	show_all_data(tree_table)

####################################################################################################################################

####################################################### SEARCH BY/FOR ##############################################################

def set_search_by_option(search_parameter,tree_table,search_parameter_entry):

	try:
		conn=mysql.connector.connect(user='root',password='12345',host='localhost',database='restaurant_management')
		cur=conn.cursor()
	except:
		messagebox.showerror('Error','System can\'t connect with MySQL for some reason')

	if search_parameter == 'Roll No.':
		search_parameter = 'roll'
	if search_parameter == 'Name':
		search_parameter = 'name'
	if search_parameter == 'Gender':
		search_parameter = 'gender'
	if search_parameter == 'Date of Birth':
		search_parameter = 'dob'
	if search_parameter == 'Email':
		search_parameter = 'email'
	if search_parameter == 'Phone No.':
		search_parameter = 'phone'

	cur.execute("SELECT * FROM student WHERE %s = '%s'"%(search_parameter,search_parameter_entry))
	data_rows = cur.fetchall()
	tree_table.delete(*tree_table.get_children())
	for row in data_rows:
		tree_table.insert('','end',values=(row))

####################################################################################################################################

connect()
