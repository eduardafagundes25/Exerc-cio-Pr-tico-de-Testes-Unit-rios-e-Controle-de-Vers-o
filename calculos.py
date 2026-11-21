from datetime import date, datetime


def _converter_data(valor, nome):
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    if isinstance(valor, str):
        try:
            return datetime.strptime(valor, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"{nome} deve estar no formato YYYY-MM-DD") from None
    raise ValueError(f"{nome} deve ser uma data válida")


def calcular_idade(data_nascimento):
    """Calcula a idade em anos a partir da data de nascimento."""
    nascimento = _converter_data(data_nascimento, "Data de nascimento")
    hoje = date.today()

    if nascimento > hoje:
        raise ValueError("A data de nascimento não pode ser futura")

    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade


def dias_para_data_futura(data_futura):
    """Retorna quantos dias faltam até uma data futura."""
    futura = _converter_data(data_futura, "Data futura")
    hoje = date.today()

    if futura < hoje:
        raise ValueError("A data informada não pode estar no passado")

    return (futura - hoje).days


def dias_desde_data_passada(data_passada):
    """Retorna quantos dias se passaram desde uma data passada."""
    passada = _converter_data(data_passada, "Data passada")
    hoje = date.today()

    if passada > hoje:
        raise ValueError("A data informada não pode estar no futuro")

    return (hoje - passada).days
