# Análise de Dados de Ecommerce - Aplicação Dash

# Importando bibliotecas
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


# =========================================================
# LEITURA DO DATAFRAME
# =========================================================

#df = pd.read_csv('ecommerce_estatistica.csv')
df = pd.read_csv('C:/Users/marcop/OneDrive - Globo Comunicação e Participações sa/Área de Trabalho/Marco/Cursos/Python-EBAC/Modulo 7/Exemplo/data/raw/ecommerce_estatistica.csv')



# Removendo colunas de review e coluna de índice
dfdrop = df.drop(
    ['Unnamed: 0', 'Review1', 'Review2', 'Review3'],
    axis=1
)


# Tratamento da quantidade de produtos vendidos
dfdrop['Qtd_Vendidos'] = (
    dfdrop['Qtd_Vendidos']
    .astype(str)
    .str.replace('+', '', regex=False)
    .str.replace('mil', '000', regex=False)
)

dfdrop['Qtd_Vendidos'] = pd.to_numeric(
    dfdrop['Qtd_Vendidos'],
    errors='coerce'
)


# =========================================================
# FUNÇÃO 1 - HISTOGRAMA
# =========================================================

def criar_histograma():

    fig = px.histogram(
        dfdrop,
        x='Preço',
        nbins=30
    )

    fig.update_layout(
        title='Distribuição dos Preços dos Produtos',
        xaxis_title='Preço',
        yaxis_title='Quantidade de Produtos'
    )

    return fig


# =========================================================
# FUNÇÃO 2 - GRÁFICO DE DISPERSÃO
# =========================================================

def criar_dispersao():

    fig = px.scatter(
        dfdrop,
        x='N_Avaliações',
        y='Qtd_Vendidos',
        color='Gênero',
        hover_data=['Título', 'Marca']
    )

    fig.update_layout(
        title='Número de Avaliações vs Quantidade de Produtos Vendidos',
        xaxis_title='Número de Avaliações',
        yaxis_title='Quantidade de Produtos Vendidos'
    )

    return fig


# =========================================================
# FUNÇÃO 3 - MAPA DE CALOR
# =========================================================

def criar_heatmap():

    df_corr = dfdrop[
        [
            'Nota',
            'N_Avaliações',
            'Desconto',
            'Qtd_Vendidos',
            'Preço',
            'Nota_MinMax',
            'N_Avaliações_MinMax',
            'Desconto_MinMax',
            'Preço_MinMax'
        ]
    ].corr()

    fig = px.imshow(
        df_corr,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r'
    )

    fig.update_layout(
        title='Mapa de Calor da Correlação entre Variáveis'
    )

    return fig


# =========================================================
# FUNÇÃO 4 - GRÁFICO DE BARRAS
# =========================================================

def criar_barras():

    df_marcas = (
        dfdrop['Marca']
        .value_counts()
        .head(10)
        .reset_index()
    )

    df_marcas.columns = ['Marca', 'Quantidade']

    fig = px.bar(
        df_marcas,
        x='Marca',
        y='Quantidade'
    )

    fig.update_layout(
        title='Top 10 Marcas com Maior Número de Produtos',
        xaxis_title='Marca',
        yaxis_title='Quantidade de Produtos'
    )

    return fig


# =========================================================
# FUNÇÃO 5 - GRÁFICO DE PIZZA
# =========================================================

def criar_pizza():

    df_genero = (
        dfdrop['Gênero']
        .value_counts()
        .reset_index()
    )

    df_genero.columns = ['Gênero', 'Quantidade']

    fig = px.pie(
        df_genero,
        names='Gênero',
        values='Quantidade'
    )

    fig.update_layout(
        title='Distribuição dos Produtos por Gênero'
    )

    return fig


# =========================================================
# FUNÇÃO 6 - GRÁFICO DE DENSIDADE
# =========================================================

def criar_densidade():

    fig = px.histogram(
        dfdrop,
        x='Preço',
        nbins=30,
        histnorm='density'
    )

    fig.update_layout(
        title='Densidade da Distribuição dos Preços',
        xaxis_title='Preço',
        yaxis_title='Densidade'
    )

    return fig


# =========================================================
# FUNÇÃO 7 - GRÁFICO DE REGRESSÃO
# =========================================================

def criar_regressao():

    fig = px.scatter(
        dfdrop,
        x='N_Avaliações',
        y='Qtd_Vendidos',
        trendline='ols'
    )

    fig.update_layout(
        title='Regressão entre Número de Avaliações e Quantidade de Produtos Vendidos',
        xaxis_title='Número de Avaliações',
        yaxis_title='Quantidade de Produtos Vendidos'
    )

    return fig


# =========================================================
# CRIAÇÃO DA APLICAÇÃO DASH
# =========================================================

app = dash.Dash(__name__)


# =========================================================
# LAYOUT DA APLICAÇÃO
# =========================================================

app.layout = html.Div(

    children=[

        html.H1(
            'Análise de Dados de Ecommerce',
            style={'textAlign': 'center'}
        ),

        html.H2(
            'Visualização dos Dados',
            style={'textAlign': 'center'}
        ),

        dcc.Graph(
            figure=criar_histograma()
        ),

        dcc.Graph(
            figure=criar_dispersao()
        ),

        dcc.Graph(
            figure=criar_heatmap()
        ),

        dcc.Graph(
            figure=criar_barras()
        ),

        dcc.Graph(
            figure=criar_pizza()
        ),

        dcc.Graph(
            figure=criar_densidade()
        ),

        dcc.Graph(
            figure=criar_regressao()
        )
    ]
)


# =========================================================
# EXECUÇÃO DA APLICAÇÃO
# =========================================================

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8051
    )