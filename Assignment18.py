import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Simulation Function
def simulate_spread(init_infected, contact_rate, days):
    infected = [init_infected]
    for day in range(1, days):
        new_infections = infected[-1] * contact_rate
        infected.append(infected[-1] + new_infections)
    return infected

# Constants
days = 100
initial_infected = 100
contact_rate = 0.1  # 10% growth

infected_data = simulate_spread(initial_infected, contact_rate, days)

# Create Plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
l, = plt.plot(range(days), infected_data, lw=2)
ax.set_xlabel('Days')
ax.set_ylabel('Infected People')
ax.set_title('COVID-19 Spread Simulation (USA)')
ax.grid(True)

# Slider for Contact Rate
ax_contact = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_contact = Slider(ax_contact, 'Contact Rate', 0.01, 0.5, valinit=contact_rate)

# Update function
def update(val):
    new_contact_rate = slider_contact.val
    new_data = simulate_spread(initial_infected, new_contact_rate, days)
    l.set_ydata(new_data)
    fig.canvas.draw_idle()

slider_contact.on_changed(update)
plt.show()
