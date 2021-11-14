#from QuantConnect import Resolution
#from QuantConnect import DataNormalization
#from QuantConnect.Algorithm import QCAlgorithm
from AlgorithmImports import *

class Firsttestproject(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2018, 12, 1)  # Set Start Date
        self.SetEndDate(2020, 4, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        self.ibm = self.AddEquity("IBM", Resolution.Daily)
        #self.ibm.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.lastOrderEvent = None

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            self.StopMarketOrder("IBM", -50, 0.90 * self.Securities["IBM"].Close)
            self.MarketOrder("IBM", 100)

         #printing the Avg price of IWM to the console
           #self.Debug("THE AVERAGE PRICE OF IBM IS: " +str(self.Portfolio["IBM"].AveragePrice))

        #sell stocks
            #self.StopMarketOrder("IBM", -50, 0.90 * self.Securities["IBM"].Close)

    def OnOrderEvent(self, orderEvent):

        if orderEvent.Status == OrderStatus.Filled:
            self.lastOrderEvent = orderEvent
            self.Debug( "THIS IS THE ORDER ID: " +str(self.lastOrderEvent.OrderId) )            