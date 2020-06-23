# Example sketch for HCI 584 - Chris Harding May 31, 2020

This is an example of a student project for HCI 584. It will be used to illustrate its use in creating a project planning document (spec)

### Title: Show local earthquake activity


### Describe the project in a few paragraphs
- The app will show the most severe historical quake activity at a user given location and within a user given radius. 
- I envision a map of the area with quake locations shown as point markers and date and magnitude as number labels. 
- By default the most severe quakes (up to 100) from 1900 - present would be shown. Each marker could visualize additional quake properties. 
- The user should be able to filter/refine this by setting ranges for date, magnitude and depth and overall number. 
- Additionally, users can request a statistics table and plot (graph, non-map!) of these quakes. This would be a web app (ideally mobile) but could also provide a API which would receive these user set parameters (query parameters or JSON) and return a map/table/plot.


### Who would be the users? Are there secondary stakeholders?
- My primary use would be educational i.e. students learning about quake activity in their or other relevant areas, either in the class room or on field trips. Would also apply to the general public. 
- Secondary stakeholders could be those wanting to integrate this into their own apps

### What problem would it (help to) solve?
- This would help to make users aware of current and past quake activity in their (or any) area. For example students in Chicago would learn about the 5.5 1968 quake.

### What is the workflow (user path)? What would the user do? What is the primary interaction? Is there an interaction loop?
- Select location via click on map, lat/lon input, or location text search. 
- Select and later refine parameters via text field input which refreshes both views. 
- Switch between map view and statistics view (table + plot). 

### What data would be used (input), how would you get it and how is it processed/analyzed?
- Data will come online from the USGS Earth quake Catalog API https://earthquake.usgs.gov/fdsnws/event/1/ witch which I can request a list of quakes sorted by magnitude and around a certain location. 
- Download data for this app (up to 100 quakes) is tiny and extremely fast. 
- Minimal processing should be needed as the filtering is done mostly server side. 
- Some work is needed to arrive at good visualization parameters to map the current set of quakes effectively for any mix of data without map clutter.
- There's next to no analysis other than summary stats.

### What are the results and how are they presented? 
- Online (folium or google map view) More quake data (fatalities) shown as balloon text info when clicking a on quake marker. 
- Table and plot as static images (possible as "live" visualization where parameters are changed on the fly).  
- Possibly current settings as presets or send as email so somebody else can jump to them.