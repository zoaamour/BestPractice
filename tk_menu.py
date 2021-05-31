import tkinter as tk


class MenuExample:

    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, width=25)
        self.label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        self._create_menubar()

    def _create_menubar(self):
        # create the menubar
        self.menubar = tk.Menu(self.root)
        self.root.configure(menu=self.menubar)

        # File menu
        fileMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Exit", command=self.root.destroy)

        # View menu
        viewMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="Input", command=self.switch_to_input)
        viewMenu.add_command(label="Sell", command=self.switch_to_sell)

    def switch_to_input(self):
        # put the code to switch to the input page here...
        self.label.configure(text="you clicked on View->Input")

    def switch_to_sell(self):
        # put the code to switch to the sell page here...
        self.label.configure(text="you clicked on View->Sell")


app = MenuExample()
tk.mainloop()
