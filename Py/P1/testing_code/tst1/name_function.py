def get_formatted_name(f_name, l_name, m_name="") -> str:
    full_name = f"{f_name} {m_name} {l_name}" if m_name else f"{f_name} {l_name}"
    return full_name.title()
