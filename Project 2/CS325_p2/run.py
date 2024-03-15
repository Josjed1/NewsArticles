# Collects data from a specified URL, processes it, and saves both raw and processed data into files.

# Import necessary modules
from module_1.data_processor import DataProcessor
from module_2.data_collector import DataCollector

# Set the URL to collect data from
url = 'https://www.foxnews.com/world/us-taxpayer-funded-un-agencys-long-history-enabling-hamas-exposed'

def main():
    # Use data collector to fetch data from the URL
    data_collector = DataCollector()
    raw_data = data_collector.collect_data(url)
    
    # Call raw print function
    raw_print(raw_data)

    # Use data processor to process the raw data
    data_processor = DataProcessor()
    processed_data = data_processor.process_data(raw_data)
    
    # Call process print function
    process_print(processed_data)

def raw_print(raw_data):
    # Save raw data to the 'raw' folder
    raw_file_path = 'Data/raw/raw_filename.txt'
    with open(raw_file_path, 'w') as raw_file:
        raw_file.write(raw_data)
    print(f"Raw data collected and saved at {raw_file_path}")

def process_print(processed_data):
    # Save processed data to the 'processed' folder
    processed_file_path = 'Data/processed/processed_filename.txt'
    with open(processed_file_path, 'w') as processed_file:
        processed_file.write(processed_data)
    print(f"Processed data saved at {processed_file_path}")

if __name__ == "__main__":
    main()
