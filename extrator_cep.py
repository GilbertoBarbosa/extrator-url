endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, 23440-120, RJ"

# Regular Extression -- RegEx
import re

# 5 dígitos + hifen (opcional) + 3 dígitos

# Quantificadores: {5}
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match

if busca:
    cep = busca.group()
    print(cep)