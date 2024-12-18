import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

pickle_folder = "../data/pickle/"

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
    