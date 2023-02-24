import tkinter as tk
from pdf_merger_gui import PDFMergerGUI

if __name__ == "__main__":
    # Create Tkinter window and run mainloop
    root = tk.Tk()
    root.configure(bg='#ecf0f1')
    pdf_merger_gui = PDFMergerGUI(root)
    root.mainloop()
