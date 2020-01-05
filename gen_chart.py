import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

plt.style.use("fivethirtyeight")

# Default function for animation
def animate(i):
    # Read data from data.csv
    # And store data in variables
    data = pd.read_csv('data.csv')
    x = data["x_value"]
    y1 = data["y_value1"]
    y2 = data["y_value2"]
    y3 = data["y_value3"]

    # Clear chart
    plt.cla()

    # Plot different company prices on chart
    plt.plot(x, y1, label="Apple Stock")
    plt.plot(x, y2, label="Amazon Stock")
    plt.plot(x, y3, label="Lifevantage Stock")

    # Position Legend
    plt.legend(loc="upper left")
    plt.tight_layout()

# Call animate() and set time interval to 1s
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

# Display chart
plt.show()
