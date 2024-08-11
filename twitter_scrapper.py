import snscrape.modules.twitter as sntwitter
import csv
import time
import os

# Set the folder path
folder_name = 'splitted_data'
folder_path = os.path.join(os.getcwd(), folder_name)

# Create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

query = "(politics OR war) lang:en"
tweet_limit = 200000
batch_size = 10000  # Number of tweets to scrape per request
output_prefix = os.path.join(folder_path, "hashtagless")
output_count = 1

# Scrape tweets in batches
total_scraped = 0
scraped_batch = 0
start_time = time.time()  # Start measuring elapsed time

while total_scraped < tweet_limit:
    print(f"Creating new file after : {time.time()-start_time} from last")
    output_file = f"{output_prefix}_{output_count}.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Tweet Text", "Hashtags"])

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= batch_size:
                break
            print(f"Scraped {total_scraped} tweets.")
            writer.writerow([tweet.user.username, tweet.content, tweet.hashtags])
            total_scraped += 1
            scraped_batch += 1

        output_count += 1

elapsed_time = time.time() - start_time  # Calculate elapsed time

print("Scraping complete.")
print(f"Elapsed time: {elapsed_time} seconds.")
