import requests

def print_grid_from_google_doc(url):
    # Fetch the document data
    response = requests.get(url)
    data = response.text.splitlines()
    
    # Create a dictionary to store characters at specific positions
    grid = {}
    max_x = max_y = 0
    
    # Parse each line to extract coordinates and characters
    for line in data:
        if line.strip():  # Skip empty lines
            x, y, char = line.split()
            x, y = int(x), int(y)
            grid[(x, y)] = char
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    
    # Print the grid
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += grid.get((x, y), ' ')
        print(row)

# Test the function with the provided URL
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
print_grid_from_google_doc(url)
