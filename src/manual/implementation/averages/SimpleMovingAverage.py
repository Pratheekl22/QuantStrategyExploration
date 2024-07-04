import yfinance as yf
import matplotlib.pyplot as plt

class SMACalculator:
    def __init__(self, ticker: str, start_date: str, end_date: str, window: int = 10):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.window = window

    def visualizeSMA(self):
        # Calculate the 10-day Simple Moving Average
        data = self.simpleMovingAverage()

        # Plot the closing prices and the 10-day QuantStrategies
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Closing Prices')
        plt.plot(data[f'SMA_{self.window}'], label=f'{self.window}-Day SMA', color='orange')
        plt.title(f'{self.ticker} Closing Prices and SMA')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def simpleMovingAverage(self):
        # Download historical stock data
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)

        cur_sum = 0
        # Convert closing prices to list
        closing_prices = data['Close'].tolist()
        moving_averages = []

        for i, price in enumerate(closing_prices):
            cur_sum += price
            if i + 1 >= self.window:
                moving_averages.append(cur_sum / self.window)
                cur_sum -= closing_prices[i - self.window + 1]
            else:
                moving_averages.append(None)

        data[f'SMA_{self.window}'] = moving_averages
        return data

sma_calculator = SMACalculator('AMZN', '2022-01-01', '2023-01-01')
sma_calculator.visualizeSMA()