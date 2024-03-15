# This script demonstrates the Single Responsibility Principle (SRP) by defining a class responsible for processing raw data.
# It utilizes the requests library to fetch HTML data from a specified URL and BeautifulSoup for parsing HTML content.

import requests
from bs4 import BeautifulSoup

class DataProcessor:
    """Module for processing raw data."""

    def process_data(self, url):
        """Processes raw HTML data and returns the main body paragraph."""
        # Fetch HTML content from the specified URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all paragraphs in the HTML
            paragraphs = soup.find_all('p')
        
        # Initialize variable to store the main article text
        article_text = ""
        
        # Concatenate text from all paragraphs to form the main body text
        if paragraphs:
            article_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])
            
        return article_text
