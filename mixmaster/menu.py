# This file is part of Cantera. See License.txt in the top-level directory or
# at http://www.cantera.org/license.txt for license and copyright information.

import sys

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


def make_menu(name, menu_bar, menu_items):
    button = tk.Menubutton(menu_bar, text=name, padx=3, pady=1)
    button.pack(side=tk.LEFT, anchor=tk.W)
    menu = tk.Menu(button, tearoff=tk.FALSE)
    for entry in menu_items:
        if entry == 'separator':
            menu.add_separator({})
        elif isinstance(entry, list):
            for num in entry:
                menu.entryconfig(num, state=tk.DISABLED)
        elif not isinstance(entry[1], list):
            if len(entry) == 2 or entry[2] == 'command':
                menu.add_command(label=entry[0], command=entry[1])
            elif entry[2] == 'check':
                entry[3].set(0)
                if len(entry) >= 5:
                    val = entry[4]
                else:
                    val = 1
                menu.add_checkbutton(label=entry[0], command=entry[1], variable=entry[3],
                                     onvalue=val)
            else:
                submenu = make_menu(entry[0], menu, entry[1])
                menu.add_cascade(label=entry[0], menu=submenu)

    button['menu'] = menu
    return button