<<<<<<< HEAD
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

=======
>>>>>>> ae85f1c7826c36be8a717482dcba17c22a800ee7
def categorize_release_season(date):
    """
    Categorize a release date into one of the following categories: Spring, Summer, Holiday, or Other.
    Args:
        date (datetime): The release date of a movie.
        
    Returns:
        str: The category of the release date.
    """
    if date.month in [6, 7, 8]:
        return 'Summer'
    elif date.month in [9, 10, 11]:
        return 'Autumn'
    elif date.month in [1, 2, 12]:
        return 'Winter'
    elif date.month in [3, 4, 5]:
<<<<<<< HEAD
        return 'Spring'
    else:
        return 'NaN'

def extract_info(infos_str):
    """Extracts country names from the 'Movie countries (Freebase ID:name tuples)' column."""
    try:
        return [info.split(":")[1].strip(" }") for info in infoq_str.split(",")]
    except Exception:
        return []

# Extract genres and count occurrences within each interval
def top_n_by_interval(feature,data,n=10):
    df = data.copy()
    top_n = df.value_counts(feature).head(n)
    
    top_order = top_n.index.tolist()
    
    df = df[df[feature].isin(top_order)]
    
    df[feature] = pd.Categorical(df[feature], categories=top_order, ordered=True)
    
    df = df.sort_values(feature)
    
    counts_by_interval = df.groupby(['Year_Interval', feature],observed=False).size().unstack(fill_value=0)
    
    # Create a DataFrame for the top genres in each interval
    top_by_interval = counts_by_interval.apply(lambda x: x.nlargest(n), axis=1)
    
    plot_data = top_by_interval.div(top_by_interval.sum(axis=1), axis=0) * 100
    
    ax = plot_data.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='tab10')
    ax.set_xlabel('Year Interval')
    ax.set_ylabel(f'Percentage of {feature}')
    ax.set_title(f'Top {n} {feature} by 20-Year Intervals (1910-2016)')
    ax.legend(title=f'{feature}', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    return ax
=======
        return 'Spring'
>>>>>>> ae85f1c7826c36be8a717482dcba17c22a800ee7
