import tkinter as tk
from tkinter import messagebox
import random

class ReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem de rezervare online")
        self.geometry("400x300")

        self.current_page = 0
        self.reservation_data = {}

        self.create_widgets()

    def create_widgets(self):
        if self.current_page == 0:
            self.label_welcome = tk.Label(self, text="Bine ați venit la programul de rezervări!")
            self.label_welcome.pack(pady=10)

            self.start_button = tk.Button(self, text="Start", command=self.start_reservation)
            self.start_button.pack(pady=5)
        elif self.current_page == 1:
            self.label = tk.Label(self, text="Alegeți hotelul:")
            self.label.pack(pady=10)

            self.hotels = ["Hotel Ramada", "Hotel Promenada", "Hotel Cismigiu", "Hotel Alice", "Hotel Belvedere"]
            self.selected_hotel = tk.StringVar()
            self.selected_hotel.set(self.hotels[0])

            for hotel in self.hotels:
                tk.Radiobutton(self, text=hotel, variable=self.selected_hotel, value=hotel).pack()

            self.check_availability_button = tk.Button(self, text="Verifică disponibilitatea", command=self.check_availability)
            self.check_availability_button.pack(pady=5)
        elif self.current_page == 2:
            self.label = tk.Label(self, text="Alegeți tipul de cameră:")
            self.label.pack(pady=10)

            self.room_types = ["Apartament", "Camera dublă", "Camera de o persoană"]
            self.selected_room_type = tk.StringVar()
            self.selected_room_type.set(self.room_types[0])

            for room_type in self.room_types:
                tk.Radiobutton(self, text=room_type, variable=self.selected_room_type, value=room_type).pack()

            self.check_room_type_availability_button = tk.Button(self, text="Verifică disponibilitatea", command=self.check_room_type_availability)
            self.check_room_type_availability_button.pack(pady=5)
        elif self.current_page == 3:
            self.label = tk.Label(self, text="Alegeți numărul de persoane:")
            self.label.pack(pady=10)

            self.person_options = ["O persoană", "Cuplu", "Familie cu 1 copil", "Familie cu 2 copii"]
            self.selected_person = tk.StringVar()
            self.selected_person.set(self.person_options[0])

            for person_option in self.person_options:
                tk.Radiobutton(self, text=person_option, variable=self.selected_person, value=person_option).pack()

            self.check_person_availability_button = tk.Button(self, text="Verifică disponibilitatea", command=self.check_person_availability)
            self.check_person_availability_button.pack(pady=5)
        elif self.current_page == 4:
            self.label = tk.Label(self, text="Alegeți etajul:")
            self.label.pack(pady=10)

            self.floor_options = ["Parter", "Etaj 1", "Etaj 2", "Etaj 3", "Etaj 4", "Etaj 5"]
            self.selected_floor = tk.StringVar()
            self.selected_floor.set(self.floor_options[0])

            for floor_option in self.floor_options:
                tk.Radiobutton(self, text=floor_option, variable=self.selected_floor, value=floor_option).pack()

            self.next_button = tk.Button(self, text="Următoarea pagină", command=self.next_page)
            self.next_button.pack(pady=5)
        elif self.current_page == 5:
            self.label = tk.Label(self, text="Alegeți metoda de plată:")
            self.label.pack(pady=10)

            self.payment_methods = ["Mastercard", "Visa", "Tichete vacanță"]
            self.selected_payment_method = tk.StringVar()
            self.selected_payment_method.set(self.payment_methods[0])

            for payment_method in self.payment_methods:
                tk.Radiobutton(self, text=payment_method, variable=self.selected_payment_method, value=payment_method).pack()

            self.next_button = tk.Button(self, text="Confirmare", command=self.confirm_reservation)
            self.next_button.pack(pady=5)

    def start_reservation(self):
        self.current_page = 1
        self.clear_widgets()
        self.create_widgets()

    def next_page(self):
        if self.current_page == 1:
            self.reservation_data["Hotel"] = self.selected_hotel.get()
        elif self.current_page == 2:
            self.reservation_data["Tip cameră"] = self.selected_room_type.get()
        elif self.current_page == 3:
            self.reservation_data["Persoane"] = self.selected_person.get()
        elif self.current_page == 4:
            self.reservation_data["Etaj"] = self.selected_floor.get()

        self.current_page += 1
        self.clear_widgets()
        self.create_widgets()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def confirm_reservation(self):
        self.reservation_data["Metodă plată"] = self.selected_payment_method.get()
        details = "\n".join([f"{key}: {value}" for key, value in self.reservation_data.items()])
        messagebox.showinfo("Rezervare finalizată", f"Rezervarea a fost realizată cu succes!\n\nDetalii rezervare:\n{details}")
        self.reset()

    def reset(self):
        self.reservation_data = {}
        self.current_page = 0
        self.clear_widgets()
        self.create_widgets()

    def check_availability(self):
        selected_hotel = self.selected_hotel.get()
        # Simulăm verificarea disponibilității
        # Presupunem că numărul de camere disponibile este un număr aleator între 1 și 10
        num_rooms_available = random.randint(1, 57)
        messagebox.showinfo("Disponibilitate camere", f"Hotelul {selected_hotel} are {num_rooms_available} camere disponibile.")
        # Adăugăm un buton "OK" sub mesajul de disponibilitate
        self.ok_button = tk.Button(self, text="OK", command=self.next_page)
        self.ok_button.pack(pady=5)

    def check_room_type_availability(self):
        selected_room_type = self.selected_room_type.get()
        # Simulăm verificarea disponibilității
        # Presupunem că numărul de camere disponibile pentru tipul de cameră este un număr aleator între 1 și 5
        num_rooms_available = random.randint(1, 18)
        messagebox.showinfo("Disponibilitate tip cameră", f"Tipul de cameră {selected_room_type} are {num_rooms_available} camere disponibile.")
        # Adăugăm un buton "OK" sub mesajul de disponibilitate
        self.ok_button = tk.Button(self, text="OK", command=self.next_page)
        self.ok_button.pack(pady=5)

    def check_person_availability(self):
        selected_person = self.selected_person.get()
        # Simulăm verificarea disponibilității
        # Presupunem că numărul de camere disponibile pentru numărul de persoane este un număr aleator între 1 și 4
        num_rooms_available = random.randint(1, 70)
        messagebox.showinfo("Disponibilitate număr persoane", f"Numărul de persoane {selected_person} are {num_rooms_available} camere disponibile.")
        # Adăugăm un buton "OK" sub mesajul de disponibilitate
        self.ok_button = tk.Button(self, text="OK", command=self.next_page)
        self.ok_button.pack(pady=5)

if __name__ == "__main__":
    app = ReservationApp()
    app.mainloop()
