import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import sys

# Importing transformed datasets from Azure:
sys.path.insert(0, 'D:\lina_lau\C339_datafundamentals\data_analysis_project')
from extract.extract import Extract

e = Extract()
dataset_mean = e.getCSV("testDirectory/dataset_mean.csv")
dataset_under = e.getCSV("testDirectory/dataset_under.csv")
dataset_over = e.getCSV("testDirectory/dataset_over.csv")

# Make dataframe pipeline interactive
idf_mean = dataset_mean.interactive()
idf_over = dataset_over.interactive()
idf_under = dataset_under.interactive()

# Defining panel widgets: the sex dropdown menu
year_slider = pn.widgets.IntSlider(name = 'Year slider', start = 1975, end = 2016, value = 1975)
sex_menu = pn.widgets.Select(options = ['BothSexes', 'Female', 'Male'], name = 'Sex')

# Defining Panel widgets: radio buttons for mean BMI in the pooled population
yaxis_prevalence = pn.widgets.RadioButtonGroup(
    name = 'Y axis',
    options = ['Prevalence'],
    button_type = 'success'
)

income_group = ['HighIncome', 'LowerIncome', 'LowerMiddleIncome', 'UpperMiddleIncome']

# Connecting the widgets to the dataset_mean pipeline
bmi_all_pipeline = (
    idf_mean[
        (idf_mean.TimeDim <= year_slider) &
        (idf_mean.Sex == sex_menu) & 
        (idf_mean.WorldBankIncomeGroup.isin(income_group))
    ]
    .groupby(['WorldBankIncomeGroup', 'TimeDim'])[yaxis_prevalence].mean()
    .to_frame()
    .reset_index()
    .sort_values(by = 'TimeDim')
    .reset_index(drop = True)
)

# Creating a chart using the data pipeline
bmi_all_plot = bmi_all_pipeline.hvplot(x = 'TimeDim', 
                                       by = 'WorldBankIncomeGroup', 
                                       y = yaxis_prevalence, 
                                       xlabel = "Years",
                                       ylabel = "Prevalence (%)",
                                       line_width = 2, 
                                       title = 'Mean BMI of adults by country income')

# Connecting the widgets to the dataset_over (overweight adults) pipeline
bmi_over_adult_pipeline = (
    idf_over[
        (idf_over.TimeDim <= year_slider) & 
        (idf_over.Sex == sex_menu) & 
        (idf_over.WorldBankIncomeGroup.isin(income_group))
    ]
    .groupby(['WorldBankIncomeGroup', 'TimeDim'])[yaxis_prevalence].mean()
    .to_frame()
    .reset_index()
    .sort_values(by = 'TimeDim')
    .reset_index(drop = True)
)

# Creating a chart for overweight adults
bmi_over_adult_plot = bmi_over_adult_pipeline.hvplot(x = 'TimeDim', 
                                       by = 'WorldBankIncomeGroup', 
                                       y = yaxis_prevalence, 
                                       xlabel = "Years",
                                       ylabel = "Prevalence (%)",
                                       line_width = 2, 
                                       title = 'Age-standardised prevalence of overweight adults (BMI >30 kg/m2) by country income', 
                                       width = 800)

# Connecting the widgets to the under_adult (underweight adults) pipeline
bmi_under_adult_pipeline = (
    idf_under[
        (idf_under.TimeDim <= year_slider) & 
        (idf_under.Sex == sex_menu) & 
        (idf_under.WorldBankIncomeGroup.isin(income_group))
    ]
    .groupby(['WorldBankIncomeGroup', 'TimeDim'])[yaxis_prevalence].mean()
    .to_frame()
    .reset_index()
    .sort_values(by = 'TimeDim')
    .reset_index(drop = True)
)


# Creating a chart for underweight adults
bmi_under_adult_plot = bmi_under_adult_pipeline.hvplot(x = 'TimeDim', 
                                       by = 'WorldBankIncomeGroup', 
                                       y = yaxis_prevalence, 
                                       xlabel = "Years",
                                       ylabel = "Prevalence (%)",
                                       line_width = 2, 
                                       title = 'Age-standardised prevalence of underweight adults (BMI <18 kg/m2) by country income', 
                                       width = 800, height = 400)



# Creating the dashboard

template = pn.template.FastListTemplate(
    title = 'Global Obesity Prevalence',
    sidebar = [pn.pane.Markdown("##Global prevalence of overweight and underweight people, by sex and country income (according to World Bank Classification)"),
              pn.pane.Markdown("#### Worldwide obesity has approximately tripled since 1975."),
              pn.pane.Markdown("#### In 2016, more than 1.9 bilion adults (>17 years and older), were overweight. Of these, >650 milion were obese."),
              pn.pane.Markdown("#### Most of the world's population live in countries where overweight and obesity kills more people than underweight."),
              pn.pane.JPG('https://c.ndtvimg.com/2020-06/dra42d7g_junk-food-_625x300_30_June_20.jpg', sizing_mode = 'scale_both'),
              pn.pane.Markdown("##Settings"),
              year_slider,
              sex_menu, 
              pn.pane.Markdown(" Data source: World Health Organisation (2023)")],
             
    main = [pn.Row(pn.Column(yaxis_prevalence, bmi_all_plot.panel(width = 800, height = 300), margin = (0, 25))),
            pn.Row(pn.Column(yaxis_prevalence, bmi_over_adult_plot.panel(width = 800, height = 300), margin = (0, 25))),
            pn.Row(pn.Column(yaxis_prevalence, bmi_under_adult_plot.panel(width = 800, height = 300), margin = (0, 25)))],
    accent_base_color = "#88d8b0",
    header_base_color = "#88d8b0",
)
template.show()
template.servable()
