import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Jacket Measurement Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    create_interface(frm_main)
    root.mainloop()

def create_interface(frm_main):
    labels = ["Talle (cm):", "Largo (cm):", "Encuentro (cm):", "Largo de Manga (cm):", "Pecho (cm):", "Cintura (cm):", "Cadera (cm):"]
    entries = []  # To store the entry widgets
    
    # Create the Labels, Entries and their position
    for i, label_text in enumerate(labels):
        lbl = Label(frm_main, text=label_text, anchor="e")  # Aligned to the right
        ent = IntEntry(frm_main, width=4)  # Use IntEntry for integer input
        lbl.grid(row=i, column=0, padx=3, pady=3, sticky="e")
        ent.grid(row=i, column=1, padx=3, pady=3)
        entries.append(ent) # To append the entries in the entries Array

    def calculate_measurements_proportions():
        # Proportions
        SEXTO = 1/6
        CUARTO = 1/4
        TERCIO = 1/3
        MITAD = 1/2
        COSTURA = 0.75
        CRUCE = 2.5
        FIT_CINTURA= 1.75
        ALTURA_CADERA = 18

        # Measurements
        talle = entries[0].get()
        largo = entries[1].get()
        encuentro = entries[2].get()
        largo_manga = entries[3].get()
        pecho = entries[4].get()
        cintura = entries[5].get()
        cadera = entries[6].get()
        profundidad_sisa = CUARTO * pecho + CUARTO * talle + 1

        # Back jacket measures [esp]
        a_esp = encuentro + 1
        b_esp = SEXTO * pecho + 0.5
        c_esp = CUARTO * b_esp
        d_esp = MITAD * c_esp
        e_esp = CUARTO * profundidad_sisa
        f_esp = e_esp - 2.5
        g_esp = TERCIO * cadera + 1

        # Front jacket measures [del]
        a_del = CUARTO * pecho
        b_del = SEXTO * pecho + 1.5
        c_del = TERCIO * b_del
        d_del = a_del + 3
        e_del = e_esp
        f_del = cadera - g_esp + 4
        angulo_hombro = b_del / c_del

        # For example:
        result = f'''
        Espalda:
        1: {b_esp:.1f} cm
        2: {c_esp:.1f} cm
        3: {d_esp:.1f} cm
        4: {e_esp:.1f} cm
        5: {f_esp:.1f} cm
        6: {g_esp:.1f} cm

        Delantero:
        1: {a_del:.1f} cm
        2: {b_del:.1f} cm
        3: {c_del:.1f} cm
        4: {d_del:.1f} cm
        5: {f_del:.1f} cm
        '''
        
        # Update the output label with the results
        output_result.config(text=result)
    
    # Create the Button and Output Label and their position
    btn_calculate = Button(frm_main, text="Calculate", command=calculate_measurements_proportions)
    btn_calculate.grid(row=len(labels), column=0, padx=3, pady=3, columnspan=2)

    output_label = Label(frm_main, text="Jacket Measurements:")
    output_label.grid(row=len(labels) + 1, column=0, padx=(3, 0), pady=3, sticky="e")

    output_result = Label(frm_main, text="")
    output_result.grid(row=len(labels) + 1, column=1, padx=0, pady=3, sticky="w")


if __name__ == "__main__":
    main()