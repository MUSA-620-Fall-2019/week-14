# Week 14<br>Dashboarding with Panel and the Holoviz Ecosystem

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MUSA-620-Fall-2019/week-14/master?filepath=lecture-14.ipynb)

## Final Project

The final deliverable **must include all three of the below items**:

1. a web-based data visualization with a URL (public or private)
1. a document describing the project, the results, and the technical methods used in each step (collection, analysis and visualization)
1. all code/spreadsheets/datasets used

The materials for steps #2 an #3 above should be submitted to your own specific GitHub repository, which can be created using the link below:

https://classroom.github.com/g/cQQU9eCr

### Important

- The code for your web-based visualization (#1) can be either in the same repository or in a separate **public** repository. If it is in its own repository, be sure to link to it from the main, submission repository.
- Be sure to include the names of everyone who worked on the final project somewhere in the README, etc!

## Office Hours

Office hours next week during the regular class slot: **Thursday Dec 12 from 5 to 8pm**

## Dashboard Examples

We'll walk through two examples of [Panel](https://panel.pyviz.org) dashboards that can serve as a reference for the final project.

1. [Visualizing recent shootings in Philadelphia using Altair, Folium, and Holoviews](https://github.com/MUSA-620-Fall-2019/philadelphia-shootings-app)
1. [Visualizing NYC taxi trips with Datashader and Altair](https://github.com/MUSA-620-Fall-2019/datashader-nyc-taxi-app)

## Summary of Web-based Options

- [Web visualization options](./WebVisualizationOptions.md)
- [Deployment options](./DeploymentOptions.md)

## References

- Panel
  - [Documentation](https://panel.pyviz.org)
  - [User Guide](https://panel.pyviz.org/user_guide/index.html)
  - [Reference Gallery](https://panel.pyviz.org/reference/index.html)
    - Includes examples of different types of Panels, e.g., HTML, Markdown, Vega, etc
  - [Example dashboards from the PyViz team](https://github.com/pyviz-demos)
- [Datashader dashboard tutorial](https://examples.pyviz.org/datashader_dashboard/dashboard.html)
  - Including a detailed walk-through of a Datashader-based dashboard
- [Holoviews Reference Gallery](http://holoviews.org/reference/index.html)
  - [Streams](http://holoviews.org/reference/index.html#streams)
  - [DynamicMap](http://holoviews.org/reference/containers/bokeh/DynamicMap.html#bokeh-gallery-dynamicmap)
- [Introduction to Python classes](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
- Heroku
  - First, signup for a Heroku free [account](https://signup.heroku.com)
  - Download and [install the command line interface (CLI)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
  - See the "Heroku Example" for Dash: https://dash.plot.ly/deployment
  - See the example [instructions](https://github.com/MUSA-620-Fall-2019/philadelphia-shootings-app#deploying-this-app-on-heroku) for deploying the Philadelphia Shootings App on Heroku
