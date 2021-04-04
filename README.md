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

* 01 - Preliminary exploration
* 02 - Clean up: a file in which information has been filtered to arrive at hypotheses.
* 03 - Visualization 
* 04 - Storytelling


# Hyphotheses

* Is there any relation between the `activity` and the `attack`? Does the shark species or age affect the type of injury?

 

* Are sharks more aggressive depending on the `time`?


# Steps

* `Step1`: filter the data and delete all de rows where there is no data, using the function `.dropna(axis=0, how="all")`
        * `axis` is to select the rows not the columns.
        * `how = "all"` is to delete if all the values in the rows are Nan.
        
* `Step2`: after filtering, study hypotheses have to be selected.

* `Step3`: Analyse the hypotheses


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
* Personal function library