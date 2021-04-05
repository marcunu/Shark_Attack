# Shark_Attack

This project is based on an analysis of data on shark attacks throughout the world.

# Index

* Documents
* Hipothesis
* Steps
* DataFrames
* Python libraries
* Programms


# Documents

* 01 - Preliminary exploration: preliminary scan of the DataFrame.
* 02 - Clean up: a file in which information has been filtered to arrive at hypotheses.
* 03 - Visualization: graphs on the hypotheses to be analyzed.
* 04 - Storytelling: union of data following a narrative.


# Hyphotheses

* Is there any relation between the `activity` and the `attack`? Does the shark species or age affect the type of injury?

* How many researchers there are and how much research they have carried out. Is there a shark attack specialist?


# Steps

* `Step 1`: filter the data and delete all de rows where there is no data, using the function `.dropna(axis=0, how="all")`
        * `axis` is to select the rows not the columns.
        * `how = "all"` is to delete if all the values in the rows are Nan.
        
* `Step 2`: after filtering, study hypotheses have to be selected.

* `Step 3`: analyze hypotheses and draw graphs to support them.

* `Step 4`: Link information and graphics in a way that is easily understood by another person.


# DataFrames

The `shark_attack` dataframe has been downloaded from [Kaggle](https://www.kaggle.com/teajay/global-shark-attacks)


# Programs

* Python
* Jupyter NoteBook
* Visual Code


# Python libraries

* Pandas
* Seaborn
* Mathplotlib
* Numpy
* Personal function library (limpieza_texto & visualizacion)