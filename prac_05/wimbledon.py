import csv, operator

FILENAME = "wimbledon.csv"
NAME_INDEX = 2
COUNTRY_INDEX = 1


def main():
    name_list, country_list = read_file()
    name_to_time = calculate_times(name_list)
    print_statement(name_to_time, country_list)


def read_file():
    country_list = []
    name_list = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            name_list.append(record[NAME_INDEX])
            if record[COUNTRY_INDEX] not in country_list:
                country_list.append(record[COUNTRY_INDEX])
    return name_list, country_list


def calculate_times(name_list):
    name_to_time = {}
    for name in name_list:
        if name in name_to_time:
            name_to_time[name] += 1
        else:
            name_to_time[name] = 1
    return name_to_time


def print_statement(name_to_time, country_list):
    print("Wimbledon Champions: ")
    for name, time in sorted(name_to_time.items(), key=operator.itemgetter(0), reverse=False):
        print(f"{name}: {time}")
    print(f"These {len(country_list)} countries have won Winbledon:")
    for country in country_list:
        print(country, end=", ")


main()
