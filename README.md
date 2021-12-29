# Spiced Data Science bootcamp final project: NLP and Sentiment Analysis with oil price and renewable energy articles
## Libraries
The code presented in this repository was written in Python 3. These are the main Python packages required for it to work: `Pandas`, `Numpy`, `Seaborn`, `Plotly`, `Matplotlib`, `Sklearn`, `BeautifulSoup`, `Requests`, `Json`, `Spacy`, `Streamlit`, `NetworkX`, `SqlAlchemy` and `Altair`.

## Introduction, project motivation and data
The main objective of this project is to analyse whether NLP techniques and sentiment analysis can be used as features for oil price and renewable energy demand prediction.
For this purpose, I scrape ~ 9000 articles from oilprice.com's `oil-price`, `alternative-energy` and `crude-oil` tabs. Because I choose a regression problem, the scraped articles are processed using modern Sentiment Analysis techniques and used as features in Random Forest regression models. The scraped articles are also treated using modern NLP techniques and used to create network visualisations of more frequent words over time. The entire project is presented in a Streamlit app that is deployed to the web using Heroku.


## File Descriptions
- `gathering_data.ipynb`: This notebook contains the code used to download the articles and to create a dataframe with the obtained texts.
- `sentiment_analysis.ipynb`: The sentiment analysis is performed on this notebook
- `negative-words.txt`: File used in the sentiment analyis
- `positive-words.txt`: File used in the sentiment analysis
- `sentiment_analysis_regression.ipynb`: Notebook with the regression exercises with Random Forest
- `nlp_notebook.ipynb`: Notebook with some further NLP preprocessing steps
- `nlp_notebook_model-network-analysis.ipynb`: The network analysis using NetworkX is conducted in this notebook
- `exploratory_data_analysis.ipynb`: Notebook with some further Exploratory Data Analysis
- `data`: The folder contains the csv files used in this project.
- `setup.sh`: file needed for the Streamlit app's deployment
- `Procfile`: file needed for the Streamlit app's deployment
- `requirements.txt`: file needed for the Streamlit app's deployment

## Methodology

The methodology of the project closely follows the following process chart, although not necessarily in chronological order. After extracting and processing the articles with Jupyter Notebooks, I work with Streamlit .py files for creating visualisations and presenting the project. As a final step, I deploy the app to the web using Heroku.

<p align="center">
  <img width="80%" height="100%" src="https://github.com/ebelingbarros/Final-project-Spiced-bootcamp/blob/main/images/process.png"> 
</p> 

## Streamlit

The entire project's results and visualisations are presented in a Streamlit app, which is deployed to the web with Heroku. Click **[here](https://energy-sentiment-analysis.herokuapp.com/)** to access the app.

<p align="center">
  <img width="80%" height="100%" src="https://github.com/ebelingbarros/Final-project-Spiced-bootcamp/blob/main/images/streamlit_app_gif.gif"> 
</p> 

## Conclusions and next steps

Forthcoming



## Acknowledgments
### A general note

I'm highly indebted to [Spiced's academy](https://www.spiced-academy.com/en/program/data-science) teaching team for the wonderful classes, course material and also code. A special thanks goes to Paula, Arjun and Joseph.

### Streamlit sites and code
- The ["NYC Uber Ridesharing Data"](https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/) and the ["Público, crítica y taquilla en IMDb"](https://share.streamlit.io/casiopa/eda-imdb/main/src/utils/streamlit/EDA_IMDb_main.py) Streamlit apps where awesome sources of inspiration for its structuration.

- The simple co-ocurrence network analysis is based on [Gin04kg's](https://www.kaggle.com/itoeiji/simple-co-occurrence-network) notebook.

- The estimation of a Random Forest models for, respectively, oil prices and renewable energy consumption, considering sentiment analysis is based on [Bee Guan Teo's](https://python.plainenglish.io/how-to-predict-stock-prices-change-with-random-forest-in-python-f707e101d5c4) notebook.

### Images
- Cartoon by [Kal](https://www.kaltoons.com/) on [The Economist](https://www.economist.com/)

- Stocks photo by [Arvind Vallabh](https://unsplash.com/@vallabh1?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)

- Renewable energy photo by [m.](https://unsplash.com/@m_____me?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)

- Oil rig photo by [American Public Power Association](https://unsplash.com/@publicpowerorg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
