# CRIAR INPUT DE NOTAS
nota1 = float(input('Digite sua Primeira Nota: '))
nota2 = float(input('Digite sua Segunda Nota: '))
nota3 = float(input('Digite sua Terceira Nota: '))

# CRIAR SOMATÓRIA DE MÉDIAS
media = (nota1+nota2+nota3)/3

# APLICAÇÃO DE CONDICIONAIS PARA A APROVAÇÃO

if media >= 5 and media <= 10:
    print(' Aprovado! ')
elif media >= 3 and media <5:
    print('Recuperação')
elif media < 3 and media >=0:
    print('Reprovado')
else:
    print('Notas Invalidas')