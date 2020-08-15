from tkinter import *
from tkinter import messagebox as mb
import csv

root = Tk()

# open root centered ===
wigth = 800
height = 500
root.title('Calculate Your Body Mass Index')
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
positionX = width_screen / 2 - wigth / 2
positionY = height_screen / 2 - height / 2
root.geometry("%dx%d+%d+%d" % (200, 500, positionX, positionY))
root.resizable(False, False)


def new_screen():
    if var_kg or var_cm != 0:
        root.geometry("%dx%d" % (1000, height))
        print('USER: Access the BMI result >new screen<')


# === open the last screen and show up details ==============
def mb_txt(txt, soma):
    # == les than 18.5 Underweight ==
    if txt <= 18.5:
        resul_label['text'] = 'Underweight'
        resul_label['bg'] = 'light blue'
        frame_final['bg'] = 'sky blue'
        resul_label['fg'] = 'black'
        resul_label.place(x=50, y=430)
        final_result['text'] = soma
        new_screen()
        mb.showinfo('BMI of less than 18.5',
                    'A BMI of less than 18.5 indicates that you are underweight, so you may need to put on some '
                    'weight. '
                    'You are recommended to ask your doctor or a dietitian for advice.')
    # == between 18.5 and 24.9 has Normal ==
    if txt >= 18.5:
        if txt <= 24.9:
            resul_label['text'] = 'Normal'
            resul_label['bg'] = 'green'
            resul_label.place(x=70, y=430)
            frame_final['bg'] = 'green3'
            final_result['text'] = soma
            new_screen()
            mb.showinfo('BMI of 18.5–24.9',
                        'A BMI of 18.5-24.9 indicates that you are at a healthy weight for your height. By maintaining'
                        ' a healthy weight, you lower your risk of developing serious health problems.')
    # == between 25 and 29.9 is Overweight ==
    if txt >= 25:
        if txt <= 29.9:
            resul_label['text'] = 'Overweight'
            resul_label['bg'] = 'red'
            frame_final['bg'] = 'red4'
            resul_label.place(x=55, y=430)
            final_result['text'] = soma
            new_screen()
            mb.showinfo('BMI of 25–29.9',
                        'A BMI of 25-29.9 indicates that you are slightly overweight. You may be advised to lose some '
                        'weight for health reasons. You are recommended to talk to your doctor or a dietitian for '
                        'advice.')
    # == more than 30 obse ==
    if txt >= 30:
        resul_label['text'] = 'OBESE'
        resul_label['bg'] = 'black'
        resul_label['fg'] = 'white'
        frame_final['bg'] = 'grey18'
        resul_label.place(x=75, y=430)
        final_result['text'] = soma
        new_screen()
        mb.showinfo('BMI of over 30',
                    'A BMI of over 30 indicates that you are heavily overweight. Your health may be at risk if you do '
                    'not lose weight. You are recommended to talk to your doctor or a dietitian for advice.')


def calculation():
    # try
    if stone_entry.get() == '':
        var_stone.set(0)
    if feet_entry.get() == '':
        var_feet.set(0)
    if pounds_entry.get() == '':
        var_pounds.set(0)
    if inches_entry.get() == '':
        var_inches.set(0)
    if kg_entry.get() == '':
        var_kg.set(0)
    if cm_entry.get() == '':
        var_cm.set(0)

    calculation_button.place(x=150, y=3700000)
    calculation_button2.place(x=150, y=370)

    # Getting "Inches, Pounds, stones and feet" to convert to BMI
    if var_inches.get() and var_pounds.get() or var_stone.get() and var_feet.get() != 0:
# ====== Stones and pounds MATH AND CONVERT TO KG =================
        stone = var_stone.get()
        pounds = var_pounds.get()
        total_pounds = (stone * 14) + pounds
        print(f'total de pounds {total_pounds}')

        total_kg = int(total_pounds * 0.45359237)
        kg_entry.delete(0, END)
        kg_entry.insert(END, total_kg)

# ======= Feet and inches MATH AND CONVERT TO CM ===============
        feet = var_feet.get()
        inches = var_inches.get()
        total_inches = (feet * 12) + inches

        total_Cm = (total_inches * 2.54) / 100
        final_cm = '%.2f' % total_Cm
        cm_entry.delete(0, END)
        cm_entry.insert(END, final_cm)

        """soma = 703 * (total_pounds / (total_inches * total_inches))
        somafinal = float('%.1f' % soma)
        bmi_entry.delete(0, END)
        bmi_entry.insert(END, soma)
        print(f'USER: Imperial method BMI {somafinal}')"""

    if var_kg.get() and var_cm.get() != 0:
# ======= KG and Cm MATH CONVERTER to BMI result===============
        k1 = var_kg.get()
        c2 = var_cm.get()
        soma = k1 / (c2 ** 2)

        somafinal = float('%.1f' % soma)
        bmi_entry.delete(0, END)
        bmi_entry.insert(END, somafinal)

# ====== Convert Cm to feet and inches =======
        resultado = c2 * 3.28084
        feet_entry.delete(0, END)
        inches_entry.delete(0,END)
        resultadofeet = '%.1d' % resultado
        resultadoinches = str(resultado)
        feet_entry.insert(END, resultadofeet)
        inches_entry.insert(END, resultadoinches[3])

# ====== Covert Kg to stones and pounds =======

        soma2 = k1 / 6.35029318
        stone11 = '%.1d' % soma2
        stone_entry.delete(0, END)
        stone_entry.insert(END, stone11)

        recorte2  = str(soma2)
        fo2 = recorte2.split('.')
        print(fo2[1])
        fo3 = int(fo2[1])
        f = int(fo3) * 14
        ff = str(f)

        #print(f'stones {s}, pounts {f}')
        if len(ff) <= 16 :
            recorte = str(f)
            pounds_entry.delete(0, END)
            pounds_entry.insert(END, recorte[0:1])
        elif len(ff) >= 17:
            recorte = str(ff)
            fo2 = recorte[0:2]
            fo3 = int(fo2)
            if fo3 <= 14:
                pounds_entry.delete(0, END)
                pounds_entry.insert(END, recorte[0:2])
            else:
                pounds_entry.delete(0, END)
                pounds_entry.insert(END, recorte[0:1])

        print(f'USER: kGs {var_kg.get()} and Cm {c2} to BMI {somafinal}')

        mb_txt(somafinal, somafinal)


def reset_button_frame_right():
    calculation_button.place(x=150, y=370)
    calculation_button2.place(x=150, y=3700000)
    reset_frame_right()


def reset_frame_right():
    var_cm.set(0)
    var_kg.set(0)
    var_inches.set(0)
    var_pounds.set(0)
    var_feet.set(0)
    var_stone.set(0)
    bmi_entry.delete(0, END)
    calculation_button2.place(x=150, y=3700000)
    calculation_button.place(x=150, y=370)


def startprogram():
    reset_frame_right()
    name = name_entry.get()

    if len(name) <= 2:
        mb.showerror('Error', 'Name has insufficient characters')
        print('USER: Error >Name has insufficient characters<')

    else:
        print('USER: Program Started')

        root.geometry("%dx%d" % (wigth, height))

        email_label.place(x=15, y=100)
        email_entry.place(x=15, y=130)
        bmi_label.place(x=5, y=220)
        bmi_entry.place(x=125, y=220)
        M_radion_button.place(x=15, y=180)
        F_radion_button.place(x=55, y=180)
        save2_button.place(x=70, y=260)
        start_button.place(x=70, y=385000)
        reset_button.place(x=55, y=385)

        def back():
            root.geometry('200x500')
            info_button.place(x=45, y=430)
            email_entry.place(x=1000, y=1000)
            email_label.place(x=1000, y=1000)
            back_button.place(x=1000, y=1000)
            F_radion_button.place(x=1000, y=1000)
            M_radion_button.place(x=1000, y=1000)
            info_button.place(x=45, y=430)
            bmi_entry.place(x=15, y=1000)
            bmi_label.place(x=15, y=1000)

            save2_button.place(x=70, y=2600000)
            start_button.place(x=70, y=385)
            reset_button.place(x=70, y=3850000)
            print('USER: Back to home page')

        back_button = Button(frame_left, text='Back', width=10, font=('Century Ghotic', 15), relief='raised', bd=5,
                             command=back)
        back_button.place(x=45, y=430)


def info():
    top = Toplevel()
    top.title('INFO')
    top.resizable(False, False)
    bl = Label(top, image=image_info)
    bl.pack()


def classif():
    top2 = Toplevel()
    top2.title('INFO')
    top2.resizable(False, False)
    bl2 = Label(top2, image=image_classif)
    bl2.pack()


def save():
    # salvar tres item ( nome , email, f/m, bmi )
    email = var_email.get()
    name = var_name.get()
    gender = v.get()
    bmi = var_bmi.get()

    if name == '' or email == '':
        mb.showerror('Error', 'There was an issue with some informations')
        print('USER: Error save >missing informations<')
        var_email.set('')
        var_name.set('')

    elif gender == 0:
        mb.showerror('Error', 'There was not gender informations')
        print('USER: Error save >missing informations<')

    else:
        question = mb.askyesno('Submit',
                               'You are about to enter the fallowing data:' + '\n' + 'Name ' + name + '\n' + 'Email ' + email)

        if question == YES:
            with open('custumerBMI.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, email, gender, bmi])
                print('USER: Saved')
                var_email.set('')
                var_name.set('')
                v.set(0)
            csvfile.close()
        else:
            var_email.set('')
            var_name.set('')
            v.set(0)


# MENU ======
MenuFrame = Frame(root, bg='gray60')
MenuFrame.pack(fill=X)
menuBotton = Menubutton(MenuFrame, text='BMI Programa')
menuBotton.pack(side=LEFT)

fileMenu1 = Menu(menuBotton, tearoff=0)
menuBotton['menu'] = fileMenu1
fileMenu1.add_command(label='Results', command=classif)
fileMenu1.add_command(label='Info', command=info)

# ===== FONT =======
font = ('arial', 18)  # font= labels
font2 = ('Century Ghotic', 25)  # font= bottons
color = 'dodger blue'
font3 = ('arial', 18)
font4 = ('Century Ghotic', 18)
font5 = ('arial', 15)
# ====== Igame =====
image = PhotoImage(file='photo2.png')
image_info = PhotoImage(file='info.png')
image_classif = PhotoImage(file='classification.png')
image_po = PhotoImage(file='po.png')

# ===== FRAME LEFT =====================================================================================================
frame_left = Label(root, width=200, height=height, image=image_po, bg='black', borderwidth=5, relief='solid')
frame_left.pack(side=LEFT)
# ==== Labels ========
name_label = Label(frame_left, text='Name')
name_label.place(x=15, y=20)
email_label = Label(frame_left, text='Email')
email_label.place(x=15, y=18000)

bmi_label = Label(frame_left, text='Your BMI is  = ', font=('Century Ghotic', 15))
bmi_label.place(x=15, y=260000)

var_name = StringVar()
name_entry = Entry(frame_left, width=17, bg='bisque', borderwidth=1, textvariable=var_name)
name_entry.place(x=15, y=50)
# ==== ENTRYS RIGHT ========
var_email = StringVar()
email_entry = Entry(frame_left, width=17, bg='bisque', borderwidth=1, textvariable=var_email)
email_entry.place(x=15, y=21000)

var_bmi = StringVar()
bmi_entry = Entry(frame_left, width=5, textvariable=var_bmi)
bmi_entry.place(x=15, y=29000)

# ===== FRAME RIGHT ====================================================================================================
frame_right = Label(root, width=590, height=height, image=image, borderwidth=5, relief='solid')
frame_right.pack(side=LEFT)
# ==== Labels RIGHT ========

width_label = Label(frame_right, text='Enter your Weight', font=font2, bg=color, fg='bisque', relief='solid')
width_label.place(x=200, y=55)
height_label = Label(frame_right, text='Enter Your Height', font=font2, bg=color, fg='bisque', relief='solid')
height_label.place(x=200, y=235)

stone_label = Label(frame_right, text='Stones', font=font, bg=color, fg='bisque', relief='solid')
stone_label.place(x=15, y=125)
feet_label = Label(frame_right, text='Feet', font=font, bg=color, fg='bisque', relief='solid')
feet_label.place(x=32, y=305)

pounds_label = Label(frame_right, text='Pounds', font=font, bg=color, fg='bisque', relief='solid')
pounds_label.place(x=205, y=125)
inches_label = Label(frame_right, text='Inches', font=font, bg=color, fg='bisque', relief='solid')
inches_label.place(x=215, y=305)

kg_label = Label(frame_right, text='or KGs', font=font, bg=color, fg='white', relief='solid')
kg_label.place(x=395, y=125)
cm_label = Label(frame_right, text='or CM', font=font, bg=color, fg='bisque', relief='solid')
cm_label.place(x=400, y=305)

ex = Label(frame_right, text='EX= 1.60', bg='bisque', relief='solid', borderwidth=3)
ex.place(x=470, y=335)

# ==== ENTRYS RIGHT ========
var_stone = DoubleVar()
var_feet = DoubleVar()
stone_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_stone)
stone_entry.place(x=90, y=120)
feet_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_feet)
feet_entry.place(x=90, y=300)

var_pounds = DoubleVar()
var_inches = DoubleVar()
pounds_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_pounds)
pounds_entry.place(x=285, y=120)
inches_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_inches)
inches_entry.place(x=290, y=300)

var_kg = DoubleVar()
var_cm = DoubleVar()
kg_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_kg)
kg_entry.place(x=470, y=120)
cm_entry = Entry(frame_right, width=7, font=font, bg='bisque', borderwidth=1, textvariable=var_cm)
cm_entry.place(x=470, y=300)

# ===== FRAME FINAL ====================================================================================================
frame_final = Label(root, width=200, height=height, bg='indian red', borderwidth=5, relief='solid')
frame_final.pack(side=LEFT)
# ==== Labels FINAL========
values_label = Label(frame_final, text='BMI VALUES', font=('arial', 25), borderwidth=3, relief='raised', bg='bisque')
values_label.place(x=15, y=20)

under_label = Label(frame_final, text='Underweight', bg='light blue', borderwidth=3, relief='raised')
under_label.place(x=45, y=70)
less_label = Label(frame_final, text='less than 18.5', bg='light blue', borderwidth=3, relief='raised')
less_label.place(x=40, y=100)

normal_label = Label(frame_final, text='Normal', bg='green', borderwidth=3, relief='raised')
normal_label.place(x=65, y=140)
between1_label = Label(frame_final, text='Between 18.5 and 24.9', bg='green', borderwidth=3, relief='raised')
between1_label.place(x=15, y=170)

over_label = Label(frame_final, text='Overweight', bg='red', fg='white', borderwidth=3, relief='raised')
over_label.place(x=50, y=210)
between2_label = Label(frame_final, text='Between 25 and 29.9', bg='red', fg='white', borderwidth=3, relief='raised')
between2_label.place(x=20, y=240)

obese_label = Label(frame_final, text='Obese', bg='black', fg='white', borderwidth=3, relief='raised')
obese_label.place(x=70, y=280)
greater_label = Label(frame_final, text='30 or greater', bg='black', fg='white', borderwidth=3, relief='raised')
greater_label.place(x=50, y=310)

final_result = Label(frame_final, text='00.00', width=7, height=1, bg='bisque', font=('arial', 35))
final_result.place(x=20, y=370)

resul_label = Label(frame_final, text='overweight', bg='black', fg='white', borderwidth=3, relief='raised')
resul_label.place(x=60, y=430)
# ============== Button ================================================================================================
calculation_button = Button(frame_right, text='Calculation Your BMI Now', font=font2, relief='raised', bd=5, fg='black',
                            command=calculation)
calculation_button.place(x=150, y=370)
calculation_button2 = Button(frame_right, text='Calculation Reset BMI Now', font=font2, relief='raised', bd=5,fg='black',
                            command=reset_button_frame_right)
save_button = Button(frame_right, text='Save', font=('Century Ghotic', 18), relief='raised', bd=5, fg='black', width=10,
                     command=save)
save_button.place(x=450, y=430)

save2_button = Button(frame_left, text='Save', font=('Century Ghotic', 15), relief='raised', bd=5, fg='black', width=10,
                      command=save)
save2_button.place(x=70, y=2600000)

start_button = Button(frame_left, text='Start', font=font2, relief='raised', bd=5, command=startprogram)
start_button.place(x=70, y=385)

reset_button = Button(frame_left, text='Reset', width=5, font=font2, relief='raised', bd=5, command=reset_frame_right)

info_button = Button(frame_left, text='Info', width=10, font=('Century Ghotic', 15), relief='raised', bd=5,
                     command=info)
info_button.place(x=45, y=430)
# Radion Button ========================================================================================================
v = IntVar()
M_radion_button = Radiobutton(frame_left, text='M', variable=v, value=1)
M_radion_button.place(x=60, y=33000)
F_radion_button = Radiobutton(frame_left, text='F', variable=v, value=2)
F_radion_button.place(x=100, y=33000)

root.mainloop()
