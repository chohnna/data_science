import pandas as pd
import plotly.express as px

# Load the data
file_path = '~/Desktop/data_science/nutritional_data.csv'
data = pd.read_csv(file_path)

# Convert protein and fat percentages to numeric values, ignoring errors for non-numeric data
data['Protein'] = pd.to_numeric(data['Protein'].str.replace('%', ''), errors='coerce')
data['Fat'] = pd.to_numeric(data['Fat'].str.replace('%', ''), errors='coerce')

# Drop rows with any missing values in 'Protein' or 'Fat'
data.dropna(subset=['Protein', 'Fat'], inplace=True)

# Create a scatter plot using Plotly for interactive hover features
fig = px.scatter(data, x='Protein', y='Fat', title='Protein vs Fat Content',
                 hover_data={'Brand': True, 'URL': True})  # Include URLs in hover data

# Update the trace for hover info to include clickable links
fig.update_traces(marker=dict(size=10),
                  hovertemplate='Brand: %{hovertext}<br>Protein: %{x}%<br>Fat: %{y}%<br><a href="%{customdata[1]}">More Info</a>',
                  hovertext=data['Brand'],  # Display brand name on hover
                  customdata=data[['Brand', 'URL']])  # Custom data for use in the hover template

# Save the interactive plot to an HTML file
fig.write_html('protein_vs_fat_scatter_plot.html')

# Show the interactive figure
fig.show()
