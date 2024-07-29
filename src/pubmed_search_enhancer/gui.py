import tkinter as tk
from tkinter import messagebox
from .llama3_expander import get_new_terms

class TermExpanderApp:
    """
    A GUI application for expanding terms in different groups.

    Attributes:
        root (tk.Tk): The root window of the Tkinter application.
        groups (dict): Dictionary containing the initial terms for each group.
        all_groups (list): List of all group names.
        current_group_index (int): Index to track the current group being processed.
        new_terms (list): List of new terms generated for the current group.
        selected_terms (dict): Dictionary to store the selected terms for each group.
    """
    def __init__(self, root, groups, all_groups):
        """
        Initialize the TermExpanderApp with the given parameters.

        Parameters:
            root (tk.Tk): The root window of the Tkinter application.
            groups (dict): Dictionary containing the initial terms for each group.
            all_groups (list): List of all group names.
        """
        self.root = root
        self.root.title("Term Expander")
        self.groups = groups
        self.current_group_index = 0
        self.new_terms = []
        self.selected_terms = {group: [] for group in self.groups}
        self.all_groups = all_groups

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        """
        Create and arrange the widgets in the GUI.
        """
        self.group_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.group_label.pack(pady=10)

        self.current_terms_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.current_terms_label.pack(pady=10)

        self.term_frame = tk.Frame(self.root)
        self.term_frame.pack(pady=10)

        self.term_vars = []
        self.term_checkbuttons = []

        self.update_button = tk.Button(self.root, text="See More", command=self.see_more_terms)
        self.update_button.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(self.root, text="Next Group", command=self.next_group)
        self.next_button.pack(side=tk.RIGHT, padx=20)

    def update_display(self):
        """
        Update the display with the current group's terms and generate new terms.
        """
        group_name = list(self.groups.keys())[self.current_group_index]
        self.group_label.config(text=f"Expanding terms for group: {group_name}")

        # Combine initial and selected terms without duplication
        current_terms = list(set(self.groups[group_name] + self.selected_terms[group_name]))
        self.current_terms_label.config(text=f"Current terms for group: {', '.join(current_terms)}")

        self.clear_terms()
        self.new_terms = get_new_terms(group_name, current_terms, self.all_groups)

        for term, explanation in self.new_terms:
            var = tk.IntVar()
            cb = tk.Checkbutton(self.term_frame, text=f"{term} - {explanation}", variable=var)
            cb.pack(anchor=tk.W)
            self.term_vars.append(var)
            self.term_checkbuttons.append(cb)

    def clear_terms(self):
        """
        Clear the terms displayed in the current frame.
        """
        for cb in self.term_checkbuttons:
            cb.destroy()
        self.term_vars.clear()
        self.term_checkbuttons.clear()

    def see_more_terms(self):
        """
        Generate and display more terms for the current group.
        """
        self.update_selected_terms()
        self.update_display()

    def next_group(self):
        """
        Move to the next group and update the display. If all groups are processed, display an info message and quit.
        """
        self.update_selected_terms()
        self.current_group_index += 1
        if self.current_group_index < len(self.groups):
            self.update_display()
        else:
            messagebox.showinfo("Info", "All groups processed")
            self.root.quit()

    def update_selected_terms(self):
        """
        Update the selected terms for the current group based on user input.
        """

        selected_terms = [self.new_terms[i][0] for i, var in enumerate(self.term_vars) if var.get()]
        group_name = list(self.groups.keys())[self.current_group_index]
        self.selected_terms[group_name].extend(selected_terms)
        self.selected_terms[group_name] = list(set(self.selected_terms[group_name]))
        self.groups[group_name].extend(selected_terms)
        self.groups[group_name] = list(set(self.groups[group_name]))

def start_gui(groups, all_groups):
    """
    Start the term expander GUI application.

    Parameters:
        groups (dict): Dictionary containing the initial terms for each group.
        all_groups (list): List of all group names.

    Returns:
        dict: Selected terms for each group after the GUI interaction.
    """
    root = tk.Tk()
    app = TermExpanderApp(root, groups, all_groups)
    root.mainloop()
    return app.selected_terms
