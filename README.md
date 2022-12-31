![1355890 (1)](https://user-images.githubusercontent.com/85708751/173954559-8cb43e97-c0c5-4442-9e9a-4bfcc7dbe97f.png) ![image](https://user-images.githubusercontent.com/85708751/176173704-851e3776-9e22-40eb-a1ec-329db2db4e35.png) <img align="right" src="https://user-images.githubusercontent.com/85708751/176286890-15060001-79ba-4035-a815-e8cf821cec86.png"> 

#   
## Python Automated Retrieval of TimeTree data
![Language](https://img.shields.io/badge/Language-Python-yellow)  ![Version](https://img.shields.io/badge/Version-1.0.1-purple) ![Windows](https://img.shields.io/badge/OS-Windows-green) ![License](https://img.shields.io/badge/License-Apache_2.0-red) [![DOI](https://zenodo.org/badge/503310621.svg)](https://zenodo.org/badge/latestdoi/503310621-purple)
### Introduction
PAReTT is a menu-driven module used to interact with the [Time Tree](http://www.timetree.org/) resource, specifically 
designed to automate batch retrieval of data for a list of species. Three main types of data can be retrieved using PAReTT:
(1) Divergence times, between an individual pair or between all species in a list, (2) Evolutionary timelines, for individuals
or a list species, and (3) Time trees of the divergence times, either for all available species within a specified taxon or
between individual species supplied as a list.
When working with a list of species, the best place to start is by using the first menu option to check the data availability 
of species in the list and removing any species for which data is not available. 

**Cite as (preprint):** Le Clercq L.S., Grobler J.P., Kotze A., and Dalton D.L. PAReTT: a Python package for the Automated Retrieval and management of divergence time data from the Time Tree resource. Authorea. September 22, 2022.
DOI: [10.22541/au.166384820.08397260/v1](https://www.authorea.com/doi/full/10.22541/au.166384820.08397260)

**Dependencies:**
- OS: Windows
- Python >= 3.6
- Numpy >= 1.20.1
- Pandas >= 1.2.4
- Math
- Bio >= 1.3.9 (for handling newick trees)
- Splinter >= 0.17.0 (for interacting with the server)
- Selenium >= 4.1.5
- [Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.31.0) >= 0.31.0 [(Added to PATH)](http://www.learningaboutelectronics.com/Articles/How-to-install-geckodriver-Python-windows.php)
- [Firefox browser](https://www.mozilla.org/en-US/firefox/new/)

**Installation:**

After downloading and extracting the zip archive PAReTT can be implemented in by navigating to the directory and using one of two methods:
```
python parett.py
```
or
```
python setup.py install
python -m parett
```
-> This option will install the relevant dependencies automatically

A pre-compiled stand-alone Windows executable is also available. [![DOI](https://img.shields.io/badge/doi-10.5281/zenodo.6653321-orange)](https://doi.org/10.5281/zenodo.6653321)

### Main menu
The following options are available through the main menu:
```
MAIN MENU:
----------------------------------------
Choose one of the following options?
   *) Check data availability
   a) Get Divergence Times (pair)
   b) Get Divergence Times (batch)
   c) Get Evolutionary Timeline
   d) Build a Time Tree
   e) Print citation
   f) Validate datafile
   g) Calculate Diversification rate (r)
   q) Quit
----------------------------------------
```
input is given as lower case '*','a','b','c','d','e','f', 'g', or 'q'
e.g.
```
Choice: a
```
#### *) Check data availability
Brings up the menu to first check the TimeTree.org website for availability of divergence time data of your study species.
```
AVAILABILITY MENU:
----------------------------------------
Choose one of the following options?
     i) Individual
     l) List
     m) Main menu
----------------------------------------
```
input is given as lower case 'i', 'l', or 'm' (return to main menu)

<details><summary>i) Individual</summary>
<p>
  
- Takes an individual species as input to look up data availability e.g. *Passer montanus*
  
- Prints availability on screen
  
</p>
</details>

<details><summary>l) List</summary>
<p>
  
- Takes a list of species as input in from a **.txt** input file e.g. **Species.txt**
  
- Prints availability on screen
  
- Provides option to save results to a file in **.csv** format e.g. **Availability.csv**
  
e.g.
  |Species|TimeTree.Data|
  |---|---|
  |Setophaga ruticilla|Available|
  |Hirundo rustica|Available|
  |Setophaga striata|Available|

</p>
</details>

#### a) Get Divergence Times (pair)
- Takes a pair of species as input to look up divergence times e.g. Taxon a: *Passer montanus*, Taxon b: *Halcyon senegalensis*
- Prints divergence time of pair on screen
#### b) Get Divergence Times (batch)
- Takes a list of species as input to look up divergence times from a **.txt** input file e.g. **Species.txt**
- Prints divergence time of pair on screen
- Provides option to save results to a file in **.csv** format e.g. **Output.csv**

e.g.
 |Taxa1|Taxa2|Div.Time|
 |---|---|---|
 |Setophaga ruticilla|Setophaga ruticilla|0|
 |Setophaga ruticilla|Hirundo rustica|35|
 |Setophaga ruticilla|Setophaga striata|3.52|
 |Hirundo rustica|Setophaga ruticilla|35|
 |Hirundo rustica|Hirundo rustica|0|
 |Hirundo rustica|Setophaga striata|35|
 |Setophaga striata|Setophaga ruticilla|3.52|
 |Setophaga striata|Hirundo rustica|35|
 |Setophaga striata|Setophaga striata|0|
 
 - When retrieving data for longer lists (>5-10) server issues may result in missing values (NA) which can be checked and replaced using the data validation menu option after the run.

#### c) Get Evolutionary Timeline
Brings up the menu options to retrieve the evolutionary timeline:
```
TIMELINE MENU:
----------------------------------------
Choose one of the following options?
     i) Individual
     l) List
     m) Main menu
----------------------------------------
```
input is given as lower case 'i', 'l', or 'm' (return to main menu)
<details><summary>i) Individual</summary>
<p>

- Takes an individual species as input to look up evolutionary timeline e.g. *Passer montanus*
  
- Downloads **.jpg** result
</p>
</details>
<details><summary>l) List</summary>
<p>

- Takes a list of species as input in from a **.txt** input file e.g. **Species.txt**
  
- Downloads **.jpg** result for each specie in list
</p>
</details>

#### d) Build a Time Tree
Brings up the time tree menu options
```
TIME TREE MENU:
----------------------------------------
Choose one of the following options?
     t) Taxon
     s) Species list
     m) Main menu
----------------------------------------
```
input is given as lower case 't', 's', or 'm' (return to main menu)
<details><summary>t) Taxon</summary>
<p>
  
- Takes the name for a taxon to get a time tree of all available species within the taxon e.g. *Saxicola*
</p>
</details>
<details><summary>s) Species list</summary>
<p>

- Takes a list of species as input in from a **.txt** input file to generate a time tree e.g. **Species.txt**
  
- Downloads the resulting time tree in the Newick format
  
- Stores replaced or missing species to a **.txt** file e.g. **replacements.txt**
</p>
</details>

#### e) Print citation
Prints the citation for the TimeTree resource
>S. Kumar, G. Stecher, M. Suleski, and S.B. Hedges, 2017.  TimeTree: a resource for timelines, timetrees, and divergence times.  Molecular Biology and Evolution 34: 1812-1819,  DOI: [10.1093/molbev/msx116](https://doi.org/10.1093/molbev/msx116)

#### f) Validate datafile
Brings up the datafile validation menu options
```
VALIDATE MENU:
----------------------------------------
      a) Check missing
      b) Replace missing
      c) View tree
      m) Main menu
----------------------------------------
```
input is given as lower case 'a', 'b', 'c', or 'm' (return to main menu)
<details><summary>a) Check missing</summary>
<p>

- Used to check for missing values from running a long list of species (>10 Species)
  
- Takes the output file (.csv) from the divergence time function and checks for any missing values
  
  e.g. 
    |Taxa1|Taxa2|Div.Time|
    |---|---|---|
    |Setophaga ruticilla|Setophaga ruticilla|0|
    |Setophaga ruticilla|Hirundo rustica|**NA**|
    |Setophaga ruticilla|Setophaga striata|3.52|
    |Hirundo rustica|Setophaga ruticilla|35|
    |Hirundo rustica|Hirundo rustica|0|
    |Hirundo rustica|Setophaga striata|**NA**|
    |Setophaga striata|Setophaga ruticilla|3.52|
    |Setophaga striata|Hirundo rustica|35|
    |Setophaga striata|Setophaga striata|0|
  
- If no missing values are detected, will print 'No missing values'
  
- If missing values are detected they are printed to the screen and an attempt will be made to look up those values
  
- Asks for file name to store the missing values as a **.csv** file e.g. **missing.csv**

  e.g. 
    |Taxa1|Taxa2|Div.Time|
    |---|---|---|
    |Setophaga ruticilla|Hirundo rustica|**35**|
    |Hirundo rustica|Setophaga striata|**35**|
</p>
</details>  
<details><summary>b) Replace missing</summary>
<p>
  
- Used to replace the missing values (divergence times) from a long list of species
  
- Takes two input files, one with the divergence times and one with the missing values detected using 'Check missing' 
  
- Asks for file name to store the validated dataset of divergence times
  
  e.g. 
    |Taxa1|Taxa2|Div.Time|
    |---|---|---|
    |Setophaga ruticilla|Setophaga ruticilla|0|
    |Setophaga ruticilla|Hirundo rustica|**35**|
    |Setophaga ruticilla|Setophaga striata|3.52|
    |Hirundo rustica|Setophaga ruticilla|35|
    |Hirundo rustica|Hirundo rustica|0|
    |Hirundo rustica|Setophaga striata|**35**|
    |Setophaga striata|Setophaga ruticilla|3.52|
    |Setophaga striata|Hirundo rustica|35|
    |Setophaga striata|Setophaga striata|0|
</p>
</details>  
<details><summary>c) View tree</summary>
<p>
  
- Takes a newick tree as input and renders a basic display of tree topology
</p>
</details>

#### g) Calulate Diversification rate (r)

- Calculates the diversification rate using the Magallon-Sanderson equation (Magallón and Sanderson, 2001)
- Takes three variables as input:

~ Species number (n)

~ Epsilon or Extinction rate fraction

~ Divergence time (t) as crown/node age

#### q) Quit
Exits program

© 2022 Le Clercq
