import requests
from bs4 import BeautifulSoup

def main():
    # Get URL from user input
    url = input("Enter the URL: ")
    
    # If you want to grab URLs in other ways, change line 6 to a comment and then uncomment other options below
    # url = 'full_url'
    # url = 'name_of_file'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all paragraphs in the HTML
        paragraphs = soup.find_all('p')
            
        if paragraphs:
            article_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

            # Write to file
            with open("test.txt", 'a') as f:
                f.write(article_text)
        else:
            print("Couldn't find any paragraphs in the article.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
