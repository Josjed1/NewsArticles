import requests
from bs4 import BeautifulSoup

def main():
    # Get URL from user input
    url = input("Enter the URL: ")
    
    #If you want to grab urls others ways, change line 6 to a commit and then unhashtag the other options below
    #url = 'full_url'
    
    #url = name of file
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_body = soup.find('div', class_='article-body')

        if article_body:
            article_text = article_body.get_text()    

            # Split the text into words
            words = article_text.split()

            # Define the maximum number of words per line
            max_words_per_line = 20

            # Write to file with a new line after every 30 words
            with open("output_onepiece.txt", 'a') as f:
                for i in range(0, len(words), max_words_per_line):
                    line = ' '.join(words[i:i+max_words_per_line])
                    f.write(line + '\n')

        else:
            print("Couldn't find the article body element.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    
    main()
