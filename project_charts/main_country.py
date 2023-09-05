from app.time_execution import time_execution_print
from app.charts import generate_line_chart
from app.input_options import get_text
from app.utils_csv import (
    read_csv, filter_data, extract_population,
    read_and_filter, read_csv_with_pandas, filter_with_pandas,
    get_population_columns
)

@time_execution_print
def option_1(path, country):
    data = read_csv(path)
    data = filter_data(data, country)
    if len(data) > 0:
        data = extract_population(data[0])
    else:
        data = None
    return data

@time_execution_print
def option_2(path, country):
    data = read_and_filter(path, country)
    if data:
        data = extract_population(data)
    return data

@time_execution_print
def option_3(path, country):
    data = read_csv_with_pandas(path)
    data = filter_with_pandas(data, 'Country/Territory', country)
    if not isinstance(data, type(None)):
        data = get_population_columns(data)
    return data

def run(path):
    country = get_text(
        'Select a country: '
    )
    option_1(path, country)
    option_2(path, country)
    data = option_3(path, country)
    if data:
        generate_line_chart(
            labels=list(data.keys())[::-1],
            values=list(data.values())[::-1],
            title=f'{country} Population',
            xlabel='Year',
            ylabel='Population',
            name=f'Population_{country}'
        )
    

if __name__ == '__main__':
    run('./data/world_population.csv')