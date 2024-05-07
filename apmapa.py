import streamlit as st
import pandas as pd
import yfinance as yf
import investpy as inv
import seaborn as sns 
import matplotlib.pyplot as plt
from datetime import date
import MetaTrader5 as mt5
from bcb import sgs 
import datetime
from datetime import timedelta



def Atividade():
    st.title('atividade')
    st.title('PIB')

      
    pib = sgs.get({'PIB':7326})

    st.bar_chart(pib,)

    st.markdown('-----')

    st.title('PIB SERVIÇOS')

    PS = sgs.get({'PS':7329})
      
    st.bar_chart(PS)

    st.markdown('--')

    st.title('IBC_br')

    ibc = sgs.get({'ibc':7329})

    st.bar_chart(ibc)

    st.markdown('----')

    st.title('População')

    populacao = sgs.get({'populacao':21774})

    st.area_chart(populacao)


def Inflação():
    st.date_input('selecione')
    st.title('Inflação')    
    bonds  = inv.get_bonds_overview('brazil')
    b2=bonds['last_close']
    st.write(b2)
    st.bar_chart(b2)
    st.markdown('------')

    st.title('IPCA-15')
    ipca = sgs.get({'ipca':7478})
    st.area_chart(ipca)

    st.markdown('-----')

    st.title('IPCA de Alimentos e Bebidas')
    albebidas = sgs.get({'albebidas':1635})
    st.area_chart(albebidas)
def Dívida():
    st.title('Dívida') 

    st.title('Dívida do Governo em Relação o PIB')
    dv = sgs.get({'dv':4504})
    st.area_chart(dv)   

def main():
    st.title('Mapa Econômico')
    st.markdown('-----')
    st.sidebar.image('brasil.jpg',caption='Mapa Econômico', width=200)
    Indicadores = ['Atividade','Inflação','Dívida']
    escolha = st.sidebar.radio('Indicadores',Indicadores)
    st.sidebar.date_input('DE:')
    st.sidebar.date_input('PARA:')



    if escolha == 'Atividade':
        Atividade()

    if escolha == 'Inflação':
        Inflação()

    if escolha == 'Dívida':
        Dívida()

main()