# Exercicio Pratico de Testes Unitarios

Projeto Python com duas funcoes de calculo de datas e testes unitarios usando pytest.

## Funcionalidades

- `calcular_idade(data_nascimento)`: calcula a idade a partir de uma data de nascimento.
- `dias_para_data_futura(data_futura)`: informa quantos dias faltam para uma data futura.
- `dias_desde_data_passada(data_passada)`: informa quantos dias se passaram desde uma data passada.

As datas podem ser informadas como `datetime.date`, `datetime.datetime` ou string no formato `YYYY-MM-DD`.

## Instalacao

```bash
python -m pip install -r requirements.txt
```

## Executando os testes

```bash
python -m pytest
```
