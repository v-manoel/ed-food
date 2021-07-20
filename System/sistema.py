def LimparTerminal():
    import os
    print( '\n')
    pause = input('Press any button to continue[...]'.center(150))
    os.system('cls' if os.name == 'nt' else 'clear')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#print((color.BOLD + color.BLUE + '-------- CARDAPIO DO ' + 'BOBS' + ' --------' + color.END).center(150))