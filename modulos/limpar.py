def limpar_terminal():
    import os
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/Mac
    else:
        os.system('clear')