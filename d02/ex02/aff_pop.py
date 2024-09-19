from load_csv import load
import matplotlib.pyplot as plt


def convert_values(value):
    if isinstance(value, str):
        if value.endswith('M'):
            return int(float(value[:-1]) * 1e6)
        elif value.endswith('k'):
            return int(float(value[:-1]) * 1e3)
    return value


def show_pop(path):
    data = load(path)
    data.iloc[:, 1:] = data.iloc[:, 1:].map(convert_values) #convert M and k suffixes

    years = data.columns[1:].astype(int)
    
    france_data = data.loc[data['country'] == 'France']
    pop_france = france_data.iloc[0, 1:]

    country2 = 'Belgium'
    country2_data = data.loc[data['country'] == country2]
    pop_country2 = country2_data.iloc[0, 1:]

    plt.figure()
    plt.plot(years, pop_france, label="France")
    plt.plot(years, pop_country2, label=country2)

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population projections')

    plt.xlim([1800, 2050]) # set X axis limits

    plt.legend()
    plt.show()


if __name__ == '__main__':
    try:
        show_pop("population_total.csv")
    except Exception as e:
        print(str(e))
