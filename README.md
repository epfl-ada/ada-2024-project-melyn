# The Evolution of Cinema : The Success Story Behind Movies Hits (1915-2015)

## Abstract

This project investigates the evolution of key factors influencing box-office success for films released between 1915 and 2015, aiming to uncover how audience preferences and industry dynamics have transformed over the century. By analyzing a wide range of characteristics—such as genre, release timing (seasonality), localization strategies (e.g., number of translations and countries), and the age and gender of lead actors—we strive to understand their impact on film ratings, revenue and broader cinematic trends.

Our study delves into five distinct historical periods (1915–1930, 1930–1950, 1950–1970, 1970–2000, and 2000–2015) to identify how shifts in these characteristics align with changes in commercial and critical success. We pay particular attention to trends in genre combinations, localization strategies and actor demographics. This comprehensive analysis reveals patterns that not only reflect the changing dynamics of cinema but also provide insights into the evolving preferences of audiences worldwide. By tracing these trends, this study aims to illuminate the factors that have driven the success of some of the most iconic films in history.


## Research Questions
### How has cinema evolved over time, and what pivotal moments shaped its trajectory?
- What are the defining characteristics of each cinematic era?
- How do the characteristics of films reflect broader societal and cultural changes across the five periods?

### Does the evolution of movie success follow a particular trend?
- Which genres have gained or lost prominence in each era, and what do these trends reveal about audience preferences and revenue performance?
- What impact have localization strategies, such as translations and international releases, had on a films' ability to reach broader audiences?
- What age range of lead actors has tended to yield the highest box-office numbers across different periods? Does this vary by gender or over the years? 


## Datasets
### Original dataset (CMU Movie Summary)
  The CMU Movies dataset offers valuable insights into factors affecting box-office performance, covering attributes like genre, release timing, and actor demographics across thousands of films from early cinema through 2015. This data supports our analysis of trends over time, helping us explore how audience preferences and industry practices have evolved. Specifically, it enables us to examine the impact of genres, actor age and gender, and localization on success. The dataset’s depth makes it essential for identifying patterns and answering questions about film success dynamics over the past century.

### Additional Dataset
- IMDb dataset : The IMDb dataset provides valuable ratings and voting data that can serve as an alternative metric for measuring a movie's success, beyond traditional metrics like box office revenue. By using IMDb ratings (average viewer scores out of 10) and the number of votes a movie has received, we can develop a “popularity” metric that reflects audience reception and engagement, which can highlight successful films that may not have been financial hits but were well-received by viewers.
When using IMDb data for such analyses, a key challenge is integrating it with other datasets, like the CMU movies dataset in our case. For instance, differences in naming conventions, movie release years, and sometimes even mismatches in genre categories mean that titles may not match directly. The title.basics and title.ratings tables provide most of the rating information, and most of the work is filtering and cleaning this data.
Despite these constraints, with robust preprocessing, the IMDb ratings data allows us to examine audience-based success and trends that complement or even differ from revenue-focused metrics, offering a broader perspective on a movie's impact.


## Project Plan
- **Step 1:** Data Pre-Processing and Cleaning
In this step, we focus on preparing the data for analysis. This involves cleaning the datasets by removing missing values, duplicates, or inconsistencies that could skew the results. We also standardize data formats, such as dates, names, or categories, to ensure consistency and make the data easier to work with. The goal is to make the data ready for exploration and analysis, ensuring its quality and reliability.

- **Step 2:** Exploratory Data Analysis
The goal is to get a better understanding of the behaviour of each characteristics across the periods. We examine the movie's features, such as their genres, languages, release season, ratings or box office performance. We analyze the distribution of these features and visualize them using various plots, such as histograms, bar charts, or scatter plots. This helps us to identify patterns, trends, or outliers in the data.

- **Step 3:** Propensity Score Matching & Causal Inference
We use propensity score matching to compare the characteristics of movies that are similar in all aspects except for one variable. This allows us to isolate the effect of a specific variable on the outcome of interest, such as box office performance or ratings. By matching movies with similar characteristics, we can control for confounding variables and estimate the causal effect of a particular factor on the outcome. 

- **Step 4:** Modeling
We dive deeper into more advanced analyses by using machine learning algorithms to predict rating and box office performances based on movie features such as genre, langage, and country. Taking the best model, we perform feature importance analysis to identify the most influential factors in predicting the success of a movie. This helps us to identify the key drivers of movie success and understand how different factors influence a movie's performance.

- **Step 5:** Generate plots and insights
We generate plots and visualizations to communicate our findings effectively. This includes creating charts, graphs, and tables that summarize the results of our analysis. We also provide insights and interpretations of the data, highlighting key trends, patterns, or relationships that we have identified. This step is crucial for presenting our findings in a clear and compelling way.

- **Step 6:** Data Storytelling
We create a data story that tells a compelling narrative about the evolution of cinema and the factors that have influenced movie success over time. This involves combining our analysis, insights, and visualizations into a coherent and engaging story that captivates the audience.


## Methods
- **Statistical Analysis:** We use statistical methods to analyze the relationships between different variables and identify patterns in the data.
- **Propensity Score Matching:** We use propensity score matching to isolate the effect of a specific variable on the outcome of interest
- **Machine Learning:** We  use machine learning algorithms to predict rating and box office performances based on movie features, such as linear Regression, Ridge Regression, Random Forest, XGBoost, Bagging Regressor, Gradient Boosting and Decision Tree.


## Repository Structure
```
├── data/                          # Directory for datasets and related files
│   ├── .ipynb_checkpoints/        # Checkpoints for Jupyter notebooks
│   ├── CMU/                       # CMU-specific data files
│   ├── IMDb/                      # IMDb-specific data files
│   ├── pickle/                    # Pickle files for serialized data
│   └── CPI.csv                    # Consumer Price Index dataset (CSV format)
├── pipeline/                      # Jupyter notebooks for data cleaning and preparation
│   ├── .ipynb_checkpoints/        # Checkpoints for Jupyter notebooks
│   ├── character_dataset_cleaning.ipynb # Cleaning character dataset
│   ├── IMDb_dataset_cleaning.ipynb      # Cleaning IMDb dataset
│   └── movie_dataset_cleaning.ipynb     # Cleaning movie dataset
├── plots/                         # Directory for HTML visualization outputs
├── src/                           # Source code directory
│   ├── utils/                     # Utility functions and scripts
│   ├── modeling.ipynb             # Notebook for modeling and analysis
│   ├── psm.ipynb                  # Notebook for propensity score matching and causal inference
│   ├── stats.ipynb                # Notebook for statistical analysis
├── results.ipynb                  # A well-structured notebook showing the results
├── pip_requirements.txt           # Python dependencies required for the project
├── .gitignore                     # Git ignore file
└── README.md                      # Project documentation (this file)
```

## Team Organization
- Elyes Trabelsi: Step 1 & 6 
- Najmeddine Abbassi: Step 1 & 5
- Lucas Simonnet: Step 1 & 6
- Annaelle Benlamri: Step 2 & 4
- Yassine Mamlouk: Step 2 & 3

## Link to the website
https://epfl-ada.github.io/ada-2024-project-melyn/
