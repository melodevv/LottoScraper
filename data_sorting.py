from datetime import datetime


def sort_date(date_html):
    dates = []
    draws = []

    for i in range(len(date_html)):
        # Remove html tags and attributes
        date = date_html[i].text
        date = date.split()

        # Remove day of the week
        date.pop(0)

        # Get the draw name:
        draw_name = date.pop()

        # Get the date in DateTime
        date[0] = datetime.strptime(date[0], '%d').day
        date[1] = datetime.strptime(date[1], '%B').month
        date[2] = datetime.strptime(date[2], '%Y').year

        # Add to the lists
        dates.append(datetime(date[2], date[1], date[0]).strftime('%Y%m%d'))
        draws.append(draw_name)

    return dates, draws


def sort_results(results_html):
    list_results = []
    results = []
    count = 0

    for i in results_html:
        for j in i.find_all('td'):
            if j.text != ' ':
                list_results.append(j.text)
        results.insert(-1, list_results)
        count += 1
        list_results = []

    return results
