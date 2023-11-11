import os
import time
import datetime
from PIL import Image, ImageTk
import customtkinter

raw_datetime = datetime.datetime.now()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
local_time = time.localtime()
current_time = time.strftime("%H:%M:%S", local_time)
current_date = datetime.date.today()
current_path = os.path.dirname(os.path.realpath(__file__))
reports = []

def corruptionScan():
    if os.path.isfile(r"reports.txt"):
        pass
    else:
        with open(r"reports.txt", 'x') as f:
            f.write("")

def read_runtimereports(path):
    webpages = []
    with open(path, 'r') as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                line.replace('127.0.0.1',' ')
                webpages.append(line)
    return(webpages)

corruptionScan()
reports=read_runtimereports(f"{current_path}/addresses.sv")
reports_string = ''

for index in reports:
    reports_string = reports_string + f"{index}\n"
print(reports_string)

class UI(customtkinter.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.login_frame = customtkinter.CTkFrame(self, bg_color= "black")
        self.login_frame.grid(row=0)
        login_image = ImageTk.PhotoImage(Image.open(current_path + r"/images/web.png"))
        self.fake_button_image = customtkinter.CTkButton(self.login_frame, text="", image = login_image, width=20, height=20, fg_color="#883cdc", hover_color="#883cdc")
        self.fake_button_image .grid(row=0, column=0, padx=15, pady=(10, 0))
        
        self.banner = customtkinter.CTkLabel(self.login_frame, text="Blocked Websites loaded;\nAll listed sites are currently being blocked.",
                                                 font=customtkinter.CTkFont(size=10))
        self.banner.grid(row=1, column=0, padx=15, pady=(9, 0))
        
        self.information = customtkinter.CTkLabel(self.login_frame, text=f"{current_date} - {current_path}",
                                                 font=customtkinter.CTkFont(size=10))
        self.information.grid(row=2, column=0, padx=15, pady=(0, 1))

        self.information_tags = customtkinter.CTkLabel(self.login_frame, text="[redirecting]                 [name] ",
                                                 font=customtkinter.CTkFont(size=12))
        self.information_tags.grid(row=3, column=0, padx=15, pady=(0, 2))

        self.loaded_reports = customtkinter.CTkLabel(self.login_frame, text=f"{reports_string}",
                                                 font=customtkinter.CTkFont(size=12))
        self.loaded_reports.grid(row=4, column=0, padx=15, pady=(0, 0))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.login_frame = UI(master=self, width=340, height=130)
        self.login_frame.grid(row=0, column=0, padx=20, pady=20)
        self.title("SENTRY - Blacklisted Webpages")
        self.resizable(False, False)

app = App()
app.mainloop()