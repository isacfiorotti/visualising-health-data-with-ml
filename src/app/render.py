import dask.dataframe as dd
import datashader as ds
import datashader.transfer_functions as tf
import plotly.express as px
import datashader as ds
import datashader.transfer_functions as tf

#---------------------------------------------------------------------------------#

#TODO: Add functionality to infer header names from the CSV file
#TODO: Add functionality to wrapper function to check that the program has been able to read all data types and converts time to interpretable time

def read_csv(path, header_names):
    """
    Reads data from a CSV file using Dask.

    Args:
        path (str): The path to the CSV file.
        header_names (list): A list of column names for the CSV file.

    Returns:
        ddf.datframe: A dask DataFrame containing the data.
    """

    ddf = dd.read_csv(path, 
                     header=0, 
                     names=header_names)

    ddf = ddf.persist() # Persist for future operations? I think that there might be a problem with this ask for help from big data people

    #Temporary function to convert time to interpretable time
    ddf['Time(s)'] = dd.to_datetime(ddf['Time(s)'], format='%H:%M:%S.%f').astype('int64')

    return ddf

#---------------------------------------------------------------------------------#

def rasterise(df, width, height, x_feat, y_feat):
    """
    Rasterises Dask DataFrame using Datashader.

    Args:
        df (ddf.dataframe): A dask DataFrame containing the data to be plotted.
        width (int): The width of the rendered image.
        height (int): The height of the rendered image.
        x_feat (str): The name of the column in the DataFrame to be used as the x-axis.
        y_feat (str): The name of the column in the DataFrame to be used as the y-axis.

    Returns:
        PIL.Image.Image: The rendered image of the line plot.
    """
    canvas = ds.Canvas(plot_width=width, plot_height=height)
    agg = canvas.line(df, x=x_feat, y=y_feat)
    return tf.shade(agg, how='linear')

#---------------------------------------------------------------------------------#

#TODO: Add ability to choose different type of graph

def plot_raster(df, width, height, x_feat, y_feat):
    """
    Plots the rasterised image using Plotly Express.

    Args:
        df (ddf.dataframe): A dask DataFrame containing the data to be plotted.
        width (int): The width of the rendered image.
        height (int): The height of the rendered image.
        x_feat (str): The column name for the x-axis.
        y_feat (str): The column name for the y-axis.
    """
    img = rasterise(df.compute(), width, height, x_feat, y_feat) # Always make sure to .compute() or you will not pass a ddf

    # Plotly express plot
    fig = px.imshow(img)
    fig.update_layout(
        title='Line Plot using Datashader and Plotly',
    )

    print("Image displayed successfully.")

#---------------------------------------------------------------------------------#

