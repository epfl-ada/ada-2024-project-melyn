import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

pickle_folder = "../data/pickle/"

genres_dict = {
    "Action": ["Ninja movie", "Escape Film", "Spy", "Cavalry Film", "Martial Arts Film", "Gangster Film", "Sword and Sandal", "Swashbuckler films", "Samurai cinema", "Combat Films", "Action/Adventure", "Action Comedy", "Action Thrillers", "Glamorized Spy Film", "Superhero movie", "Sword and sorcery", "Space western", "Adventure", "Outlaw biker film", "Parkour in popular culture", "Chase Movie", "Superhero", "Biker Film", "Auto racing", "Boxing", "Action"],
    "Adventure": ["Coming-of-age film", "Horse racing", "Jungle Film", "Road movie", "Family-Oriented Adventure", "Fantasy Adventure", "Costume Adventure", "Science fiction Western", "Animal Picture", "Extreme Sports", "Fantasy", "Adventure Comedy", "Beach Film", "Travel", "Wuxia", "Foreign legion"],
    "Animated": ["Animated Musical", "Animated cartoon", "Computer Animation", "Stop motion", "Clay animation", "Anime", "Supermarionation", "Animation"],
    "Black-and-white": ["Black-and-white"],
    "Bollywood":["Bollywood"],
    "Chinese Movies":["Chinese Movies"],
    "Comedy": ["Comedy-drama", "Slapstick", "Gross out", "Comedy of Errors", "Comedy of manners", "Domestic Comedy", "Comedy film", "Workplace Comedy", "Comedy horror", "Parody", "Courtroom Comedy", "Musical comedy", "Romantic comedy", "Tragicomedy", "Comedy Western", "Heavenly Comedy", "Sex comedy", "Stand-up comedy", "Gross-out film", "Screwball comedy", "Black comedy", "Fantasy Comedy", "Comedy Thriller", "Buddy cop", "Satire", "Comedy Thriller", "Stoner film", "Humour", "Absurdism", "Bloopers & Candid Camera", "Media Satire", "Ealing Comedies", "British New Wave", "Comdedy", "Political satire", "Mumblecore", "Slapstick", "Camp", "Mockumentary", "Buddy film", "Female buddy film", "Hip hop movies", "Comedy"],
    "Crime": ["Master Criminal Films", "Crime Fiction", "Crime Drama", "Detective fiction", "Crime", "Neo-noir", "Gangster Film", "Heist", "Law & Crime", "Crime Thriller", "Suspense", "Detective", "Whodunit", "Crime Comedy", "Caper story", "Conspiracy fiction", "Blaxploitation", "Outlaw"],
    "Disaster": ["Natural disaster", "Doomsday film", "Road-Horror", "Disaster", "Nuclear warfare", "Plague"],
    "Documentary": ["Documentary", "Rockumentary", "World History", "Social issues", "Docudrama", "Hagiography", "Educational", "Essay Film", "Nature", "Animals", "Archives and records", "Archaeology"],
    "Drama": ["Family Drama", "Biographical film", "Melodrama", "Marriage Drama", "Psychological thriller", "Kitchen sink realism", "Historical drama", "Political drama", "Romantic drama", "Addiction Drama", "Inspirational Drama", "Social problem film", "Legal drama", "Courtroom Drama", "Psychological thriller", "Slice of life story", "Childhood Drama", "Interpersonal Relationships", "Coming of age", "Tragedy", "Feminist Film", "Star vehicle", "Americana", "Mumblecore", "Family Film", "Medical fiction", "Journalism", "Ensemble Film", "Family & Personal Relationships", "Race movie", "LGBT", "Biopic [feature]", "Drama", "Christmas movie", "Indie", "Biography", "Private military company", "Women in prison films", "Prison"],
    "Experimental": ["Surrealism", "Avant-garde", "Mondo film", "Absurdism", "Expressionism", "Experimental film", "Existentialism", "Dogme 95", "Czechoslovak New Wave"],
    "Fantasy": ["Children's Fantasy", "Romantic fantasy", "Fantasy Drama", "Mythological Fantasy", "Sword and sorcery films", "Supernatural", "Alien Film", "Heaven-Can-Wait Fantasies", "Space opera", "Alien invasion", "Fantasy Adventure", "Revisionist Fairy Tale", "Fairy tale", "Gothic Film", "Period Horror", "Monster"],
    "Historical": ["Historical fiction", "Historical Epic", "Biographical film", "Costume drama", "World History", "Period piece", "British Empire Film", "The Netherlands in World War II", "Cold War", "Gulf War", "Early Black Cinema", "History", "Americana", "Movies About Gladiators"],
    "Horror": ["Horror", "Sci-Fi Horror", "Psychological horror", "Natural horror films", "Creature Film", "Splatter film", "Demonic child", "Zombie Film", "Monster movie", "Vampire movies", "Werewolf fiction", "Costume Horror", "Road-Horror", "Horror Comedy", "Slasher", "Haunted House Film", "Psycho-biddy", "Giallo", "B-movie", "Cult", "Illnesses & Disabilities", "Monster"],
    "Japanese Movies": ["Japanese Movies"],
    "Musical": ["Operetta", "Animated Musical", "Musical comedy", "Backstage Musical", "Courtroom Comedy", "Musical Drama", "Dance", "Jukebox musical", "Concert film", "Singing cowboy", "Music", "Instrumental Music", "Musical"],
    "Noir": ["Neo-noir", "Film noir", "Future noir", "Mystery", "Pre-Code"],
    "Other": ["Other"],
    "Pornographic": ["Softcore Porn", "Sexploitation", "Erotica", "Gay pornography", "Hardcore pornography", "Erotic Drama", "Erotic thriller", "Pinku eiga", "Pornographic movie", "Pornography", "Gay"],
    "Propaganda": ["Propaganda film", "Political cinema", "Social problem film"],
    "Romance": ["Romance Film", "Romantic comedy", "Romantic drama", "Romantic fantasy", "Gay Themed", "Gay Interest", "LGBT", "Interpersonal Relationships", "Homoeroticism", "Buddy film"],
    "Science Fiction": ["Cyberpunk", "Sci-Fi Horror", "Sci-Fi Thriller", "Time travel", "Alien Film", "Space opera", "Apocalyptic and post-apocalyptic fiction", "Dystopia", "Alien invasion", "Science Fiction", "Steampunk", "Space western", "Sci-Fi Adventure", "Future noir", "Computers", "Z movie", "Kafkaesque", "Sci Fi Pictures original films"],
    "Silent film":["Silent film"],
    "Sports":["Sports"],
    "Teen": ["Teen", "Coming-of-age film", "School story", "Juvenile Delinquency Film", "Children's", "Children's/Family"],
    "Thriller": ["Psychological thriller", "Crime Thriller", "Erotic thriller", "Political thriller", "Action Thrillers", "Suspense", "Thriller", "Erotic thriller", "Conspiracy fiction"],
    "War": ["War film", "Anti-war film", "Combat Films", "Gulf War", "The Netherlands in World War II", "Anti-war"],
    "Western": ["Revisionist Western", "Acid western", "Singing cowboy", "Indian Western", "Hybrid Western", "Epic Western", "B-Western", "Spaghetti Western", "Western", "Outlaw"],
    "World cinema": ["World cinema"]
}

def clean_genres():
    '''
    Create a simplified DataFrame by grouping subgenre columns into broader genre categories.
    Each broader genre will have its own column, set to `True` if any of its corresponding subgenres 
    in the original DataFrame are `True`.
    
    Arguments:
        df: DataFrame containing subgenres
    Returns:
        df_merged: DataFrame containing genres
    '''
    with open(pickle_folder + 'movies_genres_exploded.p', 'rb') as f:
        df = pickle.load(f)
    dummies = pd.get_dummies(df['Genres'])
    df = pd.concat([df.drop(columns='Genres'),dummies],axis=1
                    ).groupby('Wikipedia_movie_ID', as_index=False).max()
    df_id = df[['Wikipedia_movie_ID','Movie_name','Movie_box_office_revenue','Year','Year_Interval','nb_of_Genres']].copy()
    for genre, subgenres in genres_dict.items():
        df_id[f"Genre_{genre}"] = df[subgenres].any(axis=1)
    return df_id

def categorize_release_season(date):
    """
    Categorize a release date into one of the following categories: Spring, Summer, Holiday, or Other.
    Args:
        date (datetime): The release date of a movie.      
    Returns:
        str: The category of the release date.
    """
    if date in [6, 7, 8]:
        return 'Summer'
    elif date in [9, 10, 11]:
        return 'Autumn'
    elif date in [1, 2, 12]:
        return 'Winter'
    elif date in [3, 4, 5]:
        return 'Spring'
    else:
        return 'NaN'

def clean_columns(feature,top_size,prefix=None):
    with open(pickle_folder + f'movies_{feature.lower()}_exploded.p', 'rb') as f:
        df = pickle.load(f)
    top = df.value_counts(feature).head(top_size).index.to_list()
    df.loc[~df[feature].isin(top),feature] = "Other"
    dummies = pd.get_dummies(df[feature],prefix=prefix)
    df = pd.concat([df.drop(columns=feature),dummies],axis=1
                    ).groupby('Wikipedia_movie_ID', as_index=False).max()
    if feature=="Languages":
        df.columns = [x.lower().replace(" language","") if x.lower().endswith("language") 
                      else x.lower() if x.lower().startswith("lang_") else x 
                      for x in df.columns]
    return df

def dropempty(df,feature):
    """
    Drop all the rows containg empty list for the column 'feature'
    Args:
        feature (str): The feature to be analyzed.
        df (DataFrame): The prepared DataFrame
    Returns:
        DataFrame: A filtered DataFrame containing only the rows with one or more element in the column 'feature'.
        N: Number of rows dropped.
    """
    len_before = len(df[feature])
    df = df[df[feature].apply(lambda x: len(x) > 0)]
    len_after = len(df[feature])
    return df, len_before-len_after

def exploded_format(feature,df,path):
    """
    Save an exploded version of the dataframe of the desired feature 
    Args:
        feature (str): The feature to be analyzed.
        df (DataFrame): The prepared DataFrame
    """
    df_exploded = df.explode(feature)[['Wikipedia_movie_ID','Movie_name','Movie_box_office_revenue','Year','Year_Interval',f'nb_of_{feature}',feature]]
    pickle.dump( df_exploded, open(path,"wb") )
    display(df_exploded.value_counts(feature))

def extract_info(infos_str):
    """
    Extracts country names from the 'Movie countries (Freebase ID:name tuples)' column.
    Args:
        infos_str (str): The string containing the country information.
    Returns:
        list: A list of country names.    
    """
    try:
        return [info.split(":")[1].strip(' }"') for info in infos_str.split(",")]
    except Exception:
        return []

def prepare_top_n_data(feature, data, n=10):
    """
    Prepares the data by selecting the top n features and ordering them.
    Args:
        feature (str): The feature to be analyzed.
        data (DataFrame): The data to be analyzed.
        n (int): The number of top features to be considered.
    Returns:
        DataFrame: A filtered DataFrame containing only the top n features.
    """
    df = data.copy()
    top_n = df[feature].value_counts().head(n)
    top_order = top_n.index.tolist()
    
    df = df[df[feature].isin(top_order)]
    df[feature] = pd.Categorical(df[feature], categories=top_order, ordered=True)
    
    return df

def top_n_average_rating(feature, data, n=10):
    """
    Plots the top n features by average rating for the entire period.
    Args:
        feature (str): The feature to be analyzed.
        df (DataFrame): The prepared DataFrame with top n features.
        n (int): The number of top features to be considered.
    Returns:
        ax: The plot of the top n features by average rating.
    """
    df = prepare_top_n_data(feature, data, n)
    avg_revenue_by_genre = df.groupby(feature,observed=False)['averageRating'].mean().nlargest(n)
    
    ax = avg_revenue_by_genre.plot(kind='bar', figsize=(8, 5), colormap='tab10')
    ax.set_xlabel(feature)
    ax.set_ylabel('Average IMDb Rating')
    ax.set_title(f'Top {n} {feature} by Average IMDb Rating (1915-2015)')
    plt.tight_layout()
    
    return ax

def top_n_by_interval(feature, data, n=10, revenue=False):
    """
    Plots the top n features by 20-year intervals, either by count or by average revenue.
    Args:
        feature (str): The feature to be analyzed.
        df (DataFrame): The prepared DataFrame with top n features.
        n (int): The number of top features to be considered.
        revenue (bool): Whether to calculate by revenue or count.
    Returns:
        ax: The plot of the top n features by 20-year intervals.
    """
    df = prepare_top_n_data(feature, data, n)
    if revenue:
        counts_by_interval = df.groupby(['Year_Interval', feature],observed=False)['Movie_box_office_revenue'].mean().unstack(fill_value=0)
    else:
        counts_by_interval = df.groupby(['Year_Interval', feature],observed=False).size().unstack(fill_value=0)
    
    top_by_interval = counts_by_interval.apply(lambda x: x.nlargest(n), axis=1)
    plot_data = top_by_interval.div(top_by_interval.sum(axis=1), axis=0) * 100

    ax = plot_data.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='tab10')
    ax.set_xlabel('Year Interval')
    title_revenue = 'Average Box Office Revenue' if revenue else 'Occurrences'
    ax.set_title(f'Top {n} {feature} by {title_revenue} by 20-Year Intervals (1915-2015)')
    ax.legend(title=f'{feature}', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    return ax


def top_n_total_revenue(feature, data, n=10):
    """
    Plots the top n features by average box office revenue for the entire period.
    Args:
        feature (str): The feature to be analyzed.
        df (DataFrame): The prepared DataFrame with top n features.
        n (int): The number of top features to be considered.
    Returns:
        ax: The plot of the top n features by average box office revenue.
    """
    df = prepare_top_n_data(feature, data, n)
    avg_revenue_by_genre = df.groupby(feature,observed=False)['Movie_box_office_revenue'].mean().nlargest(n)
    
    ax = avg_revenue_by_genre.plot(kind='bar', figsize=(8, 5), colormap='tab10')
    ax.set_xlabel(feature)
    ax.set_ylabel('Average Box Office Revenue')
    ax.set_title(f'Top {n} {feature} by Average Box Office Revenue (1915-2015)')
    plt.tight_layout()
    
    return ax
    