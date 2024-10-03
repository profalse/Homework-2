# Все данные взяты из официальных источников

# №1. График

# import matplotlib.ticker as ticker
# import matplotlib.pyplot as plt
# x = [1960, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# y = [90, 76, 71, 74, 85, 98, 104, 97, 91, 100, 113, 119, 132, 157, 160, 178, 165, 185, 156, 184, 195, 197, 203, 225, 251, 294, 282, 252, 284, 311, 318, 333, 366, 377, 473, 610, 709, 782, 829, 873, 959, 1053, 1149, 1289, 1509, 1753, 2099, 2694, 3468, 3832, 4550, 5614, 6301, 7020, 7636, 8016, 8094, 8817, 9905, 10144, 10409, 12556, 12970, 12500]

# plt.plot(x, y)
# ax = plt.gca()
# ax.set_xlim(1960, 2022)
# ax.set_ylim(0, 13000)

# ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2020])
# ax.set_yticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000])

# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(1000))

# plt.plot(x, y, color='blue', marker = 'o', markersize = 5)
# plt.xlabel('')
# plt.ylabel('ВВП Китая на душу населения в $')
# plt.title('ВВП Китая на душу населения с 1960 - 2022')
# plt.grid(True, which='major', axis='y', linestyle='solid')

# plt.show()


# №3. Гистограмма

# import matplotlib.pyplot as plt

# x = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
# y = [-5.58, 10.3, 18.18, 16.95, 10.65, -5.77, -4.1, 16.94, 19.3, 7.06, 3.81, 7.76, 2.31, 8.72, -1.57, 7.57, 11.33, 7.59, 7.83, 5.11, 9.02, 10.77, 15.19, 13.43, 8.95, 11.66, 11.22, 4.21, 3.92, 9.26, 14.22, 13.88, 13.04, 10.95, 9.92, 9.24, 7.85, 7.66, 8.49, 8.34, 9.13, 10.04, 10.11, 11.39, 12.72, 14.23, 9.65, 9.4, 10.64, 9.55, 7.86, 7.77, 7.43, 7.04, 6.85, 6.95, 6.75, 5.95, 2.24, 8.11, 4.2, 4.9]

# colors = ['red', 'green', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
# plt.bar(x, y, label='Темпы роста ВВП Китая 1962-2023 гг.', color = colors)
# plt.xlabel('')
# plt.ylabel('Рост ВВП Китая в (%)')
# plt.title('Темпы роста ВВП Китая 1962-2023 гг.')
# plt.legend(loc='upper right')

# plt.show()


# №2. Круговая диаграмма

# import numpy as np
# import matplotlib.pyplot as plt
# amount = [32.6, 9.2, 7.6, 6.9, 7.0, 1.8, 4.1, 3.1, 8.0, 3.9, 15.9]
# labels = ["Промышленное производство", "Оптовая и розничная торговля", "Сельское хозяйство, лесное хозяйство, животноводство и рыболовство", "Недвижимость", "Строительство", "Проживание и рестораны", "Транспортировка, хранение, отправка почтой", "Аренда, лизинг, бизнес-услуги", "Финансы", "Передача информации, программное обеспечение и ИТ-услуги", "Остальное"]
# colors = plt.cm.viridis(np.linspace(0, 1, len(amount)))

# plt.pie(amount, labels=labels, colors=colors, autopct='%1.f%%')
# plt.title("Экономика Китая в 2021 году: ВВП по секторам")
# plt.show()