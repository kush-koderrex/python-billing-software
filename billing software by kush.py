from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software BY Kush")
        bg_color="#074463"

        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,fg="white",bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        ######################################## VARIABLES ######################################################################

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.sparay=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        #############################################grocry##############################
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        ########################COLD DRINK##########################################
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup= IntVar()
        self.limca= IntVar()
        self.sprite= IntVar()


        ################################# TOTAL PRODUCTS#######################
        self.cosmatic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmatic_tax = StringVar()
        self.grocry_tax = StringVar()
        self.cold_drink_tax = StringVar()



        #################################CUSRTOMER NAME########################3
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.c_search_bill=StringVar()



        ######################################### COSTOMER DETAIL FRAME #################################
        F1=LabelFrame(self.root,text="Custom Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)


        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Customer Phone no",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20)
        c_bill_txt=Entry(F1,width=15,textvariable=self.c_search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        Bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font='arial 12 bold').grid(row=0,column=6,pady=10)

##########################################cosmatic-frame###############################33

        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatics", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5,y=180,width=325,height=370)

        bath_label=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text=Entry(F2,width=10,textvariable=self.soap
                        ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        face_label = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_text = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        face_cream = Label(F2, text="Face wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_text = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        sparay_label = Label(F2, text="Hair spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        sparay_text = Entry(F2, width=10,textvariable=self.sparay, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        gell_label = Label(F2, text="Gell", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        gell_text = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        lotion_label = Label(F2, text="Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        lotion_text = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")

#########################################################Frame-2#####################################################################################3

        F3 = LabelFrame(self.root,bd=10, text="COLD DRINKS", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=370)

        rice_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_text = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")

        fode_oil_label = Label(F3, text="Food_oil", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        fode_oil_text = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        daal_lable = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_text = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        wheat_label = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_text = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        sugar_label = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_text = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        tea_label = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_text = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1,
                                               padx=10,
                                               pady=10,
                                               sticky="w")

        ###########################################################Frame-3############################################################3
        F4 = LabelFrame(self.root,bd=10, text="Cosmatics", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=370)

        maza_label = Label(F4, text="maza", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        maza_text = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")

        cock_label = Label(F4, text="cock", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_text = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        frooti_cream = Label(F4, text="frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_text = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        thumbsup_label = Label(F4, text="thumbsup", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumbsup_text = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        limca_label = Label(F4, text="limca", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_text = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        sprite_label = Label(F4, text="sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_text = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")


####################################################bill area######################################
        F5 =Frame(self.root,relief=GROOVE,bd=10)
        F5.place(x=1010, y=180, width=385, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

################################################button frame###################################
        F6 = LabelFrame(self.root, text="Bill menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl=Label(F6,text="Totala Cosmatic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmatic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Totala Grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Totala Cosmatic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)



        c1_lbl = Label(F6, text="Cosmatic Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmatic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocry_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)


        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold ").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold ").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold ").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold ").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()




    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*40
        self.c_fw_p=self.face_wash.get()*40
        self.c_hs_p=self.sparay.get()*40
        self.c_hg_p=self.gell.get()*40
        self.c_bl_p=self.lotion.get()*40

        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
            )
        self.cosmatic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmatic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get() * 40
        self.g_f_p=self.food_oil.get() * 140
        self.g_d_p=self.daal.get() * 240
        self.g_w_p=self.wheat.get() * 540
        self.g_s_p=self.sugar.get() * 340
        self.g_t_p=self.tea.get() * 240


        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
            )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocry_tax.set("Rs. "+str(self.g_tax))



        self.d_m_p=self.maza.get() * 60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get() * 45
        self.d_t_p=self.thumbsup.get() * 44
        self.d_l_p=self.limca.get() * 45
        self.d_s_p=self.sprite.get() * 40

        self.total_drinks_price = (
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
            )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))


        self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"  UPTRONICS POWER SYSTEM \n")
        self.txtarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        # self.txtarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.txtarea.insert(END,"\n ====================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n ====================================")



    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details are must")

        elif self.cosmatic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected")

        else:

            self.welcome_bill()

            #++++++++++++cosmatics+++++++
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t {self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\n Face Cream\t\t {self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\n Face wash\t\t {self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.sparay.get()!=0:
                self.txtarea.insert(END, f"\n Spray \t\t {self.sparay.get()}\t\t{self.c_s_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END, f"\n Gell \t\t {self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END, f"\n Lotion \t\t {self.lotion.get()}\t\t{self.c_bl_p}")

                # ++++++++++++Cold drinks+++++++
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t {self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t {self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Dall\t\t {self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat \t\t {self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar \t\t {self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea \t\t {self.lotion.get()}\t\t{self.g_t_p}")

                # +++++++++++++++++++
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t {self.maza.get()}\t\t{self.d_m_p}")
            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Cock\t\t {self.cock.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t {self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumpsup \t\t {self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca \t\t {self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite \t\t {self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, "\n ------------------------------------")
            if self.cosmatic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmatics Tax\t\t\t{self.cosmatic_tax.get()}")
            if self.grocry_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocry_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")


            self.txtarea.insert(END, f"\n Total Bill\t\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, "\n ------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. {self.bill_no.get()} saved Succesfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.c_search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalied Bill NO.")


    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data ?")
        if op > 0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.sparay.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            #############################################grocry##############################
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            ########################COLD DRINK##########################################
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            ################################# TOTAL PRODUCTS#######################
            self.cosmatic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmatic_tax.set("")
            self.grocry_tax.set("")
            self.cold_drink_tax.set("")

            #################################CUSRTOMER NAME########################3
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.c_search_bill.set("")


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit ?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()