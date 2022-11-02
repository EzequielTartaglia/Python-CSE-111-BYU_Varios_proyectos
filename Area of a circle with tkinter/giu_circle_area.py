
import math
import tkinter as tk
import number_entry as nent


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Tire Volume")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the text fields and the results.
    lbl_ratio = tk.Label(frm_main, text="Aspect Ratio:")

    # Create three text fields.
    ent_radius = nent.FloatEntry(frm_main, 0, 300, width=5)

    # Create a label to display the result.
    lbl_result_label = tk.Label(frm_main,text="Area of a circle: ")
    lbl_result = tk.Label(frm_main, width=8, anchor="e")

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, text fields, and buttons in a grid.
    lbl_ratio.grid( row=1, column=0, padx=3, pady=2, sticky="w")
    ent_radius.grid(row=1, column=1, padx=3, pady=2, sticky="e")
    lbl_result_label.grid(row=2, column=0, padx=3, pady=2, sticky="w")
    lbl_result.grid(row=2, column=1, padx=3, pady=2, sticky="e")
    btn_clear.grid( row=3, column=2, padx=3, pady=2)


    # This function is called each time the user releases a key.
    def calculate(event):
        """Compute the approximate volume of a tire in liters."""
        try:
            # Get the user input.
            #a = π r2
            r = ent_radius.get()
            π = math.pi
            

            # Compute the tire volume in liters.
            area = (π * r * r)

            # Display the volume rounded to one place after
            # the decimal for the for the user to see.
            lbl_result.config(text=f"{area:.1f}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the text fields, clear the result labels.
            lbl_result.config(text="")


    # This function is called each time
    # the user clicks the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        ent_radius.focus()


    # Bind the calculate function to the three text fields
    # so that the calculate function will be called when
    # the user changes the text in the text fields.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_radius.focus()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()