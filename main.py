from tkinter import *
from functions import *


Fee = 0.00
gbp_amount = 0.00
currency = ""
Total = 0
is_staff= ""


window = Tk()
window.geometry("720x620")


gbp_entrybox = Entry(text = "")
gbp_entrybox.place(x = 130, y = 70, width = 120, height = 25)

title1 = Label(window, text = "Currency converter")
title1.place(x = 190, y = 10)

title2 = Label(window, text = "Amount of GBP:")
title2.place(x = 110, y = 40)


def set_gbp():
    global gbp_amount
    tmp_gbp = gbp_entrybox.get()
    gbp_amount = float(tmp_gbp)
    gbp_entrybox["bg"] = "grey"
    print(gbp_amount)


button1 = Button(text = "Set GBP amount" , command = set_gbp)
button1.place(x = 260, y = 70, width = 120, height = 25)

currency_entrybox = Entry(text = "")
currency_entrybox.place(x = 130, y = 210, width = 120, height = 25)


def set_currency():
    tmp = currency_entrybox.get()
    currency = str(tmp)

    response_1 = converter(currency, gbp_amount)
    convert_result = Label(window, text=response_1)
    convert_result.place(x=150, y=300, width=200, height=25)

    response_2 = fee_calculation(gbp_amount)
    fee_result = Label(window, text=f"Transaction fee: {response_2}")
    fee_result.place(x=150, y=320, width=200, height=25)

    response_3 = staff_verification(is_staff, response_2, gbp_amount)
    staff_result = Label(window, text=f"Total: {response_3}")
    staff_result.place(x=150, y=340, width=200, height=25)


title3 = Label(window, text="Convert to:")
title3.place(x=110, y=180)

button2 = Button(text="Convert", command=set_currency)
button2.place(x=260, y=210, width=120, height=25)

title4 = Label(window, text="Are you a member of staff?")
title4.place(x=110, y=110)


def aff_click():
    global is_staff
    is_staff = "yes"


def neg_click():
    global is_staff
    is_staff = "no"


aff_button = Button(text="Yes", command=aff_click)
aff_button.place(x=130, y=140, width=50, height=25)
neg_button = Button(text="No", command=neg_click)
neg_button.place(x=190, y=140, width=50, height=25)


infotxt1 = Label(window, text="Available currencies:\n"
                              "\n USD - US Dollar\n"
                              " EUR - Euro\n"
                              " BRL - Brazilian real\n"
                              " JPY - Japanese Yen\n"
                              " TRL - Turkish Lira")
infotxt1.place(x=400, y=50, width=300, height=100)

window.mainloop()




