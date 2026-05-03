# Importando a biblioteca
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação dos níveis (pode alterar os valores)
simulacao = [1, 2, 3, 4, 5]

# Exibição dos níveis com cores
for nivel in simulacao:
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(cor + mensagem)

# Restaura estilo padrão (extra, já que usamos autoreset)
print(Style.RESET_ALL)