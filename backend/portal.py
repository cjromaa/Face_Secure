### Individual Portal GUI where individual can update there information 

import customtkinter
from customtkinter import CTkToplevel, CTkLabel, CTkTextbox

customtkinter.set_appearance_mode("Dark")  # Set the theme to Dark
customtkinter.set_default_color_theme("dark-blue")  # Set the color theme

root = customtkinter.CTk()
root.title("Individual Portal")  # Set window title
root.geometry("640X480")  # Set window size

def edit_information():
    def update_info(info_type, entry_widget):
        info = entry_widget.get()
        print(f"{info_type} Information:", info)
        from main import updated_info
        updated_info(info_type, info)
        
    top = customtkinter.CTkToplevel()
    top.title("Update Information")
    top.geometry("660x720")  

    # Scrollable frame setup
    frame_container = customtkinter.CTkFrame(top)
    canvas = customtkinter.CTkCanvas(frame_container)
    scrollbar = customtkinter.CTkScrollbar(frame_container, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # This frame will contain your widgets
    scrollable_frame = customtkinter.CTkFrame(canvas)

    # Place the frame in the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=815)  # Match the width with the window

    # Function to update the scrollregion
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the function to the scrollable frame's configuration event
    scrollable_frame.bind("<Configure>", on_frame_configure)

    # Packing the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    frame_container.pack(fill="both", expand=True)

    # Improved layout using padding and alignment
    def create_section(master, text, placeholder_text):
        label = customtkinter.CTkLabel(master=master, text=text, font=("Roboto", 16))  # Reduced font size
        label.pack(pady=(10, 2), padx=5)  # Reduced padding

        entry = customtkinter.CTkEntry(master=master, placeholder_text=placeholder_text)
        entry.pack(pady=(2, 10), padx=5, fill='x')  # Adjusted padding

        button = customtkinter.CTkButton(master=master, text=text, command=lambda: update_info(text.split(" ")[1], entry), width=180, height=30)  # Smaller button
        button.pack(pady=(5, 10), padx=5)  # Adjusted padding

        return entry

    # Create sections for each information type
    address_info = create_section(scrollable_frame, "Update Address Information", "Address Information")
    age_info = create_section(scrollable_frame, "Update Age Information", "Age Information")
    ethnicity_info = create_section(scrollable_frame, "Update Ethnicity Information", "Ethnicity Information")
    gender_info = create_section(scrollable_frame, "Update Gender Information", "Gender Information")
    major_info = create_section(scrollable_frame, "Update School Major Information", "School Major Information")
    occupation_info = create_section(scrollable_frame, "Update Occupation Information", "Occupation Information")
    phone_info = create_section(scrollable_frame, "Update Phone Number Information", "Phone Number Information")
    school_info = create_section(scrollable_frame, "Update School Information", "School Information")


def exit():
    root.destroy()
    from main import main
    main()

# Frame to hold the widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)  # Adjust padding

# Label for title
label = customtkinter.CTkLabel(master=frame, text="Individual Portal", font=("Roboto", 24))
label.pack(pady=12, padx=10)  # Consistent padding

# Button to start the program
button = customtkinter.CTkButton(master=frame, text="Edit Information", command=edit_information, width=200, height=50)
button.pack(pady=12, padx=10)  # Consistent padding


button2 = customtkinter.CTkButton(master=frame, text="Close Program", command=exit, width=200, height=50)
button2.pack(pady=12, padx=10)  # Consistent padding
root.mainloop()
