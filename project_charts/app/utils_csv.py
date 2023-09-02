import csv
import re

def read_csv(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data.append(dict(iterable))
    return data

def select_column(data, column_name, is_numeric=False):
    if is_numeric:
        result = list(map(lambda x: float(x[column_name]), data))
    else:
        result = list(map(lambda x: x[column_name], data))
    return result

def filter_data(data, country):
    return list(
        filter(
            lambda x: x['Country/Territory'] == country,
            data
        )
    )

def read_and_filter(path, country):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            data_country = dict(iterable)
            if country == data_country['Country/Territory']:
                return data_country
    return None

def extract_population(data):
    population = {}
    for key, value in data.items():
        match = re.match('([0-9]+) Population', key)
        if match:
            population[match.group(1)] = value
    return {k:int(v) for k, v in population.items()}
    
def group_countries(countries, values, min_value=10):
    new_countries = []
    new_values = []
    for c, v in zip(countries, values):
        if v >= min_value:
            new_countries.append(c)
            new_values.append(v)
    new_countries.append('Others')
    new_values.append(sum(values) - sum(new_values))
    return new_countries, new_values
    
def sort_values(labels, values, asc=False):
    def method(x):
        return x[1]
    list_data = list(zip(labels, values))
    list_data.sort(key=method, reverse=asc)
    return list(zip(*list_data))
