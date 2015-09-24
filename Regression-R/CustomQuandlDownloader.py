class QuandlSettings:
    """
    This class contains settings for the quandl integration package, settings include,
    * rows:int - specifies the amount of historical data to extract in [frequency]
    * column:int - specifies the column in the data-set to use for the regression analysis
    * frequency:String - select between ("daily"|weekly"|"monthly"|"quarterly"|"annual")
    * transformation:String - select the numerical transformation ("diff"|"rdiff"|"normalize"|"cumul")
    * order:String - select order of data between ("asc"|"desc")
    """
    rows = 0
    column = 1
    frequency = "weekly"
    transformation = "normalize"
    order = "desc"

    def __init__(self, rows, column, frequency="weekly", transformation="normalize", order="desc"):
        """
        This initialization method constructs a new QuandlSettings object
        """
        self.rows = rows
        self.column = column
        self.frequency = frequency
        self.transformation = transformation
        self.order = order

