import PySimpleGUI as sg
from random import randint

sg.theme('Reddit')   
evento = ''

while evento != 'Não':
    random = randint(1, 6)
    layout = [ 
                [sg.Text("Voce quer rolar o dado?")],
                [sg.Button('Sim'), sg.Button('Não')] ] 
    window = sg.Window('Window Title', layout)

    while True:
        evento, valor = window.read()
        if evento == 'Sim':
    
            layout = [ 
                [sg.Text("O valor do dado é: {}".format(random))],
                [sg.Button('Ok')] ]
            window.close(); del window 
            window = sg.Window('Window Title', layout)     
    
        if evento == sg.WIN_CLOSED or evento == 'Não': 
            break
        if evento == sg.WIN_CLOSED or evento == 'Ok': 
            break

