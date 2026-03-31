# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """Retorna la cantidad total de letras."""
    return count_vowels(text) + count_consonants(text)


def vowel_percentage(text):
    """Retorna el porcentaje de vocales sobre el total de letras."""
    total = total_letters(text)
    
    if total == 0:
        return 0.0
    
    vowels = count_vowels(text)
    porcentaje = (vowels / total) * 100
    
    return round(porcentaje, 1)


def analyze_text(text):
    """Retorna el string formateado."""
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)
    
    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"
