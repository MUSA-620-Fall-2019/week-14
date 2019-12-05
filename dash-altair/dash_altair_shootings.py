import dash
import dash_core_components as dcc
import dash_html_components as html
import altair as alt
import io
import requests
import geopandas as gpd
import altair as alt

# initialize the app
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# set a title
app.title = "Dash: Philadelphia Shootings"

# load the neighborhoods
hoods = gpd.read_file(
    "https://raw.githubusercontent.com/MUSA-620-Fall-2019/week-13/master/data/zillow_neighborhoods.geojson"
)


def get_data(days):
    """
    Query the CARTO database to get shootings from the recent past.
    
    Parameters
    ----------
    days : int
        the number of days to get data for
    
    Returns
    -------
    gdf : GeoDataFrame
        the data frame holding the queried data
    """
    query = "SELECT * FROM shootings WHERE date_ >= current_date - %d" % (days)
    r = requests.get(
        "https://phl.carto.com/api/v2/sql", params={"q": query, "format": "geojson"}
    )
    gdf = gpd.GeoDataFrame.from_features(r.json(), crs={"init": "epsg:4326"})
    gdf = gdf.dropna()

    gdf["fatal"] = gdf["fatal"].map({0: "No", 1: "Yes"})

    return gdf


def make_altair_chart(data, days):
    """
    Make the Altair chart
    """
    # select the data we need
    columns = ["ZillowName", "fatal", "race", "age"]
    data = data[columns]

    # brush selection on the ZIP code plot
    brush = alt.selection(type="interval", encodings=["y"])

    # the base chart
    base = alt.Chart(data)

    # shootings by ZIP code
    chart1 = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            y=alt.Y(
                "ZillowName:N",
                title="Neighborhood",
                sort=alt.EncodingSortField(
                    op="count",  # The operation to run on the field prior to sorting
                    order="descending",  # The order to sort in
                ),
            ),
            x=alt.X("count()", title="Number of Shootings"),
            color=alt.condition(
                brush, "fatal:N", alt.value("lightgray"), title="Fatal?"
            ),
            tooltip=[
                alt.Tooltip("count()", title="Number of Shootings"),
                alt.Tooltip("ZillowName", title="Neighborhood"),
                alt.Tooltip("fatal", title="Fatal?"),
            ],
        )
        .add_selection(brush)
        .properties(
            width=400,
            height=800,
            title="Shootings in the Last %d Days by Neighborhood" % days,
        )
    )

    # shootings by victim age
    chart2 = (
        base.mark_bar()
        .encode(
            y=alt.Y("age:Q", bin=True, scale=alt.Scale(domain=(0, 100))),
            x="count()",
            color="fatal:N",
            tooltip=["count()", "age", "fatal"],
        )
        .transform_filter(brush)
        .properties(width=300, title="Number of Shootings by Victim's Age")
    )

    # shootings by race
    chart3 = (
        base.mark_bar()
        .encode(
            y=alt.X("race:N"),
            x="count()",
            color="fatal:N",
            tooltip=["count()", "race", "fatal"],
        )
        .transform_filter(brush)
        .properties(width=300, title="Number of Shootings by Victim's Race")
    )

    return chart1 | alt.vconcat(chart2, chart3)


markdown_text = """
# Shootings in Philadelphia

This is markdown.
"""


# set the layout
app.layout = html.Div(
    [
        # the title!
        dcc.Markdown(markdown_text),
        #  this Div holds the slider
        html.Div(
            [
                # P ELEMENT FOR TITLE
                html.P(id="title", children=""),
                # DIV ELEMENT FOR DAYS SLIDER
                html.Div(
                    [
                        html.Label("Select the number of days to query"),
                        dcc.Slider(id="daysSlider", min=30, max=365, value=90),
                    ],
                    style={
                        "width": "250px",
                        "margin-right": "auto",
                        "margin-left": "auto",
                        "text-align": "center",
                    },
                ),
                # DIV ELEMENT FOR RACE DROPDOWN
                html.Div(
                    [
                        html.Label("Race"),
                        dcc.Dropdown(
                            id="raceDropdown",
                            options=[
                                {"label": i, "value": i} for i in ["W", "B", "A", "I"]
                            ],
                            value="W",
                        ),
                    ],
                    style={
                        "width": "250px",
                        "margin-right": "auto",
                        "margin-left": "auto",
                        "text-align": "center",
                    },
                ),
            ],
        ),
        # CHART IFRAME
        html.Div(
            [
                html.Iframe(
                    id="chart",
                    height="1000",
                    width="1100",
                    sandbox="allow-scripts",
                    style={"border-width": "0px", "align": "center"},
                )
            ],
            style={"display": "flex", "justify-content": "center"},
        ),
    ]
)


@app.callback(
    [
        dash.dependencies.Output("chart", "srcDoc"),
        dash.dependencies.Output("title", "children"),
    ],
    [
        dash.dependencies.Input("daysSlider", "value"),
        dash.dependencies.Input(
            "raceDropdown", "value"
        ),  # NEW: Input for race dropdown
    ],
)
def render(days, race):

    # query the CARTO database
    gdf = get_data(days)

    # NEW: select data for selected race
    gdf = gdf.loc[gdf["race"] == race]

    # count shootings and homicides
    shootings = len(gdf)
    homicides = (gdf.fatal == "Yes").sum()
    args = (shootings, homicides, days)
    title = "There have been %d shootings and %d homicides in the last %d days." % args

    # do a spatial join with ZIP codes
    hoods.crs = gdf.crs
    joined = gpd.sjoin(gdf, hoods, how="left", op="within").dropna(
        subset=["ZillowName"]
    )

    # make our chart
    chart = make_altair_chart(joined, days)

    # Save html as a StringIO object in memory
    cars_html = io.StringIO()
    chart.save(cars_html, "html")

    # Return the html from StringIO object
    return cars_html.getvalue(), title


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=5000, debug=True)
