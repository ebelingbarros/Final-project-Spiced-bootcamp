intro_explain = '''

---
#### Creating a network visualisation

##### Steps 1 and 2: 

Count total number of words and filter according to a minimum threshold.
##### Step 3 and 4: 

Create distinct words combination and iterate over it to define a combination matrix X, of the following hypothetical form.

| | Word 1| Word 2|Word 3|Word 4|
|---|---				|---				|
| Word 1|	 0| 23|10|11|
| Word 2| 50| 0|3|22|
| Word 3| 100| 23|0|34|
| Word 4| 35| 45|17|0|

<p>

##### Step 4: 

Calculate Jaccard Matrix to find distances between combinations. It can be easily done using libraries such as Scipy or Sklearn. It can also be calculated without recurring to a library by defining the transposed version of the combination matrix (XT) and counting, for each pair of rows, the number of cells that do not have equal numbers. This is the Hamming distance, which, subtracted from 1, gives the Jaccard Score (1- Hamming).

The larger the score, the more distant will be nodes in the network graph. 

| | Word 1| Word 2|Word 3|Word 4|
|---|---				|---				|
| Word 1|	 1| 0|0|0|
| Word 2| 0| 1|0|0|
| Word 3| 0| 0|1|0|
| Word 4| 0| 0|0|1|

<p>

##### Step 5: 

Create network visualisation. The size of the nodes will be defined by the number of times the word appears in the corpus.

---
'''



intro_sources = '''
---
#### Credits and acknowledgements

##### Streamlit sites and code

- The <a href="https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/">"NYC Uber Ridesharing Data"</a> and the <a href="https://share.streamlit.io/casiopa/eda-imdb/main/src/utils/streamlit/EDA_IMDb_main.py">"Público, crítica y taquilla en IMDb"</a> Streamlit apps where awesome sources of inspiration for its structuration.

- The simple co-ocurrence network analysis is based on <a href="https://www.kaggle.com/itoeiji/simple-co-occurrence-network"> Gin04kg's notebook</a>.

- The estimation of a Random Forest models for, respectively, oil prices and renewable energy consumption, considering sentiment analysis is based on <a href="https://python.plainenglish.io/how-to-predict-stock-prices-change-with-random-forest-in-python-f707e101d5c4"> Bee Guan Teo's notebook.</a>


##### Images

- Cartoon by <a href="https://www.kaltoons.com/">Kal</a> on <a href="https://www.economist.com">The Economist</a>

- Stocks photo by <a href="https://unsplash.com/@vallabh1?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Arvind Vallabh</a> on <a href="https://unsplash.com/s/photos/oil-rig?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
- Renewable energy photo by <a href="https://unsplash.com/@m_____me?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">m.</a> on <a href="https://unsplash.com/s/photos/trading?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
- Oil rig photo by <a href="https://unsplash.com/@publicpowerorg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">American Public Power Association</a> on <a href="https://unsplash.com/s/photos/renewable-energy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

'''
