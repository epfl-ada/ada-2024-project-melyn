# Abstract :
This project analyzes the key factors influencing box-office success for films released between 1914 and 2016, seeking to understand how audience preferences and industry trends have evolved over time. We focus on a variety of characteristics—such as genre, release timing, localization (number of translations), and lead actors' age and gender—to determine their impact on a film's revenue. By examining six distinct historical periods, we aim to uncover how shifts in these characteristics correlate with box-office performance. Additionally, we explore genre combinations and actor age pairings to see if certain patterns consistently align with higher revenue. We also assess how localization strategies, like translations into specific languages, have helped films reach a wider audience. This study provides a comprehensive view of the changing dynamics of film success, revealing patterns that reflect both cinematic trends and evolving audience preferences across decades

# Research Questions : 
- Does the release season of a film influence its commercial success ?
- Were there specific 20-year periods where a film's genre/theme (historical, sci-fi, romantic comedy, etc.) was the predominant factor driving its commercial success
- What age range of actors (e.g. 20s, 30s, 40s+) has tended to yield the highest box office numbers in different time periods ?
- How have the highest-grossing films' box office numbers evolved from the inception of cinema until 2016? Can we identify clear inflection points?
- Are there genres that have maintained consistent commercial appeal across most time periods ?
- Does releasing a film with more foreign language translations associate with higher worldwide box office revenue?
- To what extent does offering more foreign language translations for a film contribute to increased global box office earnings?
- Are younger actors more popular than older ones ? Is it the complete opposite? Does it vary across the years ? Does it differ depending on the genre ?

# Datasets :
### Original dataset (CMU Movie Summary): 
  The CMU Movies dataset offers valuable insights into factors affecting box-office performance, covering attributes like genre, release timing, and actor demographics across thousands of films from early cinema through 2016. This data supports our analysis of trends over time, helping us explore how audience preferences and industry practices have evolved. Specifically, it enables us to examine the impact of genres, actor age and gender, and localization on success, including whether translations boost international performance. The dataset’s depth makes it essential for identifying patterns and answering questions about film success dynamics over the past century.

### Additional Dataset :
- IMDb dataset : The IMDb dataset provides valuable ratings and voting data that can serve as an alternative metric for measuring a movie's success, beyond traditional metrics like box office revenue. By using IMDb ratings (average viewer scores out of 10) and the number of votes a movie has received, we can develop a “popularity” metric that reflects audience reception and engagement, which can highlight successful films that may not have been financial hits but were well-received by viewers.
When using IMDb data for such analyses, a key challenge is integrating it with other datasets, like the EMU movies dataset. For instance, differences in naming conventions, movie release years, and sometimes even mismatches in genre categories mean that titles may not match directly. Additionally, IMDb titles may have alternate versions or regional variations, so we have to carefully align these records to prevent duplicating or missing films during merging. The title.basics and title.ratings tables provide most of the rating information, but filtering and cleaning this data, such as removing duplicate titles or aligning names, can be time-consuming.
Despite these constraints, with robust preprocessing, the IMDb ratings data allows us to examine audience-based success and trends that complement or even differ from revenue-focused metrics, offering a broader perspective on a movie's impact.

# Methods :
- T-tests: This statistical tool can compare the means of two groups to determine if they are significantly different. In your analysis, t-tests could help evaluate which factors—such as release season, genre, or localization (e.g., high vs. low number of translations)—significantly impact box-office revenue. By identifying these differences, you can determine which characteristics have a notable effect on a film's financial success.

- Pearson Correlation Coefficient (PCC): PCC assesses the linear relationship between variables, helping you pinpoint which factors, such as lead actor age, genre, or localization, have the strongest correlation with box-office revenue. Additionally, PCC could help identify optimal values, such as the ideal runtime that maximizes box-office earnings.

- Linear Regression: This technique models the relationship between box-office revenue (dependent variable) and multiple independent variables, such as genre, actor demographics, localization, and release timing. By fitting a linear equation, linear regression allows you to predict a film's revenue based on its characteristics, providing insights into how different factors work together to drive commercial success.

# Timeline :
- Step 1: Data Pre-Processing
Movie Metadata: Clean and organize the metadata by removing outliers and irrelevant entries, such as TV shows and short films, and filtering movies with fewer than 200 reviews to ensure data relevance.
Localization Data: Process localization data (e.g., number of translations) to evaluate a film's global reach and remove any unnecessary entries, focusing on elements directly related to box-office performance.
- Step 2: Analyzing Metadata Factors
Season and Genre Analysis: Use t-tests to compare box-office performance across different release seasons and genres, identifying significant differences that might impact revenue.
Actor Demographics: Explore the influence of lead actor age and gender on box-office revenue with Pearson correlation, analyzing patterns over time and across genres.
Localization and Revenue: Investigate the relationship between the number of translations and worldwide revenue to assess the impact of localization on a film’s global success.
Real Story Identification: Calculate similarity scores to determine if films linked to real-life events (above a similarity threshold, e.g., 0.77) show stronger box-office performance.
- Step 3: Academy Awards Influence
Impact of Awards: Examine how Academy Awards, particularly Best Picture and actor performance awards, correlate with box-office revenue. Conduct comparative analysis between award-winning films and non-award-winning films, using t-tests or similar statistical methods.
- Step 4: Diversity Analysis
Gender and Ethnicity Diversity: Create metrics for each movie’s gender and ethnicity diversity. Assess how these diversity metrics correlate with box-office revenue, exploring whether films with greater diversity yield higher financial success.
Cross-Analysis with Issuing Country: Integrate diversity metrics with the issuing country data to refine insights on how diversity influences box-office performance across different regions.
- Step 5: Topic Analysis
NLP Topic Classification: Use an NLP model to classify movie summaries into common themes (e.g., romance, action, drama) and analyze how these topics affect box-office success. Determine if certain topics consistently align with higher revenue across different historical periods.
Step 6: Final Analysis and Documentation
Interpret Results: Summarize insights from each analysis step, identifying the factors most strongly associated with box-office success.
Visualizations and Presentation: Create visualizations to present your findings clearly, supporting your conclusions with data-driven insights for each factor analyzed.

# Contribution :
- Elyes: Responsible for data pre-processing, including cleaning metadata, removing irrelevant entries, and preparing localization data for analysis.
- Najmedinne: Analyzes metadata factors such as release season, genre, actor demographics, and the correlation between localization and revenue.
- Lucas: Focuses on plot analysis using NLP to tokenize plot summaries, cluster themes, and assess the impact of real-life event connections on box-office performance.
- Myriam: Examines the influence of Academy Awards on box-office revenue, analyzing the impact of Best Picture and acting awards.
- Yassine: Conducts diversity and topic analysis, evaluating the impact of gender and ethnicity diversity and categorizing movie topics to study their effect on revenue.
