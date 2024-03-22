import dask.dataframe as dd
import datashader as ds
import datashader.transfer_functions as tf
import plotly.express as px

#---------------------------------------------------------------------------------#
# Testing parameters

# Features to be displayed
x_feat = "Time(s)"
y_feat = "Arterial pressure (mmHg)"

path = "/Users/isacfiorotti/Library/CloudStorage/OneDrive-TheUniversityofNottingham/Modules/COMP4031 - Personal Project/data/data.csv"
header_names = ['Time(s)', 'Arterial pressure (mmHg)', 'Aortic Doppler (kHz)',
       'Mesenteric Doppler (kHz)', 'Renal Doppler (kHz)']

#---------------------------------------------------------------------------------#

#TODO: Make wrapper function to read data that is able to handle more features 

ddf = dd.read_csv(path, 
                 header=0, 
                 names=header_names)

ddf = ddf.persist() # Persist for future operations? I think that there might be a problem with this ask for help from big data people

#---------------------------------------------------------------------------------#

#TODO: Add functionality to wrapper function to check that the program has been able to read all data types and converts time to interpretable time

ddf['Time(s)'] = dd.to_datetime(ddf['Time(s)'], format='%H:%M:%S.%f').astype('int64')

#---------------------------------------------------------------------------------#

def rasterise(df):
    """Rasterises Dask DataFrame using Datashader.

    Args:
        df (ddf.dataframe.DataFrame): A dask DataFrame containing the data to be plotted.
    Returns:
        PIL.Image.Image: The rendered image of the line plot.
    """

    canvas = ds.Canvas(

        plot_width=1000,
        plot_height=400
    )
    agg = canvas.line(
        df,
        x=x_feat,
        y=y_feat,
    )
    return tf.shade(agg, how='linear')

#---------------------------------------------------------------------------------#

#TODO: Make function that takes rasterise input and plots it

img = rasterise(ddf.compute()) # Always make sure to .compute() or you will not pass a ddf

# Plotly express plot
fig = px.imshow(img)
fig.update_layout(
    title='Line Plot using Datashader and Plotly',
)
fig.show()
print("Image displayed successfully.")

#---------------------------------------------------------------------------------#

