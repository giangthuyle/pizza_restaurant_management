import tkinter as tk


class AdditionalInfoView(tk.Toplevel):

    def __init__(self, parent, title="Additional Information for Order", size='500x500+300+300'):
        super().__init__(parent)
        self.title(title)
        self.geometry(size)

        delivery_title = tk.Label(self, text="Delivery Methods:", font=("Arial", 12, "bold"))
        delivery_title.pack(pady=10)

        self.delivery_var = tk.StringVar()
        self.delivery_var.set("Delivery")
        delivery_radiobutton = tk.Radiobutton(self, text="Delivery", variable=self.delivery_var, value="Delivery",
                                              command=self.toggle_delivery)
        delivery_radiobutton.pack()
        takeaway_radiobutton = tk.Radiobutton(self, text="Takeaway", variable=self.delivery_var, value="Takeaway",
                                              command=self.toggle_delivery)
        takeaway_radiobutton.pack()

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self, state=tk.DISABLED)
        self.address_entry.pack()
        self.pickup_label = tk.Label(self, text="Pickup Time:")
        self.pickup_label.pack()
        self.pickup_entry = tk.Entry(self, state=tk.DISABLED)
        self.pickup_entry.pack()

        # Title: Group Booking
        group_booking_title = tk.Label(self, text="Is there a group booking associated with your order?",
                                       font=("Arial", 12, "bold"))
        group_booking_title.pack(pady=10)
        self.group_booking_var = tk.StringVar()
        self.group_booking_var.set("No")
        group_booking_yes_radiobutton = tk.Radiobutton(self, text="Yes", variable=self.group_booking_var, value="Yes",
                                                       command=self.toggle_group_booking)
        group_booking_yes_radiobutton.pack()
        group_booking_no_radiobutton = tk.Radiobutton(self, text="No", variable=self.group_booking_var, value="No",
                                                      command=self.toggle_group_booking)
        group_booking_no_radiobutton.pack()
        self.booking_code_label = tk.Label(self, text="Please enter your group booking code:")
        self.booking_code_label.pack()
        self.booking_code_entry = tk.Entry(self, state=tk.DISABLED)
        self.booking_code_entry.pack()

        # Title: Employee Discount
        employee_discount_title = tk.Label(self, text="Are you an employee at Yummy Pizza?", font=("Arial", 12, "bold"))
        employee_discount_title.pack(pady=10)
        self.employee_discount_var = tk.StringVar()
        self.employee_discount_var.set("No")
        employee_discount_yes_radiobutton = tk.Radiobutton(self, text="Yes", variable=self.employee_discount_var,
                                                           value="Yes", command=self.toggle_employee_discount)
        employee_discount_yes_radiobutton.pack()
        employee_discount_no_radiobutton = tk.Radiobutton(self, text="No", variable=self.employee_discount_var,
                                                          value="No",
                                                          command=self.toggle_employee_discount)
        employee_discount_no_radiobutton.pack()
        self.employee_card_label = tk.Label(self, text="Please enter your employee card number:")
        self.employee_card_label.pack()
        self.employee_card_entry = tk.Entry(self, state=tk.DISABLED)
        self.employee_card_entry.pack()

        # Process Payment Button
        payment_button = tk.Button(self, text="Process Payment by Card")
        payment_button.pack()

    def toggle_delivery(self):
        if self.delivery_var.get() == "Delivery":
            self.address_label.config(state=tk.NORMAL)
            self.address_entry.config(state=tk.NORMAL)
            self.pickup_label.config(state=tk.DISABLED)
            self.pickup_entry.config(state=tk.DISABLED)
        else:
            self.address_label.config(state=tk.DISABLED)
            self.address_entry.delete(0, tk.END)
            self.address_entry.config(state=tk.DISABLED)
            self.pickup_label.config(state=tk.NORMAL)
            self.pickup_entry.config(state=tk.NORMAL)

    def toggle_group_booking(self):
        if self.group_booking_var.get() == "Yes":
            self.booking_code_label.config(state=tk.NORMAL)
            self.booking_code_entry.config(state=tk.NORMAL)
        else:
            self.booking_code_label.config(state=tk.DISABLED)
            self.booking_code_entry.delete(0, tk.END)
            self.booking_code_entry.config(state=tk.DISABLED)

    def toggle_employee_discount(self):
        if self.employee_discount_var.get() == "Yes":
            self.employee_card_label.config(state=tk.NORMAL)
            self.employee_card_entry.config(state=tk.NORMAL)
        else:
            self.employee_card_label.config(state=tk.DISABLED)
            self.employee_card_entry.delete(0, tk.END)
            self.employee_card_entry.config(state=tk.DISABLED)
