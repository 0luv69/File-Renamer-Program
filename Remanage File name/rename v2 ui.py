import customtkinter as ctk
import os




class window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode("dark")
        self.geometry("400x400")
        self.title("File Re-manage")
        self.main_div= ctk.CTkFrame(self,fg_color="#4A90E2",corner_radius=0)
        self.main_div.pack(expand=True, fill="both")

        #Variable
        self.file_lists_avi=False


        ctk.CTkLabel(self,text="File Name Re-Manager",text_color="black",
                     font=ctk.CTkFont("Showcard Gothic Regular", 30, "bold"),
                     fg_color="#C6E2FF"
                     ).place(relx=.05,rely=.05,relwidth=.9,relheight=.1)
        self.box()
        self.mainloop()

    def box(self):
        self.selectbtn= ctk.CTkButton(self.main_div, text="Select File",fg_color="green",
                                      cursor="hand2", hover_color="#12372A",
                                      command=self.select_file)
        self.selectbtn.place(relx=.35,rely=.2,relwidth= .3)

        allowed_filetypes = ["png","jpg","jpeg","gif","bmp","ppm","pgm","pbm","pnm","tiff","webp","mp4"]
        self.filetype= ctk.CTkOptionMenu(self.main_div,values=allowed_filetypes )
        self.filetype.place(relx=.4,rely=.3,relwidth= .2)

        self.name_entryframe= ctk.CTkFrame(self.main_div, fg_color="#C6E2FF")
        self.name_entryframe.place(relx=0, rely=.4, relwidth=1, relheight=.1)

        ctk.CTkLabel(self.name_entryframe, text="Name: ",text_color="black"
                     
                     ).pack(side="left",padx=20)
        self.New_name= ctk.CTkEntry(self.name_entryframe,)
        self.New_name.pack(fill="x", pady=6,padx=10)

        self.go_= ctk.CTkButton(self.main_div, text="GO",border_color="#201658",
                                cursor="hand2",hover_color="#2D9596",
                                 border_width=2,fg_color="#FFFACD", text_color="black",
                                 command=self.go)
        self.go_.place(relx=.4, rely=.53, relwidth=.2, relheight= .08)
        self.bind("<Return>",self.go)


    def select_file(self):
        self.path= ctk.filedialog.askdirectory(mustexist=True,title="Select the Image")
        if self.path:
            self.file_lists_avi= True
            self.file_lists = os.listdir(self.path)

    def go(self, *args):
        o=1
        saved_success = False
        if self.file_lists_avi: 
            if self.New_name.get() !="":
                for each_File in self.file_lists:
                    try:
                        file_typetype_check = (each_File.split("."))[-1]
                        if (self.filetype.get()).upper() == file_typetype_check.upper():
                            os.rename((f"{self.path}/{each_File}"),(f"{self.path}/{self.New_name.get()}_{o}.{file_typetype_check}"))
                            o=o+1
                            saved_success= True
                    except Exception as error:
                        print(error)
                        Notification(self,text=error)
                if saved_success:
                    self.file_lists_avi=False
                    Notification(self,text="Success Done", color="green")
            else:
                Notification(self,text="First Plz Type new Name")
        else:
            Notification(self,text="First Select the file PLz")

class Notification(ctk.CTkFrame):
    def __init__(self,window, text, color="red", delay_time=4):
        super().__init__(master=window,fg_color=color,corner_radius=0)
        self.place(relx=.15, rely=.8, relwidth= .85,relheight= .15)

        ctk.CTkLabel(self,text="Notification",
                     font=ctk.CTkFont("Showcard Gothic Regular", 15, "bold"),
                     ).place(relx=.02, rely=.05)
        
        ctk.CTkButton(self, text="❌", fg_color="red", corner_radius=10,
                      hover_color="#FF6262", cursor="hand2",
                      command=self.destroy_bar
                      ).place(relx=.9, rely=0, relwidth= .12)     
        
        ctk.CTkLabel(self,text=f"> {text}",
                     ).place(relx=.03, rely=.4)
        self.bell()
        
        delay_time=delay_time*1000
        self.after(delay_time,self.destroy_bar)

    def destroy_bar(self):self.destroy()    
        
if __name__== "__main__":
    window()