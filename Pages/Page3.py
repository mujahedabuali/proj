
#for make a Book Mark page
import customtkinter as ck
from PIL import Image
from tkinter import ttk
from CTkMessagebox import CTkMessagebox


class page3(ck.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=10)

        self.bookmark_image = ck.CTkImage(Image.open("imags/bookmark.png"),size=(30,30))
        self.label = ck.CTkLabel(self, text=" Book Mark",image=self.bookmark_image,corner_radius=20,compound="left",height=50,font=ck.CTkFont(family="Times New Roman", size=25,weight="bold")) 
        self.label.pack(pady=5)
        
        columns = ('#1')
        self.table = ttk.Treeview(self,columns=columns,height=15, selectmode='browse',show='headings')

        self.table.column("#1", anchor="w",width=100,minwidth=100)
     
        self.table.heading('#1', text='Item')
        self.table.bind('<Motion>','break')

        self.scrollbar = ck.CTkScrollbar(self, orientation=ck.VERTICAL, command=self.table.yview)
        self.scrollbar.pack(side=ck.RIGHT, fill=ck.Y)

        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.table.pack(fill=ck.BOTH, expand=False,padx=15)


        button_frame = ck.CTkFrame(self,fg_color="transparent")
        button_frame.pack(fill=ck.BOTH, expand=False,padx=15,pady=20)

        self.add_button = ck.CTkButton(button_frame, text="Add a new Book Mark", command=self.add_data)
        self.add_button.place(x=200,y=100)

        self.edit_button = ck.CTkButton(button_frame, text="Edit a Book Mark ", command=self.edit_item)
        self.edit_button.place(x=400,y=100)

        self.delete_button = ck.CTkButton(button_frame, text="Delete a Book Mark", command=self.delete_item)
        self.delete_button.place(x=600,y=100)

    def add_data(self):
        self.add_window()

    def add_window(self):
        def get():
            if (self.entry.get()) :
                data = self.entry.get()
                self.table.insert('','end',values=(data))
                self.entry.delete(0,'end')

        new_window = ck.CTkToplevel(self)
        new_window.geometry("400x200")
        new_window.title('Add item')


        center_x = int(750)
        center_y = int(350)
        new_window.geometry(f"+{center_x}+{center_y}")

        entry_label = ck.CTkLabel(new_window,width=200,text="Enter URL:",font=ck.CTkFont(family="Times New Roman", size=18,weight="bold"))
        entry_label.pack(padx=10, pady=10)

        self.entry = ck.CTkEntry(new_window,width=200)
        self.entry.pack(padx=10, pady=10)

        ok_button = ck.CTkButton(new_window, text="OK", command=get)
        ok_button.pack(padx=10, pady=10)

    def edit_item(self):
         selected_item = self.table.focus()
         if selected_item:
            self.edit_window()
         else:  CTkMessagebox(title="Warning Message",message="Select a item Please",icon="warning",fade_in_duration=5)   

    def edit_window(self):
        def get():
            if (self.entry.get()) :
                item = self.table.focus()
                data = self.entry.get()
                self.table.item(item, values=data)
                self.entry.delete(0,'end')

        new_window = ck.CTkToplevel(self)
        new_window.geometry("400x200")
        new_window.title('Edit Book Mark')


        center_x = int(750)
        center_y = int(350)
        new_window.geometry(f"+{center_x}+{center_y}")

        entry_label = ck.CTkLabel(new_window,width=200,text="Enter new URL for Updtae:",font=ck.CTkFont(family="Times New Roman", size=18,weight="bold"))
        entry_label.pack(padx=10, pady=10)

        self.entry = ck.CTkEntry(new_window,width=200)
        self.entry.pack(padx=10, pady=10)

        ok_button = ck.CTkButton(new_window, text="OK", command=get)
        ok_button.pack(padx=10, pady=10)    

    def delete_item(self):
         selected_item = self.table.focus()
         if selected_item:
            self.table.delete(selected_item)
         else:  CTkMessagebox(title="Warning Message",message="Select a item Please",icon="warning",fade_in_duration=5)   
