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

* Preliminary exploration:
* Limpieza: a file in which information has been filtered to arrive at hypotheses.
* Visualization: 
* Storytelling: 


# Hyphotheses

* What are the differences between the main shark attack researchers?
* Ataque de tiburón segun `sexo`.
* Ataques de tiburón por `zona`.
* Ataques de tiburón en funcion de la actividad `realizada`.


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