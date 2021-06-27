from tkinter import *
from tkinter import ttk

class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            #self["style"] = "TEntry"
            self["foreground"]="#000000"

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            #self["style"] = "Placeholder.TEntry"
            self["foreground"]="#d5d5d5"
root = Tk()

#   declare style variable
s = ttk.Style()
#   assume that classic theme in use
s.theme_use('classic')

#   configure relief
s.configure('Placeholder.TEntry', relief='flat', background="white")
#   lets try to change this structure

s.layout('Placeholder.TEntry', [
    ('Entry.highlight', {
        'sticky': 'nswe',
        'children':
            [('Entry.border', {
                'border': '0',
                'sticky': 'nswe',
                'children':
                    [('Entry.padding', {
                        'sticky': 'nswe',
                        'children':
                            [('Entry.textarea',
                              {'sticky': 'nswe'})]
                    })]
            })]
    })])

user_input = PlaceholderEntry(root, 'USERNAME OR EMAIL', font=("Corbel", 15), foreground="#d5d5d5")
user_input.place(relx=0.18, rely=0.455, width=300, height=24)
