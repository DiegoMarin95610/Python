import pytest
from city_function import get_city_country


def test_country_city_name():
    """Prueba de parametrso ciudad, pais"""
    city_country = get_city_country("Cali", "Colombia")
    assert city_country == "Cali, Colombia"


def test_country_city_population():
    """Prueba con ciudad, pais, y poblacion"""
    city_country_population = get_city_country("Cali", "Colombia", 100000)
    assert city_country_population == "Cali, Colombia - 100000"


@pytest.mark.parametrize(
    "city, country, expected",
    [
        ("Cali", "Colombia", "Cali, Colombia"),
        ("Santiago", "Chile", "Santiago, Chile"),
        ("Cdm", "Mexico", "Cdm, Mexico"),
    ],
)
def test_country_city_name_params(city, country, expected):
    assert get_city_country(city, country) == expected


@pytest.mark.parametrize(
    "city, country, population, expected",
    [
        ("Cali", "Colombia", 100000, "Cali, Colombia - 100000"),
        ("Santiago", "Chile", 50000, "Santiago, Chile - 50000"),
        ("Cdm", "Mexico", 459000, "Cdm, Mexico - 459000"),
    ],
)
def test_country_city_name_population_params(city, country, population, expected):

    assert get_city_country(city, country, population) == expected
