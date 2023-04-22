#importando bibliotecas
import PySimpleGUI as sg

#Criando janelas com Funções
def inicial():
    sg.theme('lightBlue')
    layout = [
        [sg.Text('USUÁRIO:', size = (25,0))],
        [sg.Input('',size = (20,0), font=('Arial', 12), key='-user-')],
        [sg.Text('SENHA:', size = (25,0))],
        [sg.Input('',size = (20,0), font=('Arial', 12), key='-senha-', password_char= "*")],
        [sg.Text()],
        [sg.Button(image_filename='enter0.png', key= '-enter-'), sg.Button(image_filename='sair0.png', key='-sair-')],
        [sg.Button('Cadastre-se', size=(10,2), button_color=('black', 'lightpink'))]]
    layout_image = [[sg.Image(filename='arquivo0.png')]]
    layout = [[sg.Column(layout), sg.Column(layout_image)]]
    return sg.Window('Login', layout= layout, size=(550,300), finalize=True)


def cadastro():
    sg.theme('black')
    layout = [
        [sg.Text('Nome:', size=(25,0))], 
        [sg.Input(size=(25,0))],
        [sg.Text('Senha:', size=(25,0))],
        [sg.Input(size=(25,0), password_char='*')],
        [sg.Text('Confirme sua senha:', size=(25,0))],
        [sg.Input(size=(25,0), password_char='*')],
        [sg.Button(image_filename='enter0.png', key='enterlogin')]]
    foto_layout = [[sg.Image('astrotec0.png')]]
    layout = [[sg.Column(layout), sg.Column(foto_layout)]]
    return sg.Window('Cadastro', layout= layout, size=(450,250), finalize=True)


#Definindo janela inicial
janela1, janela2 = inicial(), None

#Loop de leitura da janela
while True:
    window, eventos, valores = sg.read_all_windows()
               
    #todos os eventos da janela inicial/janela1
    def achando_conta(usuario, senha):
        with open("contas.txt", "r") as arquivo:
            for c in arquivo:
                dados = c.strip().split(',')
                if dados[0] == usuario and dados[1] == senha:
                    return True
            return False
        

    if window == janela1 and eventos == sg.WIN_CLOSED or eventos == '-sair-':
        break
    
    elif window == janela1 and eventos == 'Cadastre-se':
        janela1.hide()
        janela2 = cadastro()

    elif window == janela1 and eventos == '-enter-':
        usuario = valores['-user-']
        senha = valores['-senha-']     
        if achando_conta(usuario, senha):
            sg.popup('Entrando na sua conta.')
        else:
            sg.popup('Usuário e/ou senha estão incorretos. Tente novamente')

    #todos os eventos da janela de cadastro/janela2
    if window == janela2 and eventos == sg.WIN_CLOSED:
        janela2.hide()
        janela1.un_hide()

    def save_conta(nome, senha):
        with open("contas.txt", "a") as cadastro:
            cadastro.write(f'{nome},{senha}\n')
    

    def nome_igual(nome):
        with open("contas.txt", "r") as cadastro:
            for c in cadastro:
                dados = c.strip().split(',')
                if dados[0] == nome:
                    return True
            return False


    if window == janela2 and eventos == 'enterlogin':
        nome = valores[0]
        senha = valores[1]
        confirmar_senha = valores[2]
        
        if nome == senha:
            sg.popup('ATENÇÂO. Nome e senha devem ser diferentes.')
        
        elif len(valores[0]) == 0 or len(valores[1]) == 0 or len(valores[2]) == 0:
            sg.popup('LUGARES EM BRANCO. Preencha todos os campos do Cadastro')
        
        elif len(nome) < 4:
            sg.popup('O Nome deve conter 4 Caracteres no mínimo.')
        
        elif len(senha) < 6:
            sg.popup('Senha deve conter no Mínimo 6 caracteres')

        elif ' ' in nome or ' ' in senha:
            sg.popup('Não são permitidos espaços entre o nome ou senha')
            nome.strip()
            senha.strip()

        elif nome_igual(nome):
            sg.popup('ESSE NOME JÀ EXISTE. Por favor... tente outro nome')

        elif senha == confirmar_senha:
            save_conta(nome, senha)
            sg.popup("SEU CADASTRO FOI REALIZADO COM SUCESSO.")
            janela2.hide()
            janela1.un_hide()
            
        else:
            sg.popup("ERRO DE SENHA. Suas senhas devem ser iguais.")
                
window.close()
