import requests
from bs4 import BeautifulSoup
from data_sorting import sort_date, sort_results
import json


def main():
    # Get url for the website to scrape
    url = "https://www.lotteryextreme.com/49s/results"
    r = requests.get(url)

    # Code executes when the request response is 200
    if r.status_code == 200:
        day_results = {}

        soup = BeautifulSoup(r.text, 'lxml')

        # Get the table headings and Get
        # the results.
        # The two variables are parallel
        # to each other.
        date_html = soup.find_all('td', class_='lotterygame2')
        results_html = soup.find_all('table', class_='results2')

        # Send the extracted data to the
        # Functions to be sorted and cleaned.
        # These two lists are parallel
        dates, draws = sort_date(date_html)
        results = sort_results(results_html)

        # Create the dictionary with the dates
        # as the keys and their value being a map
        for j in range(len(dates)):
            if dates[j] not in day_results.keys():
                day_results[dates[j]] = {}

        # Sort the draws and results according to
        # the dates.
        for key in day_results.keys():
            today_dic = {}
            for j in range(len(dates)):
                if key == dates[0]:
                    today_dic[draws[0]] = results[0]
                    results.pop(0)
                    dates.pop(0)
                    draws.pop(0)
                else:
                    break
            # Add the current date key results to dic
            day_results[key] = today_dic

        # convert the day_results to json file
        with open("results.json", "w") as outfile:
            json.dump(day_results, outfile)
            print("File Created")


main()
