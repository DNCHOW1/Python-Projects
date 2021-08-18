import selenium, requests, time, pprint, re, os, datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

# NOTEEEEEEEEEEEE
# I have to change the way this works, from checking for new opportunities to reminding me to check a spreadsheet whenever new opps show up.


# NOTEEEEE
# THIS SCRIPT RUNS ON WINDOWS TASK SCHEDULER, but it could possibly be run better on a different api







# Twilio - Sample

#os.chdir(os.path.dirname(__file__))
def run():
    past_opps = []
    current_opps = {}

    with open('past_opps.txt', 'r') as f:   # Gets all past opps, and a maybe working cookie
        for line in f:
            past_opps.append(line.strip('\n'))

    def login(): # Logins to x2vol if cookies expire. #########COULD BE IMPROVED IN FUTURE
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path='C:/Users/Shady Name/Downloads/chromedriving/chromedriver.exe', chrome_options=options)
        #driver = webdriver.Chrome(executable_path='C:/Users/Shady Name/Downloads/chromedriving/chromedriver.exe')

        driver.get('https://x2vol.com/Login.html')
        username = driver.find_element_by_id("txtUserName")
        password = driver.find_element_by_id("txtPassword")

        username.send_keys("user")
        password.send_keys('pass')
        driver.find_element_by_class_name("submit").click()

        driver.get('https://x2vol.com/Opportunities/1511380/FindOpportunities')


        cookie_data = driver.get_cookies()
        driver.quit()


        x = {data['name']: data['value'] for data in cookie_data}

        return 'ASP.NET_SessionId={}'.format(x["ASP.NET_SessionId"])

    def get_Opps(session_data): # Gets the current opps and the number of opps
        global number_opps
        soup = BeautifulSoup(session_data.content, 'html.parser')
        number_opps = (soup.find('h2').text)[-3:].strip()

        id_search = re.compile(r'id="(\S+)"')
        for i in soup.find_all(class_='CommunityList'): # The opportunities
            if i.find(class_='orgWidOneSix'):
                mo = id_search.search(str(i)) # The links to opportunities
                opp_name = i.find(class_='blueHedline').text.strip()
                current_opps[opp_name] = mo.group(1)
        print('Data Retrieved')

    def cookie_check(session): # Checks to see if cookies have expired, updates if it has.
        global cookie_header, opp_page
        with open('cookies.txt', 'r') as f: # Gets the cookie
            cookie_header = {'Cookie': f.read().rstrip('\n')}

        r = session.post('https://x2vol.com/post', headers=cookie_header)
        if r.url != 'https://x2vol.com/post':
            print('Error! Expired Cookies!')
            cookie_header = {'Cookie': login()} # If that doesn't work, have to manually get cookies
            session.post('https://x2vol.com/post', headers=cookie_header)
        opp_page = session.get('https://x2vol.com/Opportunities/1511380/FindOpportunities', headers=cookie_header)

        print('Cookies Updated')

    with requests.Session() as session:

        cookie_check(session)
        get_Opps(session_data=opp_page)

        with open('cookies.txt', 'w') as f: # Updates the cookies, if it has changed
            f.write(cookie_header["Cookie"])

        del past_opps[0] # Removes the 1st index, which is the number of oppurtunities. Wouldn't want that being compared with current_opps
        current_opps_names = set(current_opps.keys())
        new_opp_names = current_opps_names.difference(past_opps) # If any current opps are not present in past_opps, new_opp has them
        if new_opp_names: # If the list has names, then this runs
            new_opps = [[opp, current_opps[opp]] for opp in new_opp_names]

            with open('past_opps.txt', 'w') as f: # Adds the # of opps and then the oppurtunities
                f.write(number_opps + '\n')
                for oppurtunities in current_opps:
                    f.write(oppurtunities + '\n')

            def convert_links(link):
                return 'https://x2vol.com/Opportunities/1511380/OpportunityDetails?OppoDetailId={}&Page=FindOpportunity'.format(link[-36:])

            print('New opportunities!')
            new_opps = list(map(lambda oppurtunity: [oppurtunity[0], convert_links(oppurtunity[1])], new_opps))

            time_search = re.compile(r'>(.*)<')
            longest_name = max((len(oppurtunity[0]) for oppurtunity in new_opps)) # oppurtunity[0] is the name of the oppurtunity
            for i in new_opps:
                opp_link = session.get(i[1], headers = cookie_header)
                soup = BeautifulSoup(opp_link.content, 'html.parser')
                i.append([]) # The list of all times that correspond with the oppurtunity
                for y in soup.find_all(class_='dtetwoFiveSix'):
                    for time_raw in y.find_all(class_='evnTeFont'):
                        mo = time_search.search(str(time_raw))
                        time = mo.group(1)
                        i[2].append(time)

            days = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday', '6': 'Sunday'}
            with open('new_opps.txt', 'a') as f:
                for i in new_opps:
                    for times in i[2]: # The list of times
                        weekday = str(datetime.datetime(int(times[6:10]), int(times[:2]), int(times[3:5])).weekday()) # Year, month, and day. All are numbers
                        f.write('{}{}{} ({})\n'.format(i[0], times.rjust((longest_name) - len(i[0]) + 37, '_'), i[1],days[weekday]))
                        # Oppurtunity name, the times(adjusted), what day of the week, and the Am/Pm

            #Twilio
            acc_ = 'Hidden'
            token_ = 'Token'
            client = Client(acc_, token_)
            for opps in new_opps:
                all_times = ', '.join([v + days[str(datetime.datetime(int(v[6:10]), int(v[:2]), int(v[3:5])).weekday())] for v in opps[2]]) # opps[1] is the times
                client.messages.create(
                    to='myphone',
                    from_='twiliophone',
                    body='{}[{}]{}\n'.format(opps[0], all_times, opps[1]) # opps[1] is the link to the oppurtunity
                )


    print('Done')
run()
