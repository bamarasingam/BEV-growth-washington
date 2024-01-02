# BEVs (Battery Elecetric Vehicles) Growth Within Washington

## Executive Summary
### Problem Statement
Our world has come to a crossroads when it comes to transportation, specifically with automobiles. For over a century our main form of fuel for these vehicles has been gasoline/diesel. Although effective, these forms of fuel have many environmental drawbacks which have been well documented across various sources. Due too pressure from various entities (goverment, NGO's, etc.), stricter emission regulations and increased consumer focus on air quality, there has been a push towards sustainable transportation. 

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
- NumPy
- Matplotlib
- Statsmodels
- Sklearn
- Streamlit
- Geopandas
- Folium
- Streamlit_folium

### Conclusion
Based on the models, we can conclue that we can continue to see a positive growth of BEV's within the coming years. Our best performing model based on minimizing MSE was our ARIMA model, with parameters 9, 2, 0 for p, d, and q respectively. The MSE for this model was 357196.01795728324. Our multivariate modles which utilized VAR did have some trouble in making accurate predictions on the test set; although included in the notebook, this model will be needed to tuned more. The model however did project that growth of BEV's within the state continue too be positive, and this fact between both models is why we concluded that there will continue to be positive growth for BEVs within the state.

One thing to note is the model only does go back to 2017; adverse economic times and times of negative growth for BEV's are not found within this dataset. Perhaps for future iterations, looking at how cars in general fared during economic downtimes would have been beneficial in considering when making out this model. 

All in all, gas emissions and the pollutants which traditional vehicles produce are a net negative to our environment and air quality. Society has begun to shift towards more renewable and sustainable means of energy in all facets of life. Washington itself has started to implement various laws which benefit citizens for taking advantage of this shift towards a greener and more renewable future. The growth of BEV's within the state has only just begun, and will continue to grow as the years go on. 
