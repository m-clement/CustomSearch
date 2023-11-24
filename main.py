import requests

def get_ceo_image(company):
    API_KEY = open('API_KEY').read().strip()
    SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read().strip()

    query = f'{company} CEO'

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        results = response.json()

        if 'items' in results:
            return results['items'][0]['link']
        else:
            return "No results found"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
company = input('Enter a company name: ')
print(get_ceo_image(company))
