import requests
from bs4 import BeautifulSoup

def fetch_data_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return response.text

def parse_data(text):
    soup = BeautifulSoup(text, 'html.parser')
    
    # Print the HTML to debug
    print("Fetched HTML content:")
    print(soup.prettify()[:2000])  # Print the first 2000 characters for review
    
    table = soup.find('table')
    if not table:
        raise ValueError("No table found in the HTML content")

    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 3:
            try:
                x = int(cols[0].text.strip())
                y = int(cols[1].text.strip())
                char = cols[2].text.strip()
                data.append((x, y, char))
            except ValueError:
                continue  # Skip rows with invalid data

    return data

def print_grid_from_google_doc(url):
    html_text = fetch_data_from_url(url)
    data = parse_data(html_text)
    
    if not data:
        print("No valid data found in the document.")
        return

    # Determine grid size
    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, y, _ in data)
    
    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill grid with characters from data
    for x, y, char in data:
        if 0 <= x <= max_x and 0 <= y <= max_y:
            grid[y][x] = char

    # Print the grid
    for row in grid:
        print(''.join(row))

# Replace with the actual URL
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
print_grid_from_google_doc(url)
