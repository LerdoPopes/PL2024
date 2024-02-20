import re 

def cabecalho(linha):
    counter = len(linha.group(1))
    replace = f'<h{counter}>{linha.group(2)}</h{counter}>'
    return replace

def conversor(linha):

    linha = re.sub(r"^(#+)\s(.+)$",cabecalho,linha,flags=re.MULTILINE) #Cabeçalho
    
    linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha) #Bold
    
    linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha) #Itálico
    
    #Esta linha tem que estar acima da do Link pois, graças à sua especificidade, a sua expressão é ignorada caso esteja em baixo.
    linha = re.sub(r"!\[(.*?)\]\((.*?)\)",r'<img src="\2" alt="\1"/>',linha) #Imagem
    
    linha = re.sub(r'\[(.*?)\]\((.*?)\)',r'<a href="\2">\1</a>',linha) #Link 
    
    return linha

if __name__ == "__main__":
    
    while True:    
        print("Insira o texto MarkDown que quer transformar em HTML (Escreva 'lista' se deseja tranformar uma lista numerada)")
        user_input = input()
        
        if user_input == 'lista':
            lista = ""
            while True:
                user_input = input()
                if user_input != "fim":
                    lista += user_input
                    lista += "\n"
                else:
                    html_text = "<ol>\n"
                    html_text += re.sub(r'^(\d+)\.\s(.+)$', r'\n<li>\2</li>', lista,flags=re.M) #Lista Numerada 
                    html_text += '\n</ol>'
                    print(html_text)
                    break
        else:
            output = conversor(user_input) 
            print("Output transformado em HTML:")
            print(output)