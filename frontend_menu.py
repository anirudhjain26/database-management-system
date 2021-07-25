from tkinter import *
from tkinter import ttk, messagebox
import menu##table name is student

class Student:
	def __init__(self,win):
		self.win = win
		self.win.title('Restaurant Management System')
		self.win.geometry('1000x600+150+40')
		self.bg = 'gray13'
		self.fg = 'red2'
		self.win["bg"] = self.bg

		##############FUNCTIONS#############################
		def clear():
			self.VAR_phone_no.set("")
			self.VAR_roll_no.set("")
			self.VAR_name.set("")
			self.VAR_gender.set("")
			self.VAR_dob.set("")
			self.VAR_email.set("")

		def on_click(*args):
			try:
				data = (self.table.item(self.table.focus()))['values']
				self.VAR_phone_no.set(data[5])
				self.VAR_roll_no.set(data[0])
				self.VAR_name.set(data[1])
				self.VAR_gender.set(data[2])
				self.VAR_dob.set(data[3])
				self.VAR_email.set(data[4])
			except:
				messagebox.showerror('Error','Please select a relevent ID')
		####################################################
		
		##############HEADER#############
		header = Label(self.win,text="Restaurant Management System",font=('algerian',40,''),bg=self.bg,fg=self.fg)
		header.pack(side=TOP,fill=X)
		#################################

		##########ALL-VARIABLES#########
		self.VAR_roll_no = StringVar()
		self.VAR_name = StringVar()
		self.VAR_gender = StringVar()
		self.VAR_dob = StringVar()
		self.VAR_email = StringVar()
		self.VAR_phone_no = StringVar()
		################################

		########ENTRY-FIELD-FRAME########
		field_frame = Frame(self.win,bd=5,relief=RIDGE,bg=self.bg)
		field_frame.place(x=20,y=80,width=370,height=510)

		####HEAD####
		head = Label(field_frame,text='Information Form',bg=self.bg,fg=self.fg,font=('times',25,'bold underline'))
		head.grid(row=0,columnspan=2,padx=47)
		############

		###LABELS###
		L_name = Label(field_frame,text='Name',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_name.grid(row=1,column=0,pady=10,sticky='w',padx=20)
		L_roll_no = Label(field_frame,text='Roll No.',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_roll_no.grid(row=2,column=0,pady=10,sticky='w',padx=20)
		L_gender = Label(field_frame,text='Gender',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_gender.grid(row=3,column=0,pady=10,sticky='w',padx=20)
		L_dob = Label(field_frame,text='Date of birth',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_dob.grid(row=4,column=0,pady=10,sticky='w',padx=20)
		L_email = Label(field_frame,text='Email',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_email.grid(row=5,column=0,pady=10,sticky='w',padx=20)
		L_phone_no = Label(field_frame,text='Phone No.',bg=self.bg,fg=self.fg,font=('times',20,'bold'))
		L_phone_no.grid(row=6,column=0,pady=10,sticky='w',padx=20)
		############

		###ENTRY###
		E_name = Entry(field_frame,textvariable=self.VAR_name,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_name.grid(row=1,column=1,pady=10,sticky='w')
		E_roll_no = Entry(field_frame,textvariable=self.VAR_roll_no,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_roll_no.grid(row=2,column=1,pady=10,sticky='w')
		E_gender = ttk.Combobox(field_frame,textvariable=self.VAR_gender,font=('times',20,'bold'),width=9,state='readonly')
		E_gender['values'] = ('Male','Female','Other')
		E_gender.grid(row=3,column=1,pady=10,sticky='w')
		E_dob = Entry(field_frame,textvariable=self.VAR_dob,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_dob.grid(row=4,column=1,pady=10,sticky='w')
		E_email = Entry(field_frame,textvariable=self.VAR_email,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_email.grid(row=5,column=1,pady=10,sticky='w')
		E_phone_no = Entry(field_frame,textvariable=self.VAR_phone_no,bg=self.bg,fg=self.fg,font=('times',20,'bold'),width=10,bd=3)
		E_phone_no.grid(row=6,column=1,pady=10,sticky='w')
		###########

		##BUTTONS##
		B_add = Button(field_frame,text='Add',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:menu.add(E_roll_no.get(),E_name.get(),E_gender.get(),E_dob.get(),E_email.get(),E_phone_no.get(),self.table))
		B_add.grid(row=7,column=0,padx=15,sticky='w')
		B_delete = Button(field_frame,text='Delete',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:menu.delete(self.table.item(self.table.focus()),self.table))
		B_delete.grid(row=7,column=1,sticky='w',padx=15)
		B_update = Button(field_frame,text='Update',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=lambda:menu.update(E_roll_no.get(),E_name.get(),E_gender.get(),E_dob.get(),E_email.get(),E_phone_no.get(),self.table))
		B_update.grid(row=8,column=0,pady=5,padx=15,sticky='w')
		B_clear = Button(field_frame,text='Clear',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',15,'bold'),width=15,bd=10,command=clear)
		B_clear.grid(row=8,column=1,pady=5,padx=15,sticky='w')
		###########

		#################################

		########INFORMATION-FRAME########
		info_frame = Frame(self.win,bd=5,relief=RIDGE,bg=self.bg)
		info_frame.place(x=410,y=80,width=570,height=510)

		####HEAD####
		search_by = Label(info_frame,text='Search By',bg=self.bg,fg=self.fg,font=('times',15,'bold underline'))
		search_by.grid(row=0,column=0)
		search_by_options = ttk.Combobox(info_frame,font=('times',11,'bold'),width=9,state='readonly')
		search_by_options['values'] = ('Name','Roll No.','Gender','Date of Birth','Email','Phone No.')
		search_by_options.grid(row=0,column=1,pady=10,sticky='w',padx=3)
		E_search_by = Entry(info_frame,bg='gray30',fg=self.fg,font=('times',12,'bold'),width=20,bd=2)
		E_search_by.grid(row=0,column=3,pady=10,sticky='w')
		B_search_by = Button(info_frame,text='Search',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',9,'bold'),width=20,bd=3,command=lambda:menu.set_search_by_option(search_by_options.get(),self.table,E_search_by.get()))
		B_search_by.grid(row=0,column=4,pady=10,padx=5,sticky='w')
		B_showall = Button(info_frame,text='Show All',highlightbackground='#3E4149',bg=self.bg,fg=self.fg,font=('times',9,'bold'),width=30,bd=3,command=lambda:menu.show_all_data(self.table))
		B_showall.grid(row=0,column=5,pady=10,sticky='w')
		############

		#####FIELD_INFORMATION-FRAME#####
		field_info_frame = Frame(info_frame,bd=3,relief=RIDGE,bg=self.bg)
		field_info_frame.place(x=13,y=45,width=535,height=450)

		##SCROLLS##
		x_scroll = Scrollbar(field_info_frame,orient=HORIZONTAL)
		y_scroll = Scrollbar(field_info_frame,orient=VERTICAL)
		###########

		###TABLE###
		self.table = ttk.Treeview(field_info_frame,columns=('roll','name','gender','dob','email','phone'),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
		self.table.heading('roll',text='Roll No.')
		self.table.heading('name',text='Name')
		self.table.heading('gender',text='Gender')
		self.table.heading('dob',text='D.O.B')
		self.table.heading('email',text='Email')
		self.table.heading('phone',text='Phone No.')	
		###########

		##SCROLLS##
		x_scroll.pack(side=BOTTOM,fill=X)
		y_scroll.pack(side=RIGHT,fill=Y)
		x_scroll.config(command =self.table.xview)
		y_scroll.config(command =self.table.yview)	
		###########
		
		#self.TABLE-CONFIGS#
		self.table['show'] = 'headings'
		self.table.column('roll', anchor="center",width=50)
		self.table.column('name', anchor="center",width=120)
		self.table.column('gender', anchor="center",width=90)
		self.table.column('dob', anchor="center",width=90)
		self.table.column('email', anchor="center",width=150)
		self.table.column('phone', anchor="center",width=90)
		self.table.pack(fill=BOTH,expand=1)
		self.table.bind("<ButtonRelease-1>",on_click)
		###############

		#################################

		#################################


win = Tk()
obj = Student(win)
win.mainloop()