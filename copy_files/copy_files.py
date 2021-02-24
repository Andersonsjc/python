# coding: iso-8859-1 -*-
from shutil import copy
from os import path, makedirs

#Steps:
#1 - Carregar lista de arquivos e diretórios
#2 - Se diretório não existir no destino, criar
#3 - Verifica se o arquivo existe na origem, se não, mensagem de alerta
#4 - Verifica se o arquivo existe no destino, se sim, mensagem informando que não será copiado novamente
#5 - Se existe na origem, e não existe no destino, realizar a cópia

def start():
    #DE - PARA    
    #from_file_path = '\\\\servername\\files\\'
    #to_copy_path = 'C:\\temp\\copy\\'

    file_name_list = 'D:\\temp\\file_name_full.txt'
    
    
    
    copy_file(file_name_list, from_file_path, to_copy_path)

def copy_file(file_name_list, from_file_path, to_copy_path):
    print(f'Lendo o arquivo = {file_name_list}')
    with open(file_name_list) as list_file:
        for line in list_file:
            file_name = line.split(",")[0]
            dir_name = line.split(",")[1].rstrip('\n')
            destiny_directory = f'{to_copy_path}{dir_name}'
            origin_directory = f'{from_file_path}{dir_name}'

            file_dir_name = f'{origin_directory}\\{file_name}'

            if verify_if_file_exist(file_dir_name):
                #print(f'Arquivo: {file_dir_name}, encontrado!')
                copy_from_origin_to_destiny(file_name, origin_directory, destiny_directory)
            else:
                print('{:-^50}'.format(''))
                print(f'ERRO Arquivo: {file_dir_name}, NAO encontrado!')
            

def if_directory_not_exit_then_created(directory):
    if not path.exists(directory):
        makedirs(directory)
        print(f'Criado diretorio: {directory}')

def copy_from_origin_to_destiny(file_name, origin_directory, destiny_directory):
    if_directory_not_exit_then_created(destiny_directory)
    file_dir_origin = f'{origin_directory}\\{file_name}'
    file_dir_destiny = f'{destiny_directory}\\{file_name}'
    
    if verify_if_file_exist(file_dir_destiny):
        #print(f'  Arquivo: {file_dir_origin} ja existe no destino, NAO sera copiado novamente.')
        nao_faz_nada = ''
    else:
        #print(f'  Iniciando copia do arquivo: {file_dir_origin} para: {file_dir_destiny} ...')
        try:
            copy(file_dir_origin, destiny_directory)
        except Exception as e:
            print('{:-^50}'.format(''))
            print(f'  ERRO ao tentar copiar o arquivo: {file_dir_origin} para: {destiny_directory} => Menssagem de erro: {str(e)}')
        #else:
            #print(f'  SUCESSO na copia do arquivo: {file_dir_origin} para: {destiny_directory} .')

def verify_if_file_exist(file_dir_name):
    return True if path.exists(file_dir_name) else False

if __name__ == "__main__":
    start()
