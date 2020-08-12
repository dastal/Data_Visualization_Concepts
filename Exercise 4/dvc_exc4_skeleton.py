import numpy as np
import pandas as pd
import os
from bokeh.core.properties import field
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import (ColumnDataSource, HoverTool, SingleIntervalTicker,
                          Slider, Button, Label, CategoricalColorMapper)
from bokeh.palettes import Spectral8
from bokeh.plotting import figure

__file__ = 'countries.csv'
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
countries_df = pd.read_csv(os.path.join(my_absolute_dirpath,__file__))

__file__ = 'data.csv' # replace with 'data_short.csv' if facing memory error
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
indicators_df = pd.read_csv(os.path.join(my_absolute_dirpath,__file__)) 


# Hint: Go to the reference for more details: https://github.com/bokeh/bokeh/tree/master/examples/app/gapminder

# =====================================
# ====== Your code starts here ========
# =====================================

# add one more column about populatin size into indicators_df

# extract dataframe for each indicator: life expactancy, population size and income

# set up the regions_df

# construct a compact dataframe and the data source

# plotting

# add update functions

# add layout