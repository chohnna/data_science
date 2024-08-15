import matplotlib.pyplot as plt
import pandas as pd
import webbrowser

# Load nutritional data from CSV
file_path = '~/Desktop/data_science/nutritional_data.csv'
data = pd.read_csv(file_path)

# Load URLs from text file
url_file_path = '~/Desktop/data_science/dog_food_brand_urls.txt'
url_data = pd.read_csv(url_file_path, header=None, names=['Brand', 'URL'], delimiter=' - ')

# Merge the nutritional data with the URLs based on the 'Brand'
data = pd.merge(data, url_data, on='Brand', how='left')

# Convert string percentages to floats if necessary
data['Protein'] = pd.to_numeric(data['Protein'].str.replace('%', ''), errors='coerce')
data['Fat'] = pd.to_numeric(data['Fat'].str.replace('%', ''), errors='coerce')

# Define a class to hold data for plotting and URL
class CustomDataPoint:
    def __init__(self, x, y, name, url):
        self.x = x
        self.y = y
        self.name = name
        self.url = url

# Create a list of custom data points
data_points = []
for index, row in data.iterrows():
    data_point = CustomDataPoint(row['Protein'], row['Fat'], row['Brand'], row['URL'])
    data_points.append(data_point)

# Function to handle click events
def on_pick(event):
    data_point = event.artist.data_point
    print(f"Opening URL for {data_point.name}: {data_point.url}")
    webbrowser.open(data_point.url)

# Set up the plot
fig, ax = plt.subplots()
for data_point in data_points:
    artist = ax.plot(data_point.x, data_point.y, 'ro', picker=True, markersize=3)[0]
    artist.data_point = data_point  # Attach the custom data point object to the artist

fig.canvas.mpl_connect('pick_event', on_pick)

# Plot settings
plt.title('Protein vs. Fat Content in Dry Dog Foods')
plt.xlabel('Protein (%)')
plt.ylabel('Fat (%)')
plt.grid(True)
plt.savefig('drydogfood.jpeg')
plt.show()
