#extrator_cep completo e finalizado 

#02 e 04\06Alura- curso String em Python: extraindo informações de uma URL aula 04 e 05 
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
