import random

# Global Variables
good = ["A", "B", "C"]    # Good states
bad = ["D", "E", "F"]     # Bad states
sampleSpace = [good, bad] # All states

n = 100     # Number of shares
p0 = 5      # Initial price per share
x0 = n * p0 # Total initial price of shares

factor = random.random()  # Random number in [0, 1)


# X : random variable representing the value of your holdings a year from now
def X(state):
	if state in good:  # Price of stock increases
		return (1 / factor) * x0
	elif state in bad: # Price of stock decreases
		return factor * x0


# Probability Distribution Function of X
def pdfX():
	p = 0.7 # Probability of good state

	k = random.random()
	if k < p:
		return random.choice(sampleSpace[0])
	else:
		return random.choice(sampleSpace[1])


# Del : random variable representing change in the value of your asset holdings
def Del(state):
	return X(state) - x0


# R : random variable representing the return on initial investment
def R(state):
	return Del(state) / x0


# Main function
def main():
	state = pdfX()
	P = X(state) / n
	Rx = (P - p0) / p0
	print("n      = {}".format(n))
	print()
	print("x0     = {}".format(x0))
	print("p0     = {}".format(p0))
	print()
	print("X(w)   = {}".format(X(state)))
	print("P      = {}".format(P))
	print()
	print("Del(w) = {}".format(Del(state)))
	print("R(w)   = {}".format(R(state)))
	print()
	print("R = (P - p0) / p0 = {}".format(Rx))


# Call main function
if __name__ == '__main__':
	main()