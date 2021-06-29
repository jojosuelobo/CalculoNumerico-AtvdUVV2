def chuveirinho(A1, A2):
    x1 = A2 + A1
    x2 = A2 * A1
    return x1, x2


def MMC(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    while True:
        if maior % num1 == 0 and maior % num2 == 0:
            return maior
            break
        else:
            maior += 1

def lagrange(vet, qnt):
    # PARTE 1
    l0S1 = vet[1][0] - 1
    l0S2 = vet[2][0] * -1
    l0S1, l0S2 = chuveirinho(l0S1, l0S2)
    l0I = (vet[0][0] - vet[1][0]) * (vet[0][0] - vet[2][0])

    l1S1 = vet[0][0] - 1
    l1S2 = vet[2][0] - 1
    l1S1, l1S2 = chuveirinho(l1S1, l1S2)
    l1I = (vet[1][0] - vet[0][0]) * (vet[1][0] - vet[2][0])

    l2S1 = vet[0][0] - 1
    l2S2 = vet[1][0] - 1
    l2S1, l2S2 = chuveirinho(l2S1, l2S2)
    l2I = (vet[2][0] - vet[0][0]) * (vet[2][0] - vet[1][0])
    # PARTE 2
    l0S1 = vet[0][1] * l0S1
    l0S2 = vet[0][1] * l0S2
    l0x = vet[0][1] * 1
# lx -> x^2
    l1S1 = vet[1][1] * l1S1
    l1S2 = vet[1][1] * l1S2
    l1x = vet[1][1] * 1

    l2S1 = vet[2][1] * l2S1
    l2S2 = vet[2][1] * l2S2
    l2x = vet[2][1] * 1

    mmc = MMC(l0I, l1I)
    mmc = MMC(mmc, l2I)
    # PARTE 3
    val1 = mmc / l0I
    val2 = mmc / l1I
    val3 = mmc / l2I

    x2P = float((val1 * l0x) + (val2 * l1x) + (val3 * l2x))
    x1P = float((val1 * l0S1) + (val2 * l1S1) + (val3 * l2S1))
    x0P = float((val1 * l0S2) + (val2 * l1S2) + (val3 * l2S2))

    print('RESPOSTA: ')
    print(f'P(x): ({x2P}/{mmc})x^2 + ({x1P}/{mmc})x + ({x0P}/{mmc})')
    x = (x2P/mmc)* (qnt**2)+ (x1P/mmc)*qnt + x0P/mmc
    print(f'P({qnt}): {x}')

def newton(vet, qnt):
    d0 = vet[0][1]
    d1 = (vet[1][1] - d0) / (vet[1][0] - vet[0][0])
    aux = (vet[2][1] - vet[1][1]) / (vet[2][0] - vet[1][0])
    d2 = (aux - d1) / (vet[2][0] - vet[0][0])

    print(f'P(x): {d0} + {d1}(x - {vet[0][0]}) + {d2}(x - {vet[0][0]})(x - {vet[1][0]})')
    #for i in range(qnt):
    x = d0 + (d1*qnt) + (d1*vet[0][0]) + (d2*qnt + (d2*vet[0][0]))*(qnt-vet[1][0])
    print(f'P({qnt}): {x}')

vet = []
# Preenchimento dos vetores
for i in range(3):
    vet.append([0, 0])
for i in range(len(vet)):
    for j in range(len(vet[i])):
        if (j == 1):
            vet[i][j] = float(input(f'Insira o valor de Y na posição (X{i + 1}, Y{i + 1}): '))
        else:
            vet[i][j] = float(input(f'Insira o valor de X na posição (X{i + 1}, Y{i + 1}): '))
# Print de vetores
print(f'Vetores: {vet}')
esc = input('Escolha o metodo a ser usado, (1) = Interpolação de Lagrange, (QUALQUER OUTRA COISA) = Metodo de Newton: ')
qnt = float(input('Informe o valor de X: '))
if(esc == '1'):
    lagrange(vet, qnt)
else:
    newton(vet, qnt)