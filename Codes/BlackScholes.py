import numpy as np
from scipy.stats import norm

# Implementing Black-Scholes Model
def BlackScholes(S, K, r, sigma, t, option):
	# S: Current stock price
	# K: Strike price
	# r: Risk-free rate
	# sigma: Volatility
	# t: Time to maturity
	# option: 'call' or 'put'

	d1 = (np.log(S/K) + (r + (sigma**2)/2) * t) / (sigma * np.sqrt(t))
	d2 = d1 - sigma * np.sqrt(t)

	# Call option
	if option == 'call':
		return S * norm.cdf(d1) - K * np.exp(-r*t) * norm.cdf(d2)

	# Put option
	if option == 'put':
		return K * np.exp(-r*t) * norm.cdf(-d2) - S * norm.cdf(-d1)


# Main function
def main():
	S = 100
	K = 100
	r = 0.05
	sigma = 0.2
	t = 0.5

	C = BlackScholes(S, K, r, sigma, t, 'call')

	print(C)


# Call main function
if __name__ == "__main__":
	main()