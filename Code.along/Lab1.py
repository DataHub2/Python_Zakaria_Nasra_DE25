import matplotlib.pyplot as plt
import numpy as np

print("Testar matplotlib...")

# Enkel plot
plt.plot([1, 2, 3, 4, 5])
plt.ylabel('Some numbers')
plt.title('Min första plot')
plt.savefig('min_plot.png')  # Spara som bild istället för show()
print("Plot sparad som 'min_plot.png'")

# Alternativ: Visa plot
# plt.show()