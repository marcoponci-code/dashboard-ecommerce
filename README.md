# Dashboard de Análise Estatística de Ecommerce

## Sobre o Projeto

Este projeto foi desenvolvido como atividade prática do curso de Cientista de Dados da EBAC.

O objetivo foi criar uma aplicação web utilizando Dash e Plotly para visualizar análises estatísticas realizadas sobre uma base de dados de produtos de Ecommerce.

A aplicação permite explorar diferentes perspectivas dos dados através de gráficos interativos.

---

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly
- Dash

---

## Análises Desenvolvidas

O dashboard apresenta as seguintes análises:

### Distribuição de Preços

Histograma mostrando a distribuição dos preços dos produtos.

### Avaliações x Quantidade Vendida

Gráfico de dispersão relacionando número de avaliações com quantidade de produtos vendidos.

### Correlação entre Variáveis

Mapa de calor apresentando a matriz de correlação das variáveis numéricas.

### Top 10 Marcas

Gráfico de barras mostrando as marcas com maior quantidade de produtos cadastrados.

### Distribuição por Gênero

Gráfico de pizza demonstrando a participação de cada categoria.

### Densidade dos Preços

Visualização da densidade da distribuição dos preços.

### Regressão Linear

Análise de regressão entre quantidade de avaliações e quantidade vendida.

---

## Estrutura do Projeto

```text
.
├── dashboard_ecommerce.py
├── ecommerce_estatistica.csv
├── requirements.txt
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/ebac-dashboard-ecommerce.git
```

Entre na pasta:

```bash
cd ebac-dashboard-ecommerce
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute:

```bash
python dashboard_ecommerce.py
```

Após a execução, acesse:

```text
http://127.0.0.1:8051
```

---

## Autor

Marco Ponciano

Projeto desenvolvido para fins educacionais como atividade prática da EBAC.
