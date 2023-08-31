import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)
control_group = np.random.normal(loc=5, scale=1, size=100)
treatment_group = np.random.normal(loc=7, scale=1, size=100)

t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)

plt.boxplot([control_group, treatment_group], labels=['Control Group', 'Treatment Group'])
plt.ylabel('Values')
plt.title('Clinical Trial Data')
plt.figtext(0.15, 0.85, f'p-value: {p_value:.4f}', color='blue', fontsize=12)
plt.show()

if p_value < 0.05:
    print("The new treatment has a statistically significant effect.")
else:
    print("There is no statistically significant effect of the new treatment.")
