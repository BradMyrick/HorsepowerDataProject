from bokeh.plotting import figure, output_file, show, ColumnDataSource
import pandas

#Read in CSV
df = pandas.read_csv('cars.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

# output html file
output_file('index.html')

# Car List
car_list = source.data['Car'].tolist()

# add plot
p= figure(
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    title = 'Cars With Top Horsepower',
    x_axis_label = 'Horsepower',
    tools="pan,box_select,zoom_in, zoom_out,save,reset"
    )

# Render glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height =0.4,
    color='orange',
    fill_alpha=0.5,
    source=source
    )
# Show results
show(p)
