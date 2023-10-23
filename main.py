# Rafael Cristofali - RM553521

print('Bem-Vindo a Vinheria Agnello!')
endereco = input('Digite seu endereço: ')
ano_nasc = int(input('Digite o ano do seu nascimento: '))
if ((2023 - ano_nasc) < 18):
    print('Venda não permitida para menores de idade!')
else:
    print('Há 3 opções de garrafas de vinho da casa:\nTinto - R$ 10,00\nBranco - R$ 15,00\nRosé - R$ 20,00')
    qtd_tinto = int(input('Quantas garrafas você quer de vinho tinto? '))
    qtd_branco = int(input('Quantas garrafas você quer de vinho branco? '))
    qtd_rose = int(input('Quantas garrafas você quer de vinho rosé? '))
    vl_garrafas = qtd_tinto * 10.00
    vl_garrafas += qtd_branco * 15.00
    vl_garrafas += qtd_rose * 20.00
    if (vl_garrafas > 100):
        vl_frete = 0.00
        print('Você recebeu frete grátis!')
    else:
        vl_frete = 10.00
        print(f'Valor do frete é R$ {vl_frete}')
    vl_total = vl_garrafas + vl_frete
    print(f'Muito obrigado pela sua compra!\nO valor total é de R$ {vl_total}\nO endereço de entrega é: {endereco}')
