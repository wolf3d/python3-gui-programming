import tkinter as tk
from tkinter import ttk

# tkinter widget exploration

class WidgetExplorer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.entry_value = tk.StringVar()
        self.spinbox_value = tk.DoubleVar()
        self.combobox_value = tk.StringVar()       
        self.checkbutton_value = tk.BooleanVar()

        # widgets
        label_frame = ttk.LabelFrame(self, text="Explore widgets")
        my_entry = ttk.Entry(label_frame, textvariable=self.entry_value)
        my_spinbox = ttk.Spinbox(label_frame, from_=0.5, to=52.0, increment=.01, textvariable=self.spinbox_value)
        my_combobox = ttk.Combobox(label_frame, textvariable=self.combobox_value, values=["Option A","Option B","Option C"])
        my_checkbutton = ttk.Checkbutton(label_frame, text="Check to make this option True", variable=self.checkbutton_value)
        my_textwidget = tk.Text(label_frame)
        my_button = ttk.Button(label_frame, textvariable=self.entry_value, command=self.swaptext)

        # widget placement
        label_frame.grid(row=0, column=0, sticky=(tk.E + tk.W + tk.N + tk.S))
        my_entry.grid(row=0, column=0, sticky=tk.W)
        my_spinbox.grid(row=0, column=1, sticky=tk.W)        
        my_textwidget.grid(row=1, column=0, sticky=tk.W)
        my_combobox.grid(row=1, column=1, sticky=tk.W)        
        my_checkbutton.grid(row=2, column=0, sticky=tk.W)
        my_button.grid(row=2, column=0, columnspan=3)

    def swaptext(self):
        if self.entry_value.get() == 'Hi':
            self.entry_value.set('There')
        else:
            self.entry_value.set('Yo!')


class MyApplication(tk.Tk):
    """main application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Widget Explorer")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        WidgetExplorer(self).grid(row=0, column=0)
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()