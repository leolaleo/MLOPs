import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('iot_telemetry_data.csv')
# Select the variables for correlation analysis
variables = ['ts', 'device', 'humidity','light','lpg','motion','smoke','temp']
# Calculate the correlation matrix
correlation_matrix = data[variables].corr(method='spearman')
# Create a heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)

# Add plot title and show the heatmap
plt.title('Spearman Correlation Heatmap')
plt.show()