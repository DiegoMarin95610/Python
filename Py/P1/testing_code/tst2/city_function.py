def get_city_country(city, country, population="") -> str:

    full_address = (
        f"{city}, {country} - {population}" if population else f"{city}, {country}"
    )
    return full_address.title()
