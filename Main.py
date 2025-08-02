import re  # Importa o módulo 're' para usar expressões regulares
from cpf_functions import format_cpf  # Importa a função de formatação do CPF de outro arquivo

# Solicita ao usuário que digite um CPF (pode conter pontos e traços)
cpf_digitado = input('CPF: ')

# Remove qualquer caractere que não seja número (isso garante que o CPF fique só com os dígitos)
cpf_formatado = re.sub(r'[^0-9]', '', cpf_digitado)

# Pega os 9 primeiros dígitos do CPF (parte que será usada para calcular os dígitos verificadores)
cpf = cpf_formatado[:9]

# Calcula a soma dos produtos dos 9 dígitos pelos multiplicadores de 10 até 2
soma_do_cpf1 = sum(int(digito) * multiplicador
                   for multiplicador, digito in zip(range(10, 1, -1), cpf))

# Calcula o primeiro dígito verificador
primeiro_digito = (soma_do_cpf1 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador vira 0 (regra do CPF)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Junta os 9 dígitos originais com o primeiro dígito verificador
cpf_segundo_d = cpf + str(primeiro_digito)

# Calcula a soma dos produtos dos 10 dígitos (incluindo o primeiro dígito verificador)
# pelos multiplicadores de 11 até 2
soma_do_cpf2 = sum(int(digito) * multiplicador
                   for multiplicador, digito in zip(range(11, 1, -1), cpf_segundo_d))

# Calcula o segundo dígito verificador
segundo_digito = (soma_do_cpf2 * 10) % 11
# Se o resultado for maior que 9, o dígito verificador vira 0
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# Monta o CPF completo com os dois dígitos verificadores calculados
cpf = cpf + str(primeiro_digito) + str(segundo_digito)

# Compara o CPF calculado com o CPF digitado (sem pontos/traços)
# Se forem iguais, o CPF é válido; senão, inválido
print(f'O CPF {format_cpf(cpf)} é válido') if cpf == cpf_formatado \
    else print(f'O CPF {format_cpf(cpf)} é invalido')

