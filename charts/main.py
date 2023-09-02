from charts import generate_pie_chart

def run():
    generate_pie_chart(
        ['A', 'B', 'C'],
        [100, 500, 300],
        'Grafico de prueba',
        'GraficoPrueba'
    )

if __name__ == '__main__':
    run()
