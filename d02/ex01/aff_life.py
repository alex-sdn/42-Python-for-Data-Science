from load_csv import load
import matplotlib.pyplot as plt


def show_life(path):
    data = load(path)

    france_data = data.loc[data['country'] == 'France']
    years = france_data.columns[1:].astype(int)
    life_exp = france_data.iloc[0, 1:]

    plt.figure()
    plt.plot(years, life_exp)

    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('France life expectancy projections')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    try:
        show_life("life_expectancy_years.csv")
    except Exception as e:
        print(str(e))
