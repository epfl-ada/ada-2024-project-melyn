Your README.md should contain:
- Title
- Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Research Questions: A list of research questions you would like to address during the project.
- Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
- Methods
- Proposed timeline
- Organization within the team: A list of internal milestones up until project Milestone P3.
- Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

## Abstract :
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
- Original dataset (CMU Movie Summary): 
  The CMU Movies dataset is a rich resource for examining factors that may influence a film's box-office performance, especially with a focus on diverse characteristics such as genre, release timing, and actor demographics. This dataset includes detailed metadata for thousands of films, including information on genres, lead actors, release years, and localization data like the number of translations available for each movie. By capturing a wide span of years from the early days of cinema through 2016, the dataset allows us to analyze trends and shifts over distinct historical periods, aligning with our project’s aim to explore how audience preferences and industry practices have evolved over time.
In particular, the CMU Movies dataset aids in addressing questions about the impact of genres across different decades, the role of actor age and gender in a film’s success, and the influence of localization on reaching global audiences. For example, the dataset’s information on translations can help determine if movies translated into multiple languages perform better internationally, a factor we aim to correlate with box-office revenue. Additionally, the dataset’s breakdown of genres and actor demographics enables us to explore combinations of these factors—like specific genre pairings or actor age ranges—that might align with higher revenue during specific periods. Overall, the CMU Movies dataset is foundational for our project, providing the essential data needed to examine long-term patterns and answer complex questions about the changing dynamics of film success across the past century.

- # Additional :
- IMDb dataset : The IMDb dataset provides valuable ratings and voting data that can serve as an alternative metric for measuring a movie's success, beyond traditional metrics like box office revenue. By using IMDb ratings (average viewer scores out of 10) and the number of votes a movie has received, we can develop a “popularity” metric that reflects audience reception and engagement, which can highlight successful films that may not have been financial hits but were well-received by viewers.
When using IMDb data for such analyses, a key challenge is integrating it with other datasets, like the EMU movies dataset. For instance, differences in naming conventions, movie release years, and sometimes even mismatches in genre categories mean that titles may not match directly. Additionally, IMDb titles may have alternate versions or regional variations, so we have to carefully align these records to prevent duplicating or missing films during merging. The title.basics and title.ratings tables provide most of the rating information, but filtering and cleaning this data, such as removing duplicate titles or aligning names, can be time-consuming.
Despite these constraints, with robust preprocessing, the IMDb ratings data allows us to examine audience-based success and trends that complement or even differ from revenue-focused metrics, offering a broader perspective on a movie's impact.

- Wikidata Ca a voir vraiment Grosse hésitation mais grosse flemme aussi.

