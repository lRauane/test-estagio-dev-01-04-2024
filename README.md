<p style="text-align:center" dir="auto">
  <a href="#orientacoes">Orientações</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#observacoes">Observações</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#etapa-1">Etapa 1</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#etapa-2">Etapa 2</a>
</p>
<hr>
<h1 style="text-align:center">Estágio Desenvolvedor Web (Back/Front-End) - Django/Python</h1>
<h2 id="orientacoes" style="text-align:center;border-bottom:none">Orientações</h2>

- Deverá ser utilizada a linguagem Python e o framework Django para desenvolver as soluções;
- O candidato terá que criar uma branch nomeada com o seu nome e abrir um pull request para concluir a entrega do teste;
- <strong>Atenção</strong>: O candidato precisa fazer o fork do repositório para conseguir abrir o pull request;

<hr>
<h2 id="observacoes" style="text-align:center;border-bottom:none">Observações</h2>

- O banco de dados utilizado fica a sua escolha;
- Podem ser feitas alterações nas configurações do projeto Django;

<hr>
<h2 id="etapa-1" style="text-align:center;border-bottom:none">Etapa 1</h2>

Uma empresa de assinatura de energia está interessada em criar uma calculadora de economia em seu site e consultou você para desenvolver a calculadora para eles. Eles definiram como requisito a utilização da linguagem Python e o framework Django para desenvolver a aplicação.

### Sua aplicação receberá as seguintes entradas:

- Três valores representando o consumo de energia elétrica dos últimos 3 meses
- Valor da tarifa da distribuidora
- Tipo de tarifa (Comercial, Residencial e Industrial)

### Os resultados da sua aplicação serão:

- Economia Anual
- Economia Mensal
- Desconto Aplicado
- Cobertura

#### A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

#### Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

### Requisitos Etapa 1:

1. A calculadora terá que ser desenvolvida no arquivo calculator_python.py dentro da função calculator();
2. Todos os testes presentes no arquivo calculator_python.py precisam ser executados sem erros;
3. Deverá ser utilizado o framework Django para fazer a integração entre a calculadora e a interface que você deve desenvolver.


<hr>
<h2 id="etapa-2" style="text-align:center;border-bottom:none">Etapa 2</h2>

A empresa de energia gostou da sua solução para o cálculo de economia, mas necessita de algumas alterações para disponibilizá-lo aos clientes. Assim, resolveu contratá-lo novamente para desenvolver essas novas funcionalidades. Você continuará o projeto anterior usando a linguagem Python e o framework Django.

### Requisitos Etapa 2:

1. Armazenar consumidores, seus dados pessoais e de consumo no banco de dados.(dados para cadastro na planilha consumers.xlsx);
2. Armazenar as regras de desconto seguindo a tabela dada no banco de dados;
3. Associar cada consumidor cadastrado a uma regra de desconto;
4. Calcular a economia baseada nos atributos do consumidor;
5. Listar os consumidores e a economia em uma tabela para uso dos clientes.