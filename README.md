# The Evolution of Cinema: The Success Story Behind Box-Office Hits (1915-2015)

## Abstract :
This project analyzes the key factors influencing box-office success for films released between 1915 and 2015, seeking to understand how audience preferences and industry trends have evolved over time. We focus on a variety of characteristics—such as genre, release timing(season), localization (number of translations and countries), and lead actors' age and gender-to determine their impact on a film's revenue and ratings. By examining five distinct historical periods, we aim to uncover how shifts in these characteristics correlate with box-office performance. Additionally, we explore genre combinations and actor age pairings to see if certain patterns consistently align with higher revenue. We also assess how localization strategies, like translations into specific languages, have helped films reach a wider audience. This study provides a comprehensive view of the changing dynamics of film success, revealing patterns that reflect both cinematic trends and evolving audience preferences across decades.

## Research Questions : 
### Does the evolution of the success of movies follow a particular trend ?
- How have the highest-grossing films' box office numbers evolved from the inception of cinema until 2015 ? Can we identify clear inflection points ?
- Were there specific periods/time-intervals where film's had more commercial success ? And for critical success (ratings) ?

### Are there patterns/similarity between the evolutions of the key characteristics of film's across history ? 
- Does the release season of a film influence its commercial or critical success ?
- What age range of actors (e.g. kids, young actors, experimented actors, ...) has tended to yield the highest box office numbers in different time periods ? Are younger actors more popular than older ones ? Is it the complete opposite? Does it vary across the years ? Does it differ depending on the gender ?
- Are there genres that have maintained consistent commercial and critical appeal across most time periods ?
- Does releasing a film with more foreign language translations associate with higher worldwide box office revenue?
  
## Datasets :
### Original dataset (CMU Movie Summary): 
  The CMU Movies dataset offers valuable insights into factors affecting box-office performance, covering attributes like genre, release timing, and actor demographics across thousands of films from early cinema through 2015. This data supports our analysis of trends over time, helping us explore how audience preferences and industry practices have evolved. Specifically, it enables us to examine the impact of genres, actor age and gender, and localization on success. The dataset’s depth makes it essential for identifying patterns and answering questions about film success dynamics over the past century.

### Additional Dataset :
- IMDb dataset : The IMDb dataset provides valuable ratings and voting data that can serve as an alternative metric for measuring a movie's success, beyond traditional metrics like box office revenue. By using IMDb ratings (average viewer scores out of 10) and the number of votes a movie has received, we can develop a “popularity” metric that reflects audience reception and engagement, which can highlight successful films that may not have been financial hits but were well-received by viewers.
When using IMDb data for such analyses, a key challenge is integrating it with other datasets, like the CMU movies dataset in our case. For instance, differences in naming conventions, movie release years, and sometimes even mismatches in genre categories mean that titles may not match directly. The title.basics and title.ratings tables provide most of the rating information, and most of the work is filtering and cleaning this data.
Despite these constraints, with robust preprocessing, the IMDb ratings data allows us to examine audience-based success and trends that complement or even differ from revenue-focused metrics, offering a broader perspective on a movie's impact.

## Methods :
- T-tests: This statistical tool can compare the means of two groups to determine if they are significantly different. In your analysis, t-tests could help evaluate which factors—such as release season, genre, or localization (e.g., high vs. low number of translations)—significantly impact box-office revenue. By identifying these differences, you can determine which characteristics have a notable effect on a film's financial success.

- Pearson Correlation Coefficient (PCC): PCC assesses the linear relationship between variables, helping you pinpoint which factors, such as lead actor age, genre, or localization, have the strongest correlation with box-office revenue.

- Linear Regression: We will use this technique to model the relationship between box-office revenue or average rating (dependents variables) and multiple independent variables, such as genre, actor age and gender, localization, and release timing. By fitting a linear equation, linear regression allows you to predict a film's revenue or rating based on its characteristics, providing insights into how different factors work together to drive commercial and critical success.

## Project Plan :
- **Step 1:** Data Pre-Processing and cleaning
In this step, we focus on preparing the data for analysis. This involves cleaning the datasets by removing missing values, duplicates, or inconsistencies that could skew the results. We also standardize data formats, such as dates, names, or categories, to ensure consistency and make the data easier to work with. The goal is to make the data ready for exploration and analysis, ensuring its quality and reliability. This process is crucial to ensure that the analysis that follows is built on solid foundations, leading to accurate and trustworthy conclusions.

- **Step 2:** Analyzing and plotting characteristics individually
The goal is to get a better understanding of the behaviour of each characteristics across the periods. We examine the movie's features, such as their genres, release years, ratings or box office performance (same for the actor's features such as age and gender). We analyze the distribution of these features and visualize them using various plots, such as histograms, bar charts, or scatter plots. This helps us to identify patterns, trends, or outliers in the data. By focusing on each characteristic separately, we gain insights into how different movie attributes behave, laying the groundwork for more complex analysis later on.

- **Step 3:** Identifying Key Relationships and Patterns
We look at how different attributes interact with each other. For example, we can examine correlations between factors such as movie ratings and box office earnings, or how the genre of a movie affects its overall reception (e.g., ratings, number of reviews).
To achieve this, we use methods like correlation analysis, cross-tabulations, and pair plots to detect significant relationships in the data. This step helps to identify the most important variables that influence the success or failure of a movie and allows us to focus on these patterns for the story we want to tell.

- **Step 4:** Advanced Data Analysis & Modeling
We dive deeper into more advanced analyses by using a predictive modeling to estimate the potential box office earnings of a movie based on its genre, cast, and other features. Machine learning algorithms like linear regression, decision trees, or clustering could be used to segment movies based on their features and predict performance metrics. This step is about turning our observations into actionable insights. If we were to predict future trends in the movie industry or determine which characteristics are most likely to result in success, this is where we would apply more sophisticated models.

- **Step 5:** Building the Data Story and Visualization

## Proposed timeline
- 15.11.2024 : Step 1 & 2

*(29.11.2024 : Homework 2)*
- 06.12.2024 : Step 3
- 13.12.2024 : Step 4
- 20.12.2024 (Deadline Milestone 3) : Step 5

## Team Organization :
- Elyes Trabelsi: Step 1 & 3 
- Najmeddine Abbassi: Step 1, 2 & 4
- Lucas Simonnet: Step 1 & 3 
- Annaelle Benlamri: Step 1, 2 & 4
- Yassine Mamlouk: Step 1, 2 & 3
