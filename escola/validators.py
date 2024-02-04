import re
import docbr as dbr

''' def de validação da quantidade de números do CPF'''
def cpf_valido(numero_do_cpf):
   return dbr.validate(numero_do_cpf, doctype='cpf', lazy=False)
     

''' def de validação de nome com apenas letras'''
def nome_valido(nome):
    return nome.isalpha()

''' def de validação da quantidade de números do RG'''
def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

''' def de validação da quantidade de números do Celular'''
def celular_valido(numero_do_celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_do_celular)
    return resposta