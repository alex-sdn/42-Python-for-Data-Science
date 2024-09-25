from load_csv import load
import matplotlib.pyplot as plt


def convert_values(value):
    """Converts abbreviated numbers to integers"""
    if isinstance(value, str):
        if value.endswith('M'):
            return int(float(value[:-1]) * 1e6)
        elif value.endswith('k'):
            return int(float(value[:-1]) * 1e3)
    return value


def show_pop(path):
    """Loads the .csv and displays the data for France and country2"""
    data = load(path)
    data.iloc[:, 1:] = data.iloc[:, 1:].map(convert_values)

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

    plt.xlim([1800, 2050])

    plt.legend()
    plt.show()


if __name__ == '__main__':
    try:
        show_pop("population_total.csv")
    except Exception as e:
        print(str(e))
