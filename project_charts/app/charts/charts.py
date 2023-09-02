import matplotlib.pyplot as plt
PATH = './images/'

def generate_bar_chart(
        labels, values, title, xlabel, ylabel,
        name, horizontal=False
    ):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    if horizontal:
        ax.set_xlim([0, max(values) * 1.1])
        rects = ax.barh(labels, values)
    else:
        ax.set_ylim([0, max(values) * 1.1])
        rects = ax.bar(labels, values)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    format_values = ['{:,.1f}%'.format(x) for x in values]
    ax.bar_label(
        rects, padding=1, 
        labels=format_values)
    plt.savefig(PATH + name + '.png')

def generate_line_chart(
        labels, values, title, xlabel, ylabel, name
    ):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(labels, values)
    plt.savefig(PATH + name + '.png')

def generate_pie_chart(labels, values, title, name):
    plt.style.use('seaborn')
    fig, ax = plt.subplots(1,1)
    ax.pie(
        values, labels=labels, 
        autopct='%1.1f%%'
    )
    fig.suptitle(
        title,
        fontsize='large',
        fontstyle='oblique',
        fontweight='bold'
    )
    ax.axis('equal')
    plt.savefig(PATH + name + '.png')


if __name__ == '__main__':
    pass