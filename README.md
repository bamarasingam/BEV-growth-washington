# BEVs (Battery Elecetric Vehicles) Growth Within Washington

## Executive Summary
### Problem Statement
Our world has come at a crossroads when it comes to transportation, specifically with automobiles. For over a century, our main form of fuel for these vehicles has been gasoline/diesel. Although effective, these forms of fuel have many environmental drawbacks which have been well documented across various sources. Due to pressure from various entities (goverment, NGO's, etc.), stricter emission regulations and increased consumer focus on air quality, there has been a push towards sustainable transportation. 

Electric cars are seen as a promissing alternative to traditional automobiles due to their low environmental impact, and are projected to grow significantly within the coming years. The state of Washington is seen as one of the states within America at the forefront of this movement, with various policies and plans that are currently in motion to help bring the state to a greener future.

Using machine learning techniques, this repo aims to project the growth of said EV's within the state of Washington. The main analysis used will be multivariate time series analysis, using the VAR (Vector Auto Regression) model. Do note that only fully electric vehicles (BEVs) are considred within these projections; hybrids have been ommitted from total counts (which they include in the electric vehicle count within these datasets). As for the projections, the last 6 years have been very "up only" in terms of the economy, and the EV market, which is what the model is trained on. The only real "down times" the data has been trained on is the few months during COVID. The data collected starts from 2017-01-01 up until 2023-08-31. The projections are month on month, and will be limited to the next 3 years. 


### Sources
Additional sources for various tips/tricks used in notebooks are refrenced within the cell which they were used.
#### Dataset Links
All dataset links can be found within notebooks in the cell where they are refrenced/pulled
- https://catalog.data.gov/dataset/electric-vehicle-population-size-history
- https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/
- https://fred.stlouisfed.org/series/PPIACO
- https://fred.stlouisfed.org/series/TERMCBAUTO48NS
- https://fred.stlouisfed.org/series/RIFLPBCIANM60NM
- https://www.multpl.com/s-p-500-historical-prices/table/by-month
- https://catalog.data.gov/dataset/electric-vehicle-population-size-history-by-county
- https://afdc.energy.gov/stations/#/analyze
- https://catalog.data.gov/dataset/electric-vehicle-population-data
- https://geo.wa.gov/datasets/wadnr::wa-county-boundaries/geoservice

#### Libraries Used
- Pandas
- Numpy
- Matplotlib
- Statsmodels
- Sklearn
- Streamlit
- Geopandas
- Folium
- Streamlit_folium

### Conclusion
