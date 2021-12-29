# Spiced Data Science bootcamp final project: NLP and Sentiment Analysis with oil and renewable energy articles
## Libraries
The code presented in this repository was written in Python 3. These are the main Python packages required for it to work: `Pandas`, `Numpy`, `Seaborn`, `Plotly`, `Matplotlib`, `Sklearn`, `BeautifulSoup`, `Requests`, `Json`, `Spacy`, `Streamlit`, `NetworkX`, `SqlAlchemy` and `Altair`.

## Introduction, project motivation and data
The main objective of this project is to analyse whether NLP techniques and sentiment analysis can be used as features for oil price and renewable energy demand prediction.
For this purpose, I scrape ~ 9000 articles from oilprice.com's `oil-price`, `alternative-energy` and `crude-oil` tabs. Because I choose a regression problem, the scraped articles are processed using modern Sentiment Analysis techniques and used as features in Random Forest regression models. The scraped articles are also treated using modern NLP techniques and used to create network visualisations of more frequent words over time. The entire project is presented in a Streamlit app that is deployed to the web using Heroku.


## File Descriptions
- `capstone_notebook.ipynb`: The code contained in this Jupyter notebook cleans and prepares the data, carries out the EDA analysis and generates the Machine Learning regression model.
- `data`: The folder contains the exame500.csv csv file, in which the data for the project is stored.

## Methodology


<p align="center">
  <img width="80%" height="100%" src="https://github.com/ebelingbarros/Final-project-Spiced-bootcamp/blob/main/images/process.png"> 
</p> 




3. Building the model
xxxx

4. Model Evaluation
xxxxx



xxxxxx
## Streamlit



## Conclusions and next steps
xxxxx

The entire Medium post regarding these conclusions can be read here.




## Acknowledgments
### Streamlit sites and code
- The ["NYC Uber Ridesharing Data"](https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/) and the ["Público, crítica y taquilla en IMDb"](https://share.streamlit.io/casiopa/eda-imdb/main/src/utils/streamlit/EDA_IMDb_main.py) Streamlit apps where awesome sources of inspiration for its structuration.

- The simple co-ocurrence network analysis is based on [Gin04kg's](https://www.kaggle.com/itoeiji/simple-co-occurrence-network) notebook.

- The estimation of a Random Forest models for, respectively, oil prices and renewable energy consumption, considering sentiment analysis is based on [Bee Guan Teo's](https://python.plainenglish.io/how-to-predict-stock-prices-change-with-random-forest-in-python-f707e101d5c4) notebook.

### Images
- Cartoon by [Kal](https://www.kaltoons.com/) on [The Economist](https://www.economist.com/)

- Stocks photo by [Arvind Vallabh](https://unsplash.com/@vallabh1?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)

- Renewable energy photo by [m.](https://unsplash.com/@m_____me?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)

- Oil rig photo by [American Public Power Association](https://unsplash.com/@publicpowerorg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
