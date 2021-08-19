
# Ad Tech DataSet Dashboard

### Dashboard preview can be found using this link *[AdTech Dashboard](https://github.com/milanzmitrovic/Ad-Tech-Project---Dash-Plotly/blob/master/Dash.pdf)*.

## Metrics:

- Total Revenue
- Total Impressions
- Viewable Impressions
- Measurable Impressions

## Dimensions:

- Site ID
- Ad Type ID
- Geo ID
- Order ID
- Line Item Type ID
- OS ID
- Integration Type ID
- Monetization Channel


## Charts present in web app

- Bar Chart
- Line Chart
- Scatter Plot with marginal plot
- Icicle Chart

## WebApp functionality

#### Bar Chart

- Bar Chart is completely dynamic. There is possibility to choose dimension, metric and
even aggregate function to be applied to groups of data.
- Dimensions, Measures and Agg Function drop-downs are dynamically changing this chart.

#### Line Chart
- There is possibility to see evolution of different metrics over time. Also, aggregate
function applied to groups/partitions of data can be changed.
- Measure and Agg Function filter apply to this chart. 



#### Scatter Plot with Dist Chart

- There is possibility to see relationship between two variables using 
scatter diagram.
- Also, marginal distribution of variables are shown on chart.
- There are two drop-down filters, so we can choose what two variables
we want to show on chart.
- Due to data size, resampling is performed before relationship plot. Sample size is 500.


#### Icicle Chart

- Icicle Chart is new way to show hierarchical relationship between categorical 
variables. It was introduced in Plotly.js library in July 2021.
- There is dropdown menu above chart where we can choose what variables we want 
to see in hierarchical diagram. 
- Sum is always applied as aggregate function.




## DataSet info

- Raw data can be found *[here](https://github.com/milanzmitrovic/Ad-Tech-Project---Dash-Plotly/tree/master/data)*.

- Complete description of dataset can be found on Kaggle website by clicking *[here](https://www.kaggle.com/vaishnavkapil/adtech)*.
