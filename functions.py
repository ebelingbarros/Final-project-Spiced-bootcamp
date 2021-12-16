import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly import tools
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import networkx as nx
import altair as alt
from PIL import Image
from variables import *


def set_home():
    md_oil = 'images/oil.jpg'
    md_trading = 'images/trading.jpg'
    md_renewable = 'images/renewable.jpg'

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(md_oil, use_column_width='always')
    with col2:
        st.image(md_trading, use_column_width='always')
    with col3:
        st.image(md_renewable, use_column_width='always')
    #st.write(intro_herramientas_fuentes, unsafe_allow_html=True)
    
    
    st.markdown("<h3 style='text-align: center; color: black;'>Another <em style='color: red;'>crazy</em> day in the markets</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,6,2])

    
    with col1:
        st.write("")

    with col2:
        image = Image.open('images/buy_sell.jpeg')
        st.image(image, caption='Credit: Cartoon by Cal for "The Economist"', use_column_width='always')

    with col3:
        st.write("")
   
    with st.container():
        st.write(intro_sources, unsafe_allow_html=True)
        
    
def data():
    st.header('The Data')
    st.write('In this section, some of the features from the data that has been scraped from the website from Oilprice.com is presented.') 
    menu_data = st.radio(
        "",
        ("Oil Prices", "Renewable Energies", "Crude Oil"),
    )
       
    if menu_data == "Oil Prices":
        with st.container():
            st.markdown('### DataFrame `Oil Prices`')
            st.markdown('This is the dataframe that has been obtained after webscraping, tokenization and the sentiment analysis.')
            st.markdown('2189 entries  |  6 columns')
            df = pd.read_csv('data/corpus_oil_price_sample.csv')
            df.dropna(inplace=True)
            st.write(df.sample(10))
    
    
            st.subheader(f'Count of the months scraped articles were written')
            oil_price=pd.read_csv("data/oilprice.csv", index_col=0)
    
            fig, ax = plt.subplots(figsize=(12, 7))
            ax = sns.barplot(data = oil_price, x = 'date', y ='title')
            plt.xticks(fontsize=10)
            sns.despine()
            for index, label in enumerate(ax.get_xticklabels()):
                if index % 20 == 0:
                    label.set_visible(True)
                else:
                    label.set_visible(False)
            st.pyplot(fig)

    elif menu_data == "Renewable Energies":    
        with st.container():
            st.markdown('### DataFrame `Renewable Energies`')
            st.markdown('This is the dataframe that has been obtained after webscraping, tokenization and the sentiment analysis.')
            st.markdown('1833 entries | 6 columns')
            df = pd.read_csv('data/corpus_alternative_energies_sample.csv')
            df.dropna(inplace=True)
            st.write(df.sample(10))
            st.subheader(f'Count of the months scraped articles were written')
            alternative_energy=pd.read_csv("data/alternative.csv", index_col=0)
            fig, ax = plt.subplots(figsize=(12, 7))
            ax = sns.barplot(data = alternative_energy, x = 'date', y ='title')
            plt.xticks(fontsize=10)
            sns.despine()
            for index, label in enumerate(ax.get_xticklabels()):
                if index % 20 == 0:
                    label.set_visible(True)
                else:
                    label.set_visible(False)
            st.pyplot(fig)

    elif menu_data == "Crude Oil":  
        with st.container():
            st.markdown('### DataFrame `Crude Oil`')
            st.markdown('This is the dataframe that has been obtained after webscraping, tokenization and the sentiment analysis.')
            st.markdown('5009 entries | 6 columns')
            df = pd.read_csv('data/corpus_oil_price_sample.csv')
            df.dropna(inplace=True)
            st.write(df.sample(10))
            st.subheader(f'Count of the months scraped articles were written')
            crude_oil=pd.read_csv("data/corpus_crude_oil_sample.csv", index_col=0)
            fig, ax = plt.subplots(figsize=(12, 7))
            ax = sns.barplot(data = crude_oil, x = 'date', y ='title')
            plt.xticks(fontsize=10)
            sns.despine()
            for index, label in enumerate(ax.get_xticklabels()):
                if index % 20 == 0:
                    label.set_visible(True)
                else:
                    label.set_visible(False)
            st.pyplot(fig)
            st.subheader(f'A list of top words in the database')
            source = pd.read_csv('data/word_cnt_df_crude.csv', index_col=0)

            st.altair_chart(alt.Chart(source).mark_bar()
                        .encode(x='cnt:Q',
                                y=alt.Y('word:N', sort='-x'))
                        .configure_mark(opacity=0.8,color='green'), 
                        use_container_width=True)
    
    
    
def sentiment_analysis():
    corpus_oil_price=pd.read_csv("data/corpus_oil_price_final.csv", index_col=0)
    corpus_alternative_energies=pd.read_csv("data/corpus_alternative_energies_final.csv", index_col=0)
    corpus_crude_oil=pd.read_csv("data/corpus_crude_oil_final.csv", index_col=0)
    # create figure and axis objects with subplots()
    st.header('Sentiment analysis timeline plots')
    st.subheader('Oil prices sentiment analysis vs yearly oil prices (Brent in US$)')
    st.write('Although there are some discrepancies, it is possible to see in the plot below that the vader sentiment is a promising feature to predict oil prices. It remains to be seen whether its lag is a better predictor.')
    fig,ax = plt.subplots(figsize=(12, 7))
    ax.set_facecolor('#e6e6e6')
    plt.grid(color='white', linewidth=0.7)
    # make a plot
    ax.plot(corpus_oil_price.year, corpus_oil_price['vader_sentiment'], color="red", marker="o", label='Vader Sentiment')
    # set x-axis label
    ax.set_xlabel("year",fontsize=12)
    # set y-axis label
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(corpus_oil_price.year, corpus_oil_price["2020_money"],color="blue",marker="o", label='Oil price in 2020 US$')
    ax.figure.legend()
    st.pyplot(fig)
    
    st.subheader('Renewable energy sentiment analysis vs yearly global renewable energy consumption (in Exajoules)')
    st.write('By itself, renewable energy sentiment does not seem to be a good predictor of global renewable energy consumption, which has been marching steadily in the last years. It remains to be seen if the outlook is different for the American market.')
    fig,ax = plt.subplots(figsize=(12, 7))
    ax.set_facecolor('#e6e6e6')
    plt.grid(color='white', linewidth=0.7)
    # make a plot
    ax.plot(corpus_alternative_energies.year, corpus_alternative_energies['vader_sentiment'], color="red", marker="o", label='Vader Sentiment')
    # set x-axis label
    ax.set_xlabel("year",fontsize=12)
    # set y-axis label
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(corpus_alternative_energies.year, corpus_alternative_energies["renewables"],color="green",marker="o", label='Renewable energy consumption')
    ax.figure.legend()
    st.pyplot(fig)

    
    st.subheader('Crude oil sentiment analysis vs yearly global oil production (in thousands of barrels per day)')
    st.write('In the graph it is possible to see that, with the exception of the last two years, which have been marked by the Corona pandemics, there is a decoupling between global oil production and the sentiment in this market. Before the pandemic hit the world, global oil production continued its steady upward trajectory despite a more negative sentiment regarding the future of oil in the world energy mix. This tells a lot about how difficult a challenge the globe faces in its deep decarbonization attempts.')
    fig,ax = plt.subplots(figsize=(12, 7))
    ax.set_facecolor('#e6e6e6')
    plt.grid(color='white', linewidth=0.7)
    # make a plot
    ax.plot(corpus_crude_oil.year, corpus_crude_oil['vader_sentiment'], color="red", marker="o", label='Vader Sentiment')
    # set x-axis label
    ax.set_xlabel("year",fontsize=12)
    # set y-axis label
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(corpus_crude_oil.year, corpus_crude_oil["oil_production"],color="brown",marker="o", label='Oil production')
    ax.figure.legend()
    st.pyplot(fig)

    
    
def modelling():
    st.header('Modelling with sentiment analysis')
    st.write('In this section the monthly average sentiments extracted in the previous sections are regressed for both Oil Prices (Brent, in US$) and for Renewable Energy Consumption (Trillion Btu). In both cases, data is for the United States. In the oil prices subsection, an interaction term is also included, which is given by the product of oil demand and oil supply in the U.S. (in thousands of daily barrels). For the renewable energy subsection, an index of American industrial production are included in the equations, alongside monthly dummies. The equations are regressed with a simple Random Forest regression model, using GridSearch, with the following parameters: (n_estimators: 50, 100, max_depth: 2, 10, 50). To test the robustness of the model, 15% of the data from the tail is treated as "test".') 
    
    menu_modelling = st.radio(
        "",
        ("Oil Prices", "Renewable energies"),
    )

    if menu_modelling == "Oil Prices":
        # Create engine
        st.markdown('### Results for `Model 1`')
        st.markdown('Oil Price (Brent) = Sentiment + Interaction Term (Oil Demand x Oil Supply)')
        st.markdown('Training score: 0.948 | RMSE: 18.51')
        engine = create_engine('sqlite:///oil_1.db')
        corpus_oil_price_resampled2_2 = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_oil_price_resampled2_2.date, corpus_oil_price_resampled2_2['y_pred'], color="red", marker="o", label='Predicted oil prices')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_oil_price_resampled2_2.date, corpus_oil_price_resampled2_2["Brent"],color="green",marker="o", label='Observed oil prices')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)

        # Create engine
        st.markdown('### Results for `Model 2`')
        st.markdown('Oil Price (Brent) = Sentiment(-1) + Interaction Term (Oil Demand x Oil Supply)')
        st.markdown('Training score: 0.948 | RMSE: 18.3')
        engine = create_engine('sqlite:///oil_2.db')
        corpus_oil_price_resampled2_3 = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_oil_price_resampled2_3.date, corpus_oil_price_resampled2_3['y_pred'], color="red", marker="o", label='Predicted oil prices')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_oil_price_resampled2_3.date, corpus_oil_price_resampled2_3["Brent"],color="green",marker="o", label='Observed oil prices')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)
        
        # Create engine
        st.markdown('### Results for `Model 3`')
        st.markdown('Oil Price (Brent) = Sentiment + Oil Price (Brent)(-1)')
        st.markdown('Training score: 0.991 | RMSE: 7.67')
        engine = create_engine('sqlite:///oil_3.db')
        corpus_oil_price_resampled2_4 = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_oil_price_resampled2_4.date, corpus_oil_price_resampled2_4['y_pred'], color="red", marker="o", label='Predicted oil prices')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_oil_price_resampled2_4.date, corpus_oil_price_resampled2_4["Brent"],color="green",marker="o", label='Observed oil prices')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)
               
        
    elif menu_modelling == "Renewable energies":
        # Create engine
        st.markdown('### Results for `Model 1`')
        st.markdown('Renewable Energy Consumption = Sentiment + Industrial Production Index + Monthly Dummies')
        st.markdown('Training score: 0.913 | RMSE: 200.7')
        engine = create_engine('sqlite:///energy.db')
        corpus_alternatives = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_alternatives.date, corpus_alternatives['y_pred'], color="red", marker="o", label='Predicted renewable energy consumption')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_alternatives.date, corpus_alternatives["Total_renewable_consumption"],color="green",marker="o", label='Observed renewable energy consumption')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)

        # Create engine
        st.markdown('### Results for `Model 2`')
        st.markdown('Renewable Energy Consumption = Sentiment(-1) + Industrial Production Index + Monthly Dummies')
        st.markdown('Training score: 0.531 | RMSE: 197.2')
        engine = create_engine('sqlite:///energy2.db')
        corpus_alternatives2 = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_alternatives2.date, corpus_alternatives2['y_pred'], color="red", marker="o", label='Predicted renewable energy consumption')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_alternatives2.date, corpus_alternatives2["Total_renewable_consumption"],color="green",marker="o", label='Observed renewable energy consumption')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)
        
        # Create engine
        st.markdown('### Results for `Model 2`')
        st.markdown('Renewable Energy Consumption = Sentiment + Industrial Production Index + Renewable Energy Consumption(-1) + Monthly Dummies')
        st.markdown('Training score: 0.976 | RMSE: 58.2')
        engine = create_engine('sqlite:///energy3.db')
        corpus_alternatives3 = pd.read_sql("Table", engine)
        fig,ax = plt.subplots(figsize=(12, 7))
        ax.set_facecolor('#e6e6e6')
        plt.grid(color='white', linewidth=0.7)
        # make a plot
        ax.plot(corpus_alternatives3.date, corpus_alternatives3['y_pred'], color="red", marker="o", label='Predicted renewable energy consumption')
        # set x-axis label
        ax.set_xlabel("year",fontsize=12)
        # set y-axis label
        # twin object for two different y-axis on the sample plot
        #ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax.plot(corpus_alternatives3.date, corpus_alternatives3["Total_renewable_consumption"],color="green",marker="o", label='Observed renewable energy consumption')
        ax.figure.legend()
        for index, label in enumerate(ax.get_xticklabels()):
           if index % 2 == 0:
              label.set_visible(True)
           else:
              label.set_visible(False)
        st.pyplot(fig)
        
        
def network():
        st.title('Network analysis with co-ocurrence networks')
        menu_network = st.radio(
        "",
        ("Oil Prices", "Renewable energies"),
    )
        if menu_network == "Oil Prices":
            with st.container():
                st.subheader("Oil prices")
                
                st.markdown('The following graph charts the evolution of the oil price (Brent in US$).')
                chart_data = pd.read_csv('data/oil_prices_2.csv', index_col=0)
                st.write("**Oil prices (Brent) in US$D**")

                st.altair_chart(alt.Chart(chart_data.reset_index()).mark_trail()
                    .encode(x = alt.X('index:T', axis=alt.Axis(title='Years')),
                            y = alt.Y('Brent:Q', axis=alt.Axis(title='Brent in US$')), 
                            size='Brent:Q')
                    .configure_mark(
                    opacity=0.8,
                    color='cyan'
                ), use_container_width=True)    
                
                st.markdown('In what follows, the scraped data for the category "oil prices" is tokenized, treated for stopwords, and grouped into nodes using a Simple Co-occurrence Network.')
                year_selected = st.slider("Select year", 2010, 2021)
                if year_selected == 2010:
                    st.image('images/oil2010.png')
                elif year_selected == 2011:
                    st.image('images/oil2011.png')
                elif year_selected == 2012:
                    st.image('images/oil2012.png')
                elif year_selected == 2013:
                    st.image('images/oil2013.png')
                elif year_selected == 2014:
                    st.image('images/oil2014.png')
                elif year_selected == 2015:
                    st.image('images/oil2015.png')    
                elif year_selected == 2016:
                    st.image('images/oil2016.png')
                elif year_selected == 2017:
                    st.image('images/oil2017.png')    
                elif year_selected == 2018:
                    st.image('images/oil2018.png')
                elif year_selected == 2019:
                    st.image('images/oil2019.png')
                elif year_selected == 2020:
                    st.image('images/oil2020.png')
                elif year_selected == 2021:
                    st.image('images/oil2021.png')
        
                st.subheader(f'A list of top words in the database')
                source = pd.read_csv('data/word_cnt_df_oil_price.csv', index_col=0)

                st.altair_chart(alt.Chart(source).mark_bar()
                        .encode(x='cnt:Q',
                                y=alt.Y('word:N', sort='-x'))
                        .configure_mark(opacity=0.8,color='cyan'), 
                        use_container_width=True)
                                                           
        elif menu_network == "Renewable energies":
             with st.container():
                st.subheader("Renewable energies")
                
                st.markdown('The following graph charts the evolution of renewable energy consumption in the United States.')
                
                chart_data = pd.read_csv('data/renewable_energy_consumption_2.csv', index_col=0)
                st.write("**Evolution of Renewable Energy Consumption (Trillion Btu) in the US**")
                st.altair_chart(alt.Chart(chart_data.reset_index())
                    .mark_trail().encode(x = alt.X('index:T', axis=alt.Axis(title='Years')),y = alt.Y('Total_renewable_consumption:Q', axis=alt.Axis(title='Renewable energy consumption')), size='Total_renewable_consumption:Q').configure_mark(
                    opacity=0.8,
                    color='green'
                ), use_container_width=True)     
                
                st.markdown('In what follows, the scraped data for the category "renewable energy" is tokenized, treated for stopwords, and grouped into nodes using a Simple Co-occurrence Network.')
                year_selected = st.slider("Select year", 2010, 2021)
                if year_selected == 2010:
                    st.image('images/energy2010.png')
                elif year_selected == 2011:
                    st.image('images/energy2011.png')
                elif year_selected == 2012:
                    st.image('images/energy2012.png')
                elif year_selected == 2013:
                    st.image('images/energy2013.png')
                elif year_selected == 2014:
                    st.image('images/energy2014.png')
                elif year_selected == 2015:
                    st.image('images/energy2015.png')    
                elif year_selected == 2016:
                    st.image('images/energy2016.png')
                elif year_selected == 2017:
                    st.image('images/energy2017.png')    
                elif year_selected == 2018:
                    st.image('images/energy2018.png')
                elif year_selected == 2019:
                    st.image('images/energy2019.png')
                elif year_selected == 2020:
                    st.image('images/energy2020.png')
                elif year_selected == 2021:
                    st.image('images/energy2021.png')      
                
                st.subheader(f'A list of top words in the database')
                source = pd.read_csv('data/word_cnt_df_renewables.csv', index_col=0)

                st.altair_chart(alt.Chart(source).mark_bar()
                        .encode(x='cnt:Q',
                                y=alt.Y('word:N', sort='-x'))
                        .configure_mark(opacity=0.8,color='green'), 
                        use_container_width=True)


                
                
                                                        
          