import customtkinter

customtkinter.set_appearance_mode("Dark")  # Set the theme to Dark
customtkinter.set_default_color_theme("dark-blue")  # Set the color theme

root = customtkinter.CTk()
root.title("Face Secure Authentication")  # Set window title
root.geometry("640X480")  # Set window size

def program_start():
    from main import main
    main()  

def program_close():
    exit()

def add_user_func():
    from main import add_user
    add_user()
    
# Frame to hold the widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)  # Adjust padding

# Label for title
label = customtkinter.CTkLabel(master=frame, text="Face Secure Authentication", font=("Roboto", 24))
label.pack(pady=12, padx=10)  # Consistent padding

# Button to start the program
button = customtkinter.CTkButton(master=frame, text="Start Program", command=program_start, width=200, height=50)
button.pack(pady=12, padx=10)  # Consistent padding


button2 = customtkinter.CTkButton(master=frame, text="Add User", command=add_user_func, width=200, height=50)
button2.pack(pady=12, padx=10)  # Consistent padding


button2 = customtkinter.CTkButton(master=frame, text="Close Program", command=program_close, width=200, height=50)
button2.pack(pady=12, padx=10)  # Consistent padding
root.mainloop()
