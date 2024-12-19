## File Details

### 1. `DSB_Project_Text_Analysis.ipynb`
**Description**:  
This notebook handles the preprocessing and analysis of textual data. Key steps include:
- Checking and removing duplicate values.
- Handling missing data.
- Dropping irrelevant columns.
- Performing keyword-based analysis.
- Topic Modelling and Sentiment analysis.

### 2. `DSB_Data_Modelling.ipynb`
**Description**:  
This notebook focuses on preparing data for modeling. Key steps include:
- Importing and preprocessing datasets.
- Performing sentiment analysis again and followed by modelling and comparing the results obtained.
- Creating a Profit Curve to understand which is the best suited model.

### 3. `Reddit Scraping.ipynb`
**Description**:  
Performs data scraping from Reddit using the `praw` library, focusing on:
- Setting up API connections.
- Extracting Reddit posts based on specified criteria.


### 4. `nyt_data_extraction.py`
**Description**:  
Fetches data from the New York Times API using a list of refined keywords. Includes:
- API setup and configuration.
- Generating csv containing API data for the specified time period

### 5. `combined_data_final.csv`
**Description**:  
This dataset contains New York Times article data used for text analysis and modeling. The columns include:
- `keyword`: Keywords related to the article.
- `headline`: The article's title.
- `abstract`: A summary of the content.
- `pub_date`: Publication date and time.
- `section_name`: Section classification (e.g., U.S., Food).
- `type_of_material`: Type of material (e.g., News, Interactive).
- `document_type`: Document classification (e.g., article, multimedia).
- `news_desk`: News desk responsible for the article.
- `snippet`: A brief snippet of the article.
- `lead_paragraph`: The first paragraph of the article.
- `source`: Source of the article (New York Times).
- `word_count`: Word count of the article.
- `uri`: Unique identifier for the article.
- `web_url`: Link to the article.
- `byline`: Author(s) of the article.
- `keywords`: Keywords summarizing the article's content.



