email = str(input("Digite seu email: "))
localizar_dominio = email.find('@')
print(f'Domínio do e-mail: {email[localizar_dominio:]}')