import fonction as fonc
from tkinter import * 
from tkinter import ttk
import tkinter.font as font

conn = fonc.database()


# select_all = conn.select_all("carte_fidelite")
# show_all_database = conn.show_all_database()
# list_value = [3,10]
# # insert_table_once = conn.insert_table_once("carte_fidelite",list_value)
# update_once_withID = conn.update_once_withID("carte_fidelite",2,"point",190,"id_carte")
# select_with_id = conn.select_with_id("categorie",2,"id_categorie","nom_categorie")
# print (select_with_id)

class gui():

    #初始化
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        
    def set_init_window(self):
        #窗口标题
        self.init_window_name.title("Resto")
        #窗口大小
        self.init_window_name.geometry('1920x1080')  
        #背景颜色
        self.init_window_name["bg"] = "white"
        #透明度
        self.init_window_name.attributes("-alpha",0.9) 

        self.font_button = font.Font(family='Courier',size=15,weight="bold")

        self.init_window_name.maxsize(1920,1080)
        self.init_window_name.minsize(1920,1080)
        self.init_menu()
        
    def set_element(self):
        self.init_canvas_menu()

    def init_menu(self):
        mb = Menu(self.init_window_name)
        main_menu = Menu(mb,tearoff=False)
        
        main_menu.add_command(label="Connexion",command=self.login)  
        main_menu.add_command(label="Inscription",command=self.inscription) 
        main_menu.add_separator()
        main_menu.add_command(label="Déconnexion",command=self.Signout)
        mb.add_cascade(label='Menu',menu=main_menu)

        exit_menu = Menu(mb,tearoff=False)
        exit_menu.add_command(label="Test",command=self.test)
        exit_menu.add_command(label="Quitter",command=self.exit)
        mb.add_cascade(label="Quitter",menu=exit_menu)
            

        self.init_window_name.config(menu=mb)   
        
    def init_canvas_menu(self): 
        self.canvas = Canvas(self.init_window_name,bg="gray",height=1080-5,width=1920*0.1)
        self.canvas.place(x=0,y=0)
        self.button_x = 2
        self.button_y = 10
        self.button_width = 1920*0.1
        self.button_heigth = 40
        self.button_gap = 10
        photo_sandwich = PhotoImage(Image.open("C:\Users\pc\OneDrive\桌面\tp\photo\sandwich.jpg"))
        self.button_sand = Button(self.init_window_name,
            text="Sandwich",
            bg="white",
            font=(self.font_button),
            fg="black",
            activebackground="gray",
            bd=0,
            image=photo_sandwich
            )
        self.button_sand.place(
            x=self.button_x,
            y=self.button_y+40*0+self.button_gap*0,
            width=self.button_width,
            height=self.button_heigth)
        self.button_sand = Button(self.init_window_name,
            text="Boissons",
            bg="white",
            font=(self.font_button),
            fg="black",
            activebackground="gray",
            bd=0
            )
        self.button_sand.place(
            x=self.button_x,
            y=self.button_y+40*1+self.button_gap*1,
            width=self.button_width,
            height=self.button_heigth)
        self.button_sand = Button(self.init_window_name,
            text="Dessert",
            bg="white",
            font=(self.font_button),
            fg="black",
            activebackground="gray",
            bd=0
            )
        self.button_sand.place(x=self.button_x,
        y=self.button_y+40*2+self.button_gap*2,
        width=self.button_width,
        height=self.button_heigth)
            

    def test(self):
        width = self.init_window_name.winfo_width()
        print(width)    

    def login(self):
        print("Login")

    def exit(self):
        exit()

    def inscription(self):
        print("inscription")    

    def Signout(self):
        print("Sign out")    


def gui_start():
    init_window = Tk()
    new_gui = gui(init_window)
    new_gui.set_init_window()
    new_gui.set_element()
    init_window.mainloop()
    

gui_start()    