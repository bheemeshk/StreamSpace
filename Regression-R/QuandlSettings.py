def get_quandl_data(quandl_data_set_name, quandl_settings):
        """
        This method retrieves the quandl data set given the settings specified in the quandl_settings object. For more
        information about these settings see documentation from the QuandlSettings class
        """
        quandl_data_set = get(quandl_data_set_name, rows=quandl_settings.rows, returns="numpy",
                              transformation=quandl_settings.transformation,
                              sort_order=quandl_settings.order, collapse=quandl_settings.frequency)
        print(quandl_data_set)
        quandl_dates = np.arange(1, quandl_settings.rows + 1, 1)
        quandl_prices = []

        # TODO: find a better way to extract some column, X, from numpy matrix of tuples (w, x, y, z)
        for i in range(quandl_data_set.size):
            quandl_prices.append(quandl_data_set[quandl_settings.rows - (i + 1)][quandl_settings.column] / 100)
        return quandl_dates, quandl_prices