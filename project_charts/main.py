from app.time_execution import time_execution_print
from app.charts import generate_bar_chart, generate_pie_chart
from app.utils_csv import (
    read_csv, select_column, group_countries, sort_values
)
from app.input_options import get_number, get_text_from_list

@time_execution_print
def get_data(path):
    data = read_csv(path)
    labels = select_column(data, 'Country/Territory')
    values = select_column(data, 'World Population Percentage', True)
    return labels, values

def run(path):
    list_charts = ['bar', 'pie']
    type_chart = get_text_from_list(
        '''Por favor, ingrese el tipo de gráfico que desea ver (Bar o Pie),
escriba simplemente la palabra tal como aparece en el encabezado.: ''',
            list_charts
    )
    min_value = get_number(
        '''Escriba el porcentaje mínimo que desea observar por país. 
Los países con valores inferiores se agruparán bajo la opción 'Otros'. 
Por favor, escriba solo el número porcentual sin ningún tipo de signo. Ejemplo: 10: '''
    )

    labels, values = get_data(path)
    labels, values = group_countries(labels, values, min_value)
    labels, values = sort_values(labels, values)
    if values:
        if type_chart == 'bar':
            generate_bar_chart(
                labels=labels,
                values=values,
                title=f'World Population Percentage',
                xlabel='Percentage',
                ylabel='Country',
                horizontal=True,
                name='Population_Bar'
            ) 
        elif type_chart == 'pie':
            generate_pie_chart(
                labels=labels,
                values=values,
                title=f'World Population Percentage',
                name='Population_Pie'
            )

if __name__ == '__main__':
    run('./data/world_population.csv')