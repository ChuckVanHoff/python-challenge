''' This script uses profits and losses data to create, display and save a few
graphical representations of that data. '''

import matplotlib.pyplot as plt
import main

# Data for plotting
date = main.month
x = [i for i in range(len(date))]
monthly_pnl = [float(x) for x in main.monthly_pnl]
 # Create a list of cummulative sums from the the pnl list
cumsum_by_month = []
total = 0
for i in monthly_pnl:
    total += i
    cumsum_by_month.append(total)

# Create graphs of the data
 # Monthly pnl
fig, ax = plt.subplots()
ax.plot(x, monthly_pnl, 'k.')
ax.set(xlabel='nth Month After Start',
       ylabel='Dollars',
       title='Monthly Profits and Losses'
      )
ax.axhline(0, c='black')
ax.vlines(x, 0, monthly_pnl,
          color=['black' if profit >= 0 else 'red' for profit in monthly_pnl]
         )
 # Cummulative sum
fig2, ax2 = plt.subplots()
ax2.plot(x, cumsum_by_month)
ax2.set(xlabel='nth Month After Start',
       ylabel='Dollars',
       title='Cummulative Sum')
ax2.grid()

fig.savefig("./Resources/monthly_pnl.png")
fig2.savefig("./Resources/cummulative_sum.png")
plt.show()
