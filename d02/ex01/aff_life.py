from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Loads the .csv and displays the data for France"""
    try:
        data = load("life_expectancy_years.csv")

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
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
