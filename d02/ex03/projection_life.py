from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """
    Loads the data and display life expectancy in relation to
    the GDP of 1900 for each country.
    """
    try:
        file1 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        file2 = "life_expectancy_years.csv"
        income_data = load(file1)
        life_exp_data = load(file2)

        income_1900 = income_data.loc[:, ['country', '1900']]
        life_exp_1900 = life_exp_data.loc[:, ['country', '1900']]

        merged_data = pd.merge(income_1900, life_exp_1900, on='country',
                               suffixes=('_income', '_life_exp'))

        plt.figure()
        plt.scatter(merged_data['1900_income'], merged_data['1900_life_exp'])

        plt.xlabel('GDP')
        plt.ylabel('Life Excpectancy')
        plt.title('1900')

        plt.xscale('log')

        plt.show()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
