from datetime import date, datetime, timedelta

import pytest

import calculos
from calculos import calcular_idade, dias_para_data_futura


def test_calcular_idade_normal(monkeypatch):
    class DataAtual(date):
        @classmethod
        def today(cls):
            return cls(2024, 6, 15)

    monkeypatch.setattr(calculos, "date", DataAtual)
    assert calcular_idade("1990-12-20") == 33


def test_calcular_idade_aniversario_no_dia(monkeypatch):
    class DataAtual(date):
        @classmethod
        def today(cls):
            return cls(2024, 6, 15)

    monkeypatch.setattr(calculos, "date", DataAtual)
    assert calcular_idade("1990-06-15") == 34


def test_calcular_idade_ano_ainda_nao_completado(monkeypatch):
    class DataAtual(date):
        @classmethod
        def today(cls):
            return cls(2024, 6, 15)

    monkeypatch.setattr(calculos, "date", DataAtual)
    assert calcular_idade("1990-12-20") == 33


@pytest.mark.parametrize("data", ["2024/01/01", "31-01-2024", "texto"])
def test_calcular_idade_com_data_invalida(data):
    with pytest.raises(ValueError):
        calcular_idade(data)


def test_calcular_idade_com_data_nula():
    with pytest.raises(ValueError):
        calcular_idade(None)


def test_calcular_idade_com_nascimento_futuro():
    futura = date.today() + timedelta(days=1)
    with pytest.raises(ValueError):
        calcular_idade(futura)


def test_dias_para_data_futura_normal(monkeypatch):
    class DataAtual(date):
        @classmethod
        def today(cls):
            return cls(2024, 6, 15)

    monkeypatch.setattr(calculos, "date", DataAtual)
    assert dias_para_data_futura("2024-06-20") == 5


def test_dias_para_data_futura_no_dia(monkeypatch):
    class DataAtual(date):
        @classmethod
        def today(cls):
            return cls(2024, 6, 15)

    monkeypatch.setattr(calculos, "date", DataAtual)
    assert dias_para_data_futura("2024-06-15") == 0


@pytest.mark.parametrize("data", ["2024/06/20", "20-06-2024", "texto"])
def test_dias_para_data_futura_com_data_invalida(data):
    with pytest.raises(ValueError):
        dias_para_data_futura(data)


def test_dias_para_data_futura_com_data_nula():
    with pytest.raises(ValueError):
        dias_para_data_futura(None)


def test_dias_para_data_futura_com_data_passada():
    passada = date.today() - timedelta(days=1)
    with pytest.raises(ValueError):
        dias_para_data_futura(passada)
