import re 

def check_password_strength(password: str):
    """
    Classifica a força da senha:
    - Fraca: < 6 caracteres ou só letras/números
    - Média: >= 6 caracteres, inclui letras e números
    - Forte: >= 8 caracteres, inclui letras, números e caracteres especiais
    """
    
    length = len(password)
    
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    if length < 6:
        return "Fraca"
    elif length >= 6 and (has_lower or has_upper) and has_digit and not has_special:
        return "Média"
    elif length >= 8 and has_lower and has_upper and has_digit and has_special:
        return "Forte"
    else:
        return "Fraca"

    
def main():
    print("=== Password Strength Checker ===")
    senha = input("Digite uma senha para testar: ")
    print(f"A senha '{senha}' é: {check_password_strength(senha)}")

if __name__ == "__main__":
    main()    