from name_function import get_formatted_name

def test_first_last_name():
    """Prueba para nombre y apellido sin el middle name.    """
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == "Janis Joplin"   
def test_first_last_middle_name():
    """Prueba para nombre completo."""
    formatted_name = get_formatted_name('janis', 'joplin', 'raquel')
    assert formatted_name == "Janis Raquel Joplin"        
