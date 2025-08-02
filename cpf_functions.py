import validate_docbr  # Importa a biblioteca responsável por validar e formatar documentos brasileiros, como CPF e CNPJ.

def format_cpf(cpf):
    """
    Formata um CPF não formatado (somente números) para o padrão brasileiro.

    Parâmetros:
        cpf (str): CPF contendo apenas os números (ex: '12345678909').

    Retorna:
        str: CPF formatado com pontos e traço (ex: '123.456.789-09').
    """

    cpf_obj = validate_docbr.CPF()  # Cria uma instância da classe CPF da biblioteca validate-docbr.

    cpf_formatado = cpf_obj.mask(cpf)  # Usa o método mask() para aplicar a máscara de formatação no CPF fornecido.

    return cpf_formatado  # Retorna o CPF formatado.
