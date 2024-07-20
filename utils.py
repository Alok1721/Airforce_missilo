from tkinter import Toplevel, Label
from tkinter import *
import ttkbootstrap as ttk
def create_label(frame, text, font, row, col, sticky="w", padx=10, pady=5):
    label = Label(frame, text=text, font=font)
    label.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
    return label
def add_scrollbar(frame):
        canvas = Canvas(frame)
        v_scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=v_scrollbar.set)
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
        canvas.bind_all("<Shift-MouseWheel>", lambda event: canvas.xview_scroll(int(-1*(event.delta/120)), "units")) 
        return canvas, scrollable_frame

def show_about(root):
        about_window = Toplevel(root)
        about_window.geometry("900x600")
        about_window.rowconfigure(0,weight=1)
        about_window.columnconfigure(0,weight=1)
        about_window.title("About")
        _,about_window=add_scrollbar(about_window)
        about_window.columnconfigure(0,weight=1)

        runway_info_label_frame=LabelFrame(about_window,bg="red",borderwidth=1)
        runway_info_label_frame.grid(row=0,column=0,sticky="nsew")
        parking_info_label_frame=LabelFrame(about_window,bg="red",borderwidth=1)
        parking_info_label_frame.grid(row=1,column=0,sticky="nsew")
        status_info_label_frame=LabelFrame(about_window,bg="red",borderwidth=1)
        status_info_label_frame.grid(row=2,column=0,sticky="nsew")
        
        graph_display_info_label_frame=LabelFrame(about_window,bg="red",borderwidth=1)
        graph_display_info_label_frame.grid(row=3,column=0,sticky="nsew")
        
        playground_info_label_frame=LabelFrame(about_window,bg="red",borderwidth=1)
        playground_info_label_frame.grid(row=4,column=0,sticky="nsew")
        

        # runway_info_label_frame.rowconfigure(0,weight=1)
        # runway_info_label_frame.columnconfigure(0,weight=1)
        create_label(runway_info_label_frame, "1. How to give input (RUNWAY):", ("Helvetica", 16, "bold underline"), row=0, col=0)
        create_label(runway_info_label_frame, "1.1: CEP: Circular error probability (probability circle for impact point)", ("Helvetica", 10, "italic"), row=1, col=0)
        create_label(runway_info_label_frame, "1.2: Submunition dispersal radius: Spread of submunition after impact", ("Helvetica", 10, "italic"), row=2, col=0)
        create_label(runway_info_label_frame, "1.3: MOS: Minimum width & height to work normally", ("Helvetica", 10, "italic"), row=3, col=0)
        create_label(runway_info_label_frame, "1.4: No of Submunitions: no of sumunition inside one missile", ("Helvetica", 10, "italic"), row=4, col=0)
        create_label(runway_info_label_frame, "1.5: Damage radius: radius where missile destroy the area completly", ("Helvetica", 10, "italic"), row=5, col=0)
        create_label(runway_info_label_frame, "1.6: Runway width: dynamic width of runway", ("Helvetica", 10, "italic"), row=6, col=0)

        create_label(parking_info_label_frame, "2. How to give input (Parking):", ("Helvetica", 16, "bold underline"), row=0, col=0)
        create_label(parking_info_label_frame, "2.1: CEP: Circular error probability (probability circle for impact point)", ("Helvetica", 10, "italic"), row=1, col=0)
        create_label(parking_info_label_frame, "2.2: Submunition dispersal radius: Spread of submunition after impact", ("Helvetica", 10, "italic"), row=2, col=0)
        create_label(parking_info_label_frame, "2.3: MOS: Minimum width & height to work normally", ("Helvetica", 10, "italic"), row=3, col=0)
        create_label(parking_info_label_frame, "2.4: No of Submunitions: no of sumunition inside one missile", ("Helvetica", 10, "italic"), row=4, col=0)
        create_label(parking_info_label_frame, "2.5: Damage radius: radius where missile destroy the area completly", ("Helvetica", 10, "italic"), row=5, col=0)
        create_label(parking_info_label_frame, "2.6: Parking width: dynamic width of parking", ("Helvetica", 10, "italic"), row=6, col=0)

        create_label(status_info_label_frame, "3. How to use Current status:", ("Helvetica", 16, "bold underline"), row=0, col=0)
        create_label(status_info_label_frame, "3.1: Status: RED -for runway/parking is not destroy yet \n GREEN -runwat/parking is destroy", ("Helvetica", 10, "italic"), row=1, col=0)
        create_label(status_info_label_frame, "3.2: Missiles: it will count ,how much missile needed to destroy the runway/parking", ("Helvetica", 10, "italic"), row=2, col=0)
        create_label(status_info_label_frame, "3.3: Submutions: it will count totale submunitions hit the area", ("Helvetica", 10, "italic"), row=3, col=0)
        create_label(status_info_label_frame, "3.4: Hori cut: it will check ,horizontally runway mos destroy or not", ("Helvetica", 10, "italic"), row=4, col=0)
        create_label(status_info_label_frame, "3.5: Vert cut: it will check ,vertically runway mos destroy or not", ("Helvetica", 10, "italic"), row=5, col=0)
        
        create_label(graph_display_info_label_frame, "4. How to give input of Display_graph:", ("Helvetica", 16, "bold underline"), row=0, col=0)
        create_label(graph_display_info_label_frame, "4.1: 5 Cep: 5 different cep values for to check ,how many missile needed to destroy the area completely", ("Helvetica", 10, "italic"), row=1, col=0)
        create_label(graph_display_info_label_frame, "4.2: No of missile: how much missile users want to strike to aim area", ("Helvetica", 10, "italic"), row=2, col=0)
        create_label(graph_display_info_label_frame, "4.3: No of iteration: it will tell you how much iteration needed for each simulation", ("Helvetica", 10, "italic"), row=3, col=0)
        create_label(graph_display_info_label_frame, "4.4: SIMULATIOM: it will display graph ", ("Helvetica", 10, "bold"), row=4, col=0)
        
        create_label(playground_info_label_frame, "5. How to work on playground:", ("Helvetica", 16, "bold underline"), row=0, col=0)
        create_label(playground_info_label_frame, "5.1: you have to click on AIM(+) point to hit the target.it will give next target \n and everytime it will check runway/parking area completly destroy or not", ("Helvetica", 10, "italic"), row=1, col=0)
        create_label(playground_info_label_frame, "5.2: horizontal cut will green if no more horizontal area left for safe flight similarily for vertical cut", ("Helvetica", 10, "italic"), row=2, col=0)
       



        