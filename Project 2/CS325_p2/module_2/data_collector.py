# This script demonstrates the Single Responsibility Principle (SRP) by defining a class responsible for collecting data from a web page.
# It utilizes the requests library to fetch HTML content from a specified URL.

import requests

class DataCollector:
    """Module for collecting data from a web page."""

    def collect_data(self, url):
        """Collects data from the specified URL."""
        # Fetch HTML content from the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            html_content = response.text
        else:
            # Raise an exception if fetching HTML content fails
            raise Exception(f"Failed to fetch HTML from URL. Status Code: {response.status_code}")

        # Debug print to display fetched HTML content
        print("HTML Content:", html_content)

        # Extract body text from HTML content
        body_text = self.extract_body_text(html_content)

        # Debug print to display extracted body text
        print("Extracted Body Text:", body_text)

        return body_text

    def extract_body_text(self, html_content):
        """Extracts body text from HTML content."""
        # Your extraction logic here (using BeautifulSoup or other libraries)
        # For demonstration, simply returning the HTML content as is
        return html_content
