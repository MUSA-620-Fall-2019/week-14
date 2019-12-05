# Web-Based Visualization Options for the Final Project

## GitHub Pages

- Template repository: [MUSA-620-Fall-2019/github-pages-starter](https://github.com/MUSA-620-Fall-2019/github-pages-starter/)
- Supported tools: Matplotlib, Folium, Altair, hvplot/Holoviews, HTML files via IFrames
- Examples:
  - [Matplotlib charts](https://musa-620-fall-2019.github.io/github-pages-starter/example-post/)
  - [Folium maps](https://musa-620-fall-2019.github.io/github-pages-starter/folium-charts/)
  - [Altair & Hvplot/Holoviews](https://musa-620-fall-2019.github.io/github-pages-starter/measles-charts/)
- Pros:
  - Automatic deployment/hosting via GitHub
  - Easy text formatting/input via Markdown
  - Supports a variety of visualizations
- Cons:
  - Static rendering with no server support
  - Embedded visualizations cannot interact with each other

## Dash

- Examples:
  - [Dash + Altair](https://github.com/MUSA-620-Fall-2019/week-13/tree/master/dash-altair)
  - [Dash + Folium](https://github.com/MUSA-620-Fall-2019/week-13/tree/master/dash-folium)
- Only deployment option: Heroku
  - See: [Deployment Options](./DeploymentOptions.md) for instructions
- Pros:
  - Server support
  - Access to easy and beautiful widgets from Python
- Cons:
  - Visualizations rendered via IFrames and cannot interact with each other
  - Still requires HTML/CSS knowledge
  - Has to be deployed on Heroku (learning curve)

## Panel

- Examples:
  - [Visualizing recent shootings in Philadelphia using Altair, Folium, and Holoviews](https://github.com/MUSA-620-Fall-2019/philadelphia-shootings-app)
  - [Visualizing NYC taxi trips with Datashader and Altair](https://github.com/MUSA-620-Fall-2019/datashader-nyc-taxi-app)
  - Two deployment options: Binder or Heroku
    - See: [Deployment Options](./DeploymentOptions.md) for instructions
- Pros:
  - Support for all main visualization libraries
  - Only option that allows for using same code in Jupyter notebook and deployment
  - Allows for interaction between dashboard components
  - Multiple deployment options, including Binder (free + easy to set up)
- Cons:
  - Still relatively new and working through some issues
  - Deployment on Binder is not perfect
    - Constrained by Binder resources
  - Deployment to other options still challenging
