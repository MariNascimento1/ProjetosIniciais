# Código ANSI para Reset (remove todas as formatações)
RESET = "\033[0m"

# Estilos de Texto
NEGRITO = "\033[1m"
OPACO = "\033[2m"
ITALICO = "\033[3m"
SUBLINHADO = "\033[4m"
PISCAR = "\033[5m"
REVERSO = "\033[7m"
OCULTO = "\033[8m"

# Cores do Texto (Fore)
PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
PADRAO_TEXTO = "\033[39m"

# Cores de Fundo (Back)
FUNDO_PRETO = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL = "\033[44m"
FUNDO_MAGENTA = "\033[45m"
FUNDO_CIANO = "\033[46m"
FUNDO_BRANCO = "\033[47m"
FUNDO_PADRAO = "\033[49m"

# Cores Brilhantes (Texto e Fundo)
PRETO_BRILHANTE = "\033[90m"
VERMELHO_BRILHANTE = "\033[91m"
VERDE_BRILHANTE = "\033[92m"
AMARELO_BRILHANTE = "\033[93m"
AZUL_BRILHANTE = "\033[94m"
MAGENTA_BRILHANTE = "\033[95m"
CIANO_BRILHANTE = "\033[96m"
BRANCO_BRILHANTE = "\033[97m"

FUNDO_PRETO_BRILHANTE = "\033[100m"
FUNDO_VERMELHO_BRILHANTE = "\033[101m"
FUNDO_VERDE_BRILHANTE = "\033[102m"
FUNDO_AMARELO_BRILHANTE = "\033[103m"
FUNDO_AZUL_BRILHANTE = "\033[104m"
FUNDO_MAGENTA_BRILHANTE = "\033[105m"
FUNDO_CIANO_BRILHANTE = "\033[106m"
FUNDO_BRANCO_BRILHANTE = "\033[107m"

# Exemplo de uso para cada um
# print(f"{SUBLINHADO}Texto sublinhado{RESET}")
# print(f"{NEGRITO}Texto em negrito{RESET}")
# print(f"{ITALICO}Texto em itálico (se suportado){RESET}")
# print(f"{PISCAR}Texto piscando (se suportado){RESET}")
# print(f"{REVERSO}Texto com cores invertidas{RESET}")

# print(f"{VERMELHO}Texto vermelho{RESET}")
# print(f"{FUNDO_VERDE}Texto com fundo verde{RESET}")
# print(f"{AZUL_BRILHANTE}Texto azul brilhante{RESET}")
# print(f"{FUNDO_MAGENTA_BRILHANTE}Texto com fundo magenta brilhante{RESET}")
