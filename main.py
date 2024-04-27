import tkinter as tk 
from tkinter import filedialog, messagebox
import os
import shutil


def create_folder(path):
    if not os.path.exists:
        os.makedirs(path)

def move_file(file, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file, destination_folder)
    
def organize(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:].lower()
        
        destination_folder = os.path.join(directory, file_extension)
        
        create_folder(destination_folder)
        
        file_path = os.path.join(directory, file)
        destination_path = os.path.join(destination_folder, file)
        
        move_file(file_path, destination_path)

def browser():
    directory = filedialog.askdirectory()
    if directory:
        organize(directory)
        
def main():
    root = tk.Tk()
    root.title('FileOrganizer')
    
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    
    button_browse = tk.Button(frame, text="Select Directory", command=browser)
    button_browse.pack(fill='x')
    
    root.mainloop()
    
    directory = input("Please enter the path of the directory you want to organize:")
    organize(directory)
    messagebox.showinfo("All files have been succesfully organized!")

if __name__ == "__main__":
    main()

