#-*-coding:UTF-8-*-

def start():
    lista = ['a', 'b', 'c']
    mapa = map(fun_print, lista)
    print(list(mapa))

def fun_print(text):
    print(f'Texto = {text}')
    return False if text == 'b' else True

if __name__ == "__main__":
    start()