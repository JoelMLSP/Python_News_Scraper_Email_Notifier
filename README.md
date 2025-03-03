# News Scraper and Email Notifier

## Overview

This is a simple Python project where I learned how to scrape news from [Hacker News](https://news.ycombinator.com/) and send it as an automated email. The script fetches the latest stories, formats them nicely, and emails them to a recipient using Gmail's SMTP service. 

This project was a fun way to get hands-on experience with web scraping, email automation, and working with environment variables for security. 

## Features

- Scrapes the top news stories from Hacker News.
- Formats the news into a simple HTML email.
- Sends an automated email using Gmail SMTP.
- Uses environment variables to store email credentials securely.

## What I Learned

- **Web Scraping**: Using `requests` to fetch web pages and `BeautifulSoup` to parse HTML.
- **Email Automation**: Sending emails using `smtplib` and `email` libraries in Python.
- **Environment Variables**: Keeping sensitive information like email credentials safe using `dotenv`.

## Requirements

To run this script, you’ll need:

- Python 3.x
- The following Python libraries:
  ```sh
  pip install requests beautifulsoup4 python-dotenv
  ```

## Setup

1. Clone this repo or copy the script.
2. Install the required dependencies (see above).
3. Create a `.env` file in the same directory as the script and add:
   ```sh
   FROM_EMAIL=your_email@gmail.com
   TO_EMAIL=recipient_email@gmail.com
   APP_SPECIFIC_PASSWORD=your_app_password
   ```
   - `FROM_EMAIL`: Your Gmail address (used to send emails).
   - `TO_EMAIL`: Recipient’s email address.
   - `APP_SPECIFIC_PASSWORD`: An app password generated from Google (due to Gmail security restrictions).

## How It Works

1. **Extract News:** The script scrapes Hacker News for the latest stories using `BeautifulSoup`:
   ```python
   def extract_news(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.content, 'html.parser')
       for i, tag in enumerate(soup.find_all('span', attrs={'class': 'titleline'})):
           print(tag.text)  # This prints the extracted titles
   ```
2. **Format the Email:** The news is formatted into an HTML-friendly structure.
3. **Send the Email:** Using Gmail’s SMTP server:
   ```python
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(FROM, PWD)
   server.sendmail(FROM, TO, msg.as_string())
   ```
4. **Secure Authentication:** The script retrieves credentials from the `.env` file.

## Running the Script

Simply run:
```sh
python script.py
```

## Notes

- If using Gmail, you need to enable "App Passwords" instead of using your main password.
- You can set up a **cron job** (Linux/macOS) or a **Task Scheduler** (Windows) to run this script automatically.
- Want to scrape a different website? Modify the `extract_news` function to target another site.

## Final Thoughts

This was a cool project where I got to mix **web scraping, automation, and security best practices**. It’s a great starting point for more advanced automation projects. If you have any ideas or improvements, feel free to contribute!

## Author

Joel El Aziz

