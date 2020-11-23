import bs4
import requests
import pandas as pd


# Scrape an article from the Huffington post
def scrape_huffington_post(url: str):
    # Create a headers dictionary so that the request is not refused by the server
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    # Request the article url and store the response
    response = requests.get(url, headers=headers)

    # If the response's status code was not 200 (success), return from the function
    if response.status_code != 200:
        # TODO Log these errors to aid in debugging
        return

    # Parse the response's content with bs4
    soup = bs4.BeautifulSoup(response.content, features='html.parser')

    # Select the first DOM element with the entry__text CSS class
    entry_text = soup.select('.entry__text')[0]

    # Select all of the DOM elements that are children of the entry__text element and that have the
    # content-list-component CSS class
    content = entry_text.select('.content-list-component')

    # Store the full text of each article
    full_text = []

    # Iterate over the selected DOM elements
    for item in content:
        # Iterate over each DOM element contained by the current item
        for el in item.contents:
            if isinstance(el, bs4.NavigableString):
                # If the current element is a NavigableString, strip and store it as the current element's text
                text = el.strip()
            else:
                # Otherwise, strip and store it's text attribute and store it as the current element's text
                text = el.text.strip()

            # Add the current element's text to the list of the current article's text
            if text:
                full_text.append(text)

    # Print the article's full text
    print('\n'.join(full_text))


# Keys are the names of the sources that are supported; values are the functions to call when scraping articles from
# those sources
supported_sources = {
    'Huffington Post': scrape_huffington_post
}


# Scrape all of the articles from supported sources (i.e. a source-specific scraping function is implemented)
def scrape_articles() -> None:
    # Define the path where the csv file containing articles with extraneoues source data removed
    articles_nosrc_path = '../../data/interim/articles_sources_removed.csv'

    # Read the csv file containing the article data to use for scraping
    df = pd.read_csv(articles_nosrc_path)

    # Scrape all of the articles from supported sources
    for source in supported_sources.keys():
        # Locate all of the dataframe entries with the current source
        articles = df.loc[df['source'] == source]

        # Iterate through all of the entries for the current source
        for article in articles.itertuples():
            # Call the appropriate function to scrape each article; the function to be called is associated with the
            # key in the supported_sources dictionary being iterated over in the parent loop
            supported_sources[source](article[1])
