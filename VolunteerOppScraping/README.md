# Volunteer Opportunity Scraping
During my high school days, there were volunteering opportunities that would show up on x2vol. The opportunities were limited in registration and would often fill up quickly. Thus, this program scrapes the x2vol webpage frequently for new opportunities, collecting the opportunity’s data as well as notifying me through text should a new one appear.

Windows task scheduler would run this script every 15 minutes to scrape a new opportunity's name, date, and time period. There were cases where multiple dates and time periods were associated to the opporunity, but it would just be handled like a single case (breaks texting a little, as it would display the incorrect weekday given multiple dates). The data would be stored in a file that could be compared to each subsequent run of the program.

In addition, once the data is scraped, the info would be sent to my phone through the TWILIO api. By the end of my TWILIO free trial, I had sent about 600 messages in the span of ~2 years. Below, you can see some opportunities out of the 275 ones scraped between Aug. 11, 2017 and Jul. 9, 2019.
![Scrape_Logs](https://user-images.githubusercontent.com/70815649/131605496-334d6fd9-d52f-4874-a2c8-0dc601f9cda6.JPG)
![image](https://user-images.githubusercontent.com/70815649/131605628-0f8ae38a-31fa-46b9-a48b-adec14c0fa7f.png)
