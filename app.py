import openpyxl
import pyautogui
import time
import datetime
import webbrowser
from urllib.parse import quote

data_hoje = datetime.datetime.now()
data_formatada = data_hoje.strftime("%d/%m")

# Carrega a planilha
workbook = openpyxl.load_workbook('membros.xlsx')
pagina_membros = workbook['Página1']

# Percorre as linhas da planilha
for linha in pagina_membros.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    data_nasc = linha[2].value

    # Verifica se a data de nascimento existe
    if data_nasc is not None:
        data_niver = data_nasc.strftime("%d/%m")

        # Verifica se o aniversário da pessoa é na data de hoje
        if data_niver == data_formatada:
            mensagem = f'Olá {nome},\n\nEspero que esteja bem! Estou passando para lhe desejar um feliz aniversário.\n\nQue você aproveite este dia ao máximo.\nQue Deus te abençoe!'

            #Da inicio ao algoritmo para inicializar o whatsapp web
            try:
                link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
                webbrowser.open(link_mensagem_whatsapp)
                time.sleep(10)
                # Tenta localizar a seta do WhatsApp
                seta = pyautogui.locateCenterOnScreen('seta.png', confidence=0.7)
                
                #Caso encontre a seta, irá realizar o clique e após isso fechar a guia do navegador
                if seta is not None:
                    time.sleep(5)
                    pyautogui.click(seta[0],seta[1])
                    time.sleep(5)
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(5)
                else:
                    print(f"Seta do WhatsApp não encontrada para {nome}. Verifique o print de tela.")

            #Caso ocorrer erro, é descrito em um arquivo CSV para qual membro não foi possível enviar a mensagem
            except Exception as error:
                print(f'Algo deu errado :(\nNão foi possível enviar a mensagem para {nome}. Erro: {error}')
                with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
                    arquivo.write(f'{nome},{telefone},Erro: {error}\n')

    else:
        print(f"Data de nascimento ausente ou inválida para {nome}")
