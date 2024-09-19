from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def projection(income_path, life_path):
    income_data = load(income_path)
    life_exp_data = load(life_path)

    income_1900 = income_data.loc[:, ['country', '1900']]
    life_exp_1900 = life_exp_data.loc[:, ['country', '1900']]

    merged_data = pd.merge(income_1900, life_exp_1900, on='country', suffixes=('_income', '_life_exp'))

    plt.figure()
    plt.scatter(merged_data['1900_income'], merged_data['1900_life_exp'])

    plt.xlabel('GDP')
    plt.ylabel('Life Excpectancy')
    plt.title('1900')

    plt.xscale('log')

    plt.show()


if __name__ == '__main__':
    try:
        projection("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")
    except Exception as e:
        print(str(e))