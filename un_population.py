'''
Importing Libraries
'''
import csv
import matplotlib.pyplot as plt


def india_population():
    '''
    Plotting Indian population over the years
    '''
    with open("population-estimates_csv.csv", encoding="utf8") as csvfile:
        pop_reader = csv.DictReader(csvfile, delimiter=",")
        india_population_estimate = {}
        for pop in pop_reader:
            country = pop["Region"]
            if country == "India":
                year = int(pop["Year"])
                india_population_estimate[year] = float(pop["Population"])

        # plot bar chart for population of India vs years
        plt.bar(india_population_estimate.keys(), india_population_estimate.values())
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title("Population of India")
        plt.show()


def pop_asean_2014():
    '''
    Population of ASEAN Countries in 2014
    '''
    with open("population-estimates_csv.csv", "r", encoding="utf8") as csvfile:
        pop_asean_reader = csv.DictReader(csvfile, delimiter=",")

        asean_pop_list = {}
        asean_country_list = [
            "Brunei Darussalam",
            "Cambodia",
            "Indonesia",
            "Lao People's Democratic Republic",
            "Malaysia",
            "Myanmar",
            "Philippines",
            "Singapore",
            "Thailand",
            "Viet Nam",
        ]

        for asean in pop_asean_reader:
            country = asean["Region"]
            if country in asean_country_list:
                year = int(asean["Year"])
                if year == 2014:
                    asean_pop_list[country] = float(asean["Population"])

        # plot bar chart for population of ASEAN vs year 2014
        plt.bar(asean_pop_list.keys(), asean_pop_list.values())
        axes = plt.gca()
        plt.xlabel("country")
        plt.ylabel("Population")
        plt.title("Population of ASEAN in 2014")
        plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment="right")
        plt.tight_layout()
        plt.show()


def total_population_saarc_every_year():
    '''
    Population of SAARC countries
    '''
    with open("population-estimates_csv.csv", "r", encoding="utf8") as csvfile:
        total_pop_reader = csv.DictReader(csvfile, delimiter=",")
        saarc_pop_list = {}
        saarc_country_list = [
            "Bangladesh",
            "Bhutan",
            "India",
            "Maldives",
            "Nepal",
            "Pakistan",
            "Sri Lanka",
            "Afghanistan",
        ]

        for saarc in total_pop_reader:
            year = int(saarc["Year"])
            if year not in saarc_pop_list:
                saarc_pop_list[year] = 0
                country = saarc["Region"]
                if country in saarc_country_list:
                    saarc_pop_list[year] += float(saarc["Population"])
            else:
                country = saarc["Region"]
                if country in saarc_country_list:
                    saarc_pop_list[year] += float(saarc["Population"])

        # plot bar chart for population of SAARC vs years
        plt.bar(saarc_pop_list.keys(), saarc_pop_list.values())
        axis = plt.gca()
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.setp(axis.get_xticklabels(), rotation=30, horizontalalignment="right")
        plt.tight_layout()
        plt.title("Population of SAARC")
        plt.show()


def grouped_asean_pop_2004_to_2014():
    '''
    Grouped bar chart of ASEAN countries from 2004 to 2014
    '''
    with open("population-estimates_csv.csv", "r", encoding="utf8") as csvfile:
        country_reader = csv.DictReader(csvfile, delimiter=",")

        asean_pop_list = {}
        asean_country_list = [
            "Brunei Darussalam",
            "Cambodia",
            "Indonesia",
            "Lao People's Democratic Republic",
            "Malaysia",
            "Myanmar",
            "Philippines",
            "Singapore",
            "Thailand",
            "Viet Nam",
        ]

        for country in country_reader:
            country_name = country["Region"]
            if country_name in asean_country_list:
                year = int(country["Year"])
                if year >= 2004 and year <= 2014:
                    if year not in asean_pop_list:
                        asean_pop_list[year] = []
                        asean_pop_list[year].append(
                            (country_name, float(country["Population"]))
                        )
                    else:
                        asean_pop_list[year].append(
                            (country_name, float(country["Population"]))
                        )

        print(asean_pop_list)
        # Create a list of years
        years = list(asean_pop_list.keys())
        print(years)

        # Create a list of population data for each country
        country_data_list = []
        for i in range(len(asean_country_list)):
            country_list = []
            for year in years:
                country_list.append(asean_pop_list[year][i][1])
            country_data_list.append(country_list)

        # print(country_data_list)

        bar_width = 0.1
        index = -5
        print(country_data_list[0])
        for i in range(len(asean_country_list)):
            plt.bar(
                [x + index * bar_width for x in range(len(years))],
                country_data_list[i],
                width=bar_width,
                label=asean_country_list[i],
            )
            index += 1

        plt.xticks([i + bar_width for i in range(len(years))], years)
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title("Population from 2004 to 2014")
        plt.tight_layout()
        plt.legend(asean_country_list)
        plt.show()


def execute():
    '''
    Main executable function
    '''
    print("1. Make a Bar Plot of 'population of India' vs. years.")
    print(
        "2. Plot a Bar Chat of the population of these countries only using data for the year 2014"
    )
    print("3. Plot a BAR CHART of Total SAARC population vs. year.")
    print("4. Plot population of ASEAN countries as groups over the years 2004 - 2014.")
    print("Select your choice ")
    user_input = input()
    user_input = int(user_input)

    if user_input == 1:
        india_population()
    elif user_input == 2:
        pop_asean_2014()
    elif user_input == 3:
        total_population_saarc_every_year()
    elif user_input == 4:
        grouped_asean_pop_2004_to_2014()
    else:
        print("Wrong Input. Exiting")


execute()
