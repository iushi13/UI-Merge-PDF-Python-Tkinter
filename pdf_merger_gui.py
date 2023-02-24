import tkinter as tk
from tkinter import filedialog, messagebox
import ntpath
from pdf_merger_logic import merge_pdfs


class PDFMergerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger")

        # Create GUI elements
        self.filepaths = []
        self.filelistbox = tk.Listbox(self.master, height=5)
        self.filelistbox.config(width=50)
        self.add_button = tk.Button(self.master, text="Add Files", command=self.add_files, bg='#2c3e50', fg='#ecf0f1', padx=10, pady=5)
        self.merge_button = tk.Button(self.master, text="Merge Files", command=self.merge_files, bg='#2c3e50', fg='#ecf0f1', padx=10, pady=5)
        self.clear_button = tk.Button(self.master, text="Clear Files", command=self.clear_files, bg='#2c3e50', fg='#ecf0f1', padx=10, pady=5)

        # Place GUI elements
        self.filelistbox.pack()
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.merge_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_files(self):
        # Open file dialog to select PDF files
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

        # Add selected files to listbox
        for file in files:
            self.filepaths.append(file)
            self.filelistbox.insert(tk.END, ntpath.basename(file))

    def merge_files(self):
        # Save merged file
        savepath = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")])

        try:
            merge_pdfs(self.filepaths, savepath)
            messagebox.showinfo(title="Success", message="Merging successful!")
        except Exception as e:
            messagebox.showerror(title="Error", message="An error occurred while merging the files.")

    def clear_files(self):
        # Clear listbox and filepaths list
        self.filelistbox.delete(0, tk.END)
        self.filepaths = []
