def economics_example():
    """
    This method creates a set of regression analyses based on economics GDP's of the BRICS nations, 
    """
    # b: blue, g: green, r: red, c: cyan, m: magenta, y: yellow, k: black, w: white
    statsmodels_args = StatsModelsSettings(1, False)
    quandl_args_prices = QuandlSettings(15, 1, "yearly")

    # South Africa, China, Brazil, India, Russia
    regressions = [RegressionAnalysis("WORLDBANK/ZAF_NY_GDP_MKTP_KN", quandl_args_prices, statsmodels_args, 'b'),
                   RegressionAnalysis("WORLDBANK/CHN_NY_GDP_MKTP_KN", quandl_args_prices, statsmodels_args, 'g'),
                   RegressionAnalysis("WORLDBANK/BRA_NY_GDP_MKTP_KN", quandl_args_prices, statsmodels_args, 'k'),
                   RegressionAnalysis("WORLDBANK/IND_NY_GDP_MKTP_KN", quandl_args_prices, statsmodels_args, 'm'),
                   RegressionAnalysis("WORLDBANK/RUS_NY_GDP_MKTP_KN", quandl_args_prices, statsmodels_args, 'c')]
    plot_regression_line(regressions)



