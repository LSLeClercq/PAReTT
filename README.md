# PAReTT
## Python Automated Retrieval of TimeTree data
version 1.0.1
### Introduction
PAReTT is a menu-driven module used to interact with the [Time Tree](http://www.timetree.org/) resource, specifically 
designed to automate batch retrieval of data for a list of species. Three main types of data can be retrieved using PAReTT:
(1) Divergence times, between an individual pair or between all species in a list, (2) Evolutionary timelines, for indivuals
or a list species, and (3) Time trees of the divergence times, either for all available species within a specified taxon or
between individual species supplied as a list.
When working with a list of species, the best place to start is by using the first menu option to check the data availability 
of species in the list and removing any species for which data is not available. When retrieving data for longer lists (>5-10)
server issues may result in missing values which can be checked and replaced using the data validation menu option after the run.

Dependencies:
- Panda
- BioPython (for handling newick trees)
- Splinter (for interacting with the server)
- Geckodriver (Added to PATH)
  
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
   q) Quit
----------------------------------------
```
input is given as lower case '*','a','b','c','d','e','f', or 'q'
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
  
</p>
</details>

#### a) Get Divergence Times (pair)
- Takes a pair of species as input to look up divergence times e.g. Taxon a: *Passer montanus*, Taxon b: *Halcyon senegalensis*
- Prints divergence time of pair on screen
#### b) Get Divergence Times (batch)
- Takes a list of species as input to look up divergence times from a **.txt** input file e.g. **Species.txt**
- Prints divergence time of pair on screen
- Provides option to save results to a file in **.csv** format e.g. **Output.csv**
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
  
- If no missing values are detected, will print 'No missing values'
  
- If missing values are detected they are printed to the screen and an attempt will be made to look up those values
  
- Asks for file name to store the missing values as a **.csv** file e.g. **missing.csv**
</p>
</details>  
<details><summary>b) Replace missing</summary>
<p>
  
- Used to replace the missing values (divergence times) from a long list of species
  
- Takes two input files, one with the divergence times and one with the missing values detected using 'Check missing' 
  
- Asks for file name to store the validated dataset of divergence times
</p>
</details>  
<details><summary>c) View tree</summary>
<p>
  
- Takes a newick tree as input and renders a basic display of tree topology
</p>
</details>

#### q) Quit
Exits program
