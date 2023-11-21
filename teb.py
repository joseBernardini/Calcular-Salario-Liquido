

import customtkinter
from customtkinter import *
janela = customtkinter.CTk()
custom_font = ("Comic Sans MS", 22)
custom_font2 = ("arial", 18)
custom_font3 = ("Comic Sans MS", 14)

def abrir_janelaesta():
    janela3 = customtkinter.CTkToplevel()
    janela3.geometry("400x600")
    janela3.config()
    janela3.title("Conversor de salário bruto")


    customtkinter.set_appearance_mode("dark")




    Tlabel = customtkinter.CTkLabel(janela3,text="Insira o salário bruto Estatutário ", font=custom_font)
    Tlabel.pack(padx=10, pady=10)


    entrada = customtkinter.CTkEntry(janela3, width=122, placeholder_text="insira o valor bruto")
    entrada.pack(padx=10, pady=10)

    botao = customtkinter.CTkButton(janela3, text="Calcular", font=custom_font2, width=160)
    botao.pack(padx=10, pady=10)




    INSSlabel = customtkinter.CTkLabel(janela3,text="INSS:")
    INSSlabel.place(x=89, y=220)

    INSSentry = customtkinter.CTkEntry(janela3, width=122,)
    INSSentry.place(x=137, y=220)

    IRPFlabel = customtkinter.CTkLabel(janela3,text="IRPF:" )
    IRPFlabel.place(x=89, y=270)

    IRPFentry = customtkinter.CTkEntry(janela3, width=122)
    IRPFentry.place(x=137, y=270)

    FGTSlabel = customtkinter.CTkLabel(janela3,text="FGTS:" )
    FGTSlabel.place(x=85, y=320)

    FGTSentry = customtkinter.CTkEntry(janela3, width=122)
    FGTSentry.place(x=137, y=320)

    SLlabel = customtkinter.CTkLabel(janela3,text="SALÁRIO LIQUIDO:")
    SLlabel.place(x=17, y=370)

    SLentry = customtkinter.CTkEntry(janela3, width=122)
    SLentry.place(x=135, y=370)

    janela3.lift()
    janela3.grab_set()

    janela3.mainloop()
def abrir_janela():
    janela2 = customtkinter.CTkToplevel()
    janela2.geometry("400x600")
    janela2.config()
    janela2.title("Conversor de salário bruto")


    customtkinter.set_appearance_mode("dark")




    Tlabel = customtkinter.CTkLabel(janela2,text="Insira o salário bruto CLT ", font=custom_font)
    Tlabel.pack(padx=10, pady=10)


    entrada = customtkinter.CTkEntry(janela2, width=122, placeholder_text="insira o valor bruto")
    entrada.pack(padx=10, pady=10)

    botao = customtkinter.CTkButton(janela2, text="Calcular", font=custom_font2, width=160)
    botao.pack(padx=10, pady=10)




    INSSlabel = customtkinter.CTkLabel(janela2,text="INSS:")
    INSSlabel.place(x=89, y=220)

    INSSentry = customtkinter.CTkEntry(janela2, width=122,)
    INSSentry.place(x=137, y=220)

    IRPFlabel = customtkinter.CTkLabel(janela2,text="IRPF:" )
    IRPFlabel.place(x=89, y=270)

    IRPFentry = customtkinter.CTkEntry(janela2, width=122)
    IRPFentry.place(x=137, y=270)

    FGTSlabel = customtkinter.CTkLabel(janela2,text="FGTS:" )
    FGTSlabel.place(x=85, y=320)

    FGTSentry = customtkinter.CTkEntry(janela2, width=122)
    FGTSentry.place(x=137, y=320)

    SLlabel = customtkinter.CTkLabel(janela2,text="SALÁRIO LIQUIDO:")
    SLlabel.place(x=17, y=370)

    SLentry = customtkinter.CTkEntry(janela2, width=122)
    SLentry.place(x=135, y=370)


    janela2.lift()
    janela2.grab_set()

    janela2.mainloop()
def abrir_janelacreditos():
    janela4 = customtkinter.CTkToplevel()
    janela4.geometry("400x600")
    janela.config()

    label = customtkinter.CTkLabel(janela4,text="Esta calculadora de salário bruto foi desenvolvida por ", font=custom_font3)
    label.place(x=23, y=10)

    label2 = customtkinter.CTkLabel(janela4,text="José Guilherme, um entusiasta da programação", font=custom_font3)
    label2.place(x=23, y=30)

    label3 = customtkinter.CTkLabel(janela4,text="e apaixonado por criar soluções práticas.", font=custom_font3)
    label3.place(x=23, y=50)

    label4 = customtkinter.CTkLabel(janela4,text="José Guilherme se dedica a fornecer ferramentas ", font=custom_font3)
    label4.place(x=23, y=70)

    label5 = customtkinter.CTkLabel(janela4,text="úteis para facilitar o planejamento de trabalho para ", font=custom_font3)
    label5.place(x=23, y=90)

    label6 = customtkinter.CTkLabel(janela4,text="estatutários e trabalhadores sob o regime CLT. ", font=custom_font3)
    label6.place(x=23, y=110)

    label7 = customtkinter.CTkLabel(janela4,text="A calculadora disponibilizada aqui é uma ferramenta ", font=custom_font3)
    label7.place(x=23, y=150)

    label8 = customtkinter.CTkLabel(janela4,text="versátil que permite calcular o salário bruto,  ", font=custom_font3)
    label8.place(x=23, y=170)

    label9 = customtkinter.CTkLabel(janela4,text="considerando diferentes aspectos, como INSS, IRPF,", font=custom_font3)
    label9.place(x=23, y=190)

    label10 = customtkinter.CTkLabel(janela4,text="FGTS, entre outros. Desenvolvida com a intenção", font=custom_font3)
    label10.place(x=23, y=210)

    label11 = customtkinter.CTkLabel(janela4,text="de simplificar os cálculos relacionados às rotinas,", font=custom_font3)
    label11.place(x=23, y=230)

    label12 = customtkinter.CTkLabel(janela4,text="a calculadora visa fornecer uma experiência", font=custom_font3)
    label12.place(x=23, y=250)

    label13 = customtkinter.CTkLabel(janela4,text="fácil e eficiente para estimar o salário líquido.", font=custom_font3)
    label13.place(x=23, y=270)

    label14 = customtkinter.CTkLabel(janela4,text="Para entrar em contato com o desenvolvedor ou obter", font=custom_font3)
    label14.place(x=23, y=310)

    label15 = customtkinter.CTkLabel(janela4,text="mais informações sobre a calculadora, você pode entrar ", font=custom_font3)
    label15.place(x=23, y=330)

    label16 = customtkinter.CTkLabel(janela4,text="em contato com José Guilherme em ", font=custom_font3)
    label16.place(x=23, y=350)

    label17 = customtkinter.CTkLabel(janela4,text="[jose.guilhermebernadini19@gmail.com].", font=custom_font3)
    label17.place(x=23, y=370)


    


    

    janela4.lift()
    janela4.grab_set()

    janela4.mainloop()





    

janela.geometry("400x600")
botaor = customtkinter.CTkButton(janela, text="Ir para a calculadora do CLT", command=abrir_janela,)
botaor.pack(padx=10, pady=10)

botaor2 = customtkinter.CTkButton(janela, text="Ir para a calculadora do Estatutário", command=abrir_janelaesta,)
botaor2.pack(padx=20, pady=10)

botaorcre = customtkinter.CTkButton(janela, text="créditos", command=abrir_janelacreditos,)
botaorcre.pack(padx=20, pady=10)



janela.mainloop()