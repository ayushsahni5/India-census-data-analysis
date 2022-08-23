Plugins-
IDE:jupyter notebook 
Environment: Anaconda 1.7.2, python 3.8.8


Dependencies-
Python Libraries: pandas 1.2.4, numpy 1.19.5, scipy 1.6.2


_________________________________________________________________________________________________

.sh files:

assign2.sh 
top level script that runs the entire assignment(It runs each individual .sh file one by one. It should be run before any other script)

percent-india.sh
runs ques1.py

gender-india.sh
runs ques2.py

geography-india.sh
runs ques3.py

3-to-2-ratio.sh
runs ques4-a.py

2-to-1-ratio.sh
runs ques4-b.py

age-india.sh
runs ques5.py

literacy-india.sh
runs ques6.py

region-india.sh
runs ques7.py

age-gender.sh
runs ques8.py

literacy-gender.sh
runs ques9.py


I have written the python code in jupyter notebook (.ipynb) and then converted each to .py file. The .ipynb files have also been kept
because they are easier and attractive to read . The use of .py files is only for running python code using .sh files.


______________________________________________________________________________________________________
Datasets used:-

C-17(POPULATION BY BILINGUALISM and TRILINGUALISM) , C-18(POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX)  and C-19(POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATION LEVEL AND SEX) from https://censusindia.gov.in/2011Census/Language_MTs.html

C-14 (AGE WISE DATA) and C-08 from https://censusindia.gov.in

India census 2011 from http://censusindia.gov.in/pca/DDW_PCA0000_2011_Indiastatedist.xlsx
______________________________________________________________________________________________________

Jupyter Notebook files:

ques1.ipynb
Input: C-18 
Output: percent-india.csv

ques2.ipynb
Input: C-14 , C-18
Output: gender-india-a.csv, gender-india-b.csv, gender-india-c.csv

ques3.ipynb
Input: C-18 , C-14
Output: geography-india-a.csv , geography-india-b.csv , geography-india-c.csv

ques4-a.ipynb
Input: percent-india.csv (output file of ques1)
Output: 3-to-2-ratio.csv

ques4-b.ipynb
Input: percent-india.csv (output file of ques1)
Output: 2-to-1-ratio.csv

ques5.ipynb
Input:  C-14 , C-18
Output: age-india.csv

ques6.ipynb
Input: C-08 , C-19
Output: literacy-india.csv

ques7.ipynb
Input: C-17 ( 1 country level dataset and 35 state level datasets = total 36 datasets used)
Output: regio-india-a.csv , region-india-b.csv

ques8.ipynb
Input: C-14 , C-18
Output: age-gender-a.csv , age-gender-b.csv , age-gender-c.csv

ques9.ipynb
Input: C-08 , C-19
Output: literacy-gender-a.csv , literacy-gender-b.csv , literacy-gender-c.csv


In questions where output files have to be in part a,b and c:
     For ques2 and ques3: a refers to mono , b refers to bi and c refers to tri (linguilism)
     For ques8 and ques9: a refers to tri , b refers to bi and c refers to mono (linguilism)

____________________________________________________________________________________________________
HOW TO USE:

In the beginning, all programs need to be run sequentially
In order to run all programs sequentially, run the following command from the terminal-
./assign2.sh 

After this programs can be run individually as well

variable names have been used in a way that describes their meaning.

There are two main folders: 1) Datasets    2)Output files
This structure should not be changed. Moreover, Dataset folder also contains region wise subfolders, that should also not be changed.

Some functions used in the above programs may not work in different environment. Please refer to the version of environments and dependencies mentioned on top in readme.txt.

In my system, all the programs 1-9 take approximately 50 seconds to run. So, in worst case, let the program run for fairly more amount of time than that.

In some dataset, the column names ambiguos. For such datasets, I have mentioned the exact meaning of those columns as interpreted by me(with arguments to support my interpretation).For ex, in C-18, the column name 'number speaking second language' means the number of people who speak 2 OR MORE languages rather than number of people speaking EXACTLY 2 languages. I tried to remove other ambiguities as well and have mentioned the same in my code(.ipynb and .py files)

_____________________________________________________________________________________________________

-Ayush Sahni
Roll no 21111019
email: sayush21@iitk.ac.in
