## Anil Katwal, Youtube video description fetching....
from yt_dlp import YoutubeDL
import logging
logging.basicConfig(level=logging.INFO)
def fetch_youtube_info(link):
    try:
        # Using yt_dlp instead of pytube
        ydl = YoutubeDL()
        info = ydl.extract_info(link, download=False)
        # Log information
        logging.info("Title: %s", info['title'])
        logging.info("Views: %s", info['view_count'])
        logging.info("Duration: %s", info['duration'])
        logging.info("Description: %s", info['description'])
        logging.info("Ratings: %s", info.get('average_rating', 'N/A'))

        return info

    except Exception as e:
        logging.error("Error fetching YouTube info: %s", str(e))
        return None

def save_to_file(info, output_file="youtube_info.txt"):
    try:
        # Open the file in write mode
        with open(output_file, "w", encoding="utf-8") as file:
            # Write information to the file
            file.write("Title: {}\n".format(info['title']))
            file.write("Views: {}\n".format(info['view_count']))
            file.write("Duration: {}\n".format(info['duration']))
            file.write("Description: {}\n".format(info['description']))
            file.write("Ratings: {}\n".format(info.get('average_rating', 'N/A')))

        logging.info("Information has been saved to %s.", output_file)
    
    except Exception as e:
        logging.error("Error saving to file: %s", str(e))

if __name__ == "__main__":
    try:
        link = input("Enter link of Youtube video:")
        youtube_info = fetch_youtube_info(link)

        if youtube_info:
            save_option = input("Do you want to save this information to a file? (yes/no): ").lower()
            if save_option == 'yes':
                save_to_file(youtube_info)

    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
