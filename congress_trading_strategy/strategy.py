import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import SignalStrategy, TrailingStrategy
from backtesting.test import GOOG  # Example data


class OrderStrategy(SignalStrategy):
    def init(self):
        super().init()
        self.orders = self.data.df_orders  # Load orders into the strategy

    def next(self):
        # Loop through the orders and place them based on the conditions
        for _, order in self.orders.iterrows():
            if order.datetime == self.data.index[self.i]:
                if order.order_type == 'buy':
                    self.buy(size=order.quantity, price=order.price)
                elif order.order_type == 'sell':
                    self.sell(size=order.quantity, price=order.price)


def load_orders(file_path):
    return 


def calculate_results():
    # Load orders from CSV
    orders = pd.read_csv('congress_trading_signals_with_options.csv', parse_dates=['Quiver_Upload_Time', 'Filed', 'Traded'])

    # TODO group by ticker

    # TODO does it depend if it's option or stock or we can still calculate

    for index, order in orders.iterrows():
        def get_ticker():
            # TODO
            return GOOG

        ticker = get_ticker()

        ticker.df_orders = order


    # Assuming we have a CSV file with historical data for the stock
    # For example purposes, we'll use GOOG from backtesting.test
    # Replace this with your actual stock data
    data = GOOG

    # Add orders data to the DataFrame
    data.df_orders = orders

    # Run backtest
    bt = Backtest(data, OrderStrategy, cash=1000000, commission=.002)
    stats = bt.run()

    # Print stats
    print(stats)

    # Plot the results
    bt.plot()


if __name__ == "__main__":
    calculate_results()
