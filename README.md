# WOS_XML
Jupyter notebook for extracting specific fields from Clarivate's Web of Science XML dataset (https://clarivate.libguides.com/c.php?g=593069&p=4117305) ino a dataframe. Largely uses the BeatifulSoup library from bs4.

Platform notes: Used my institution's high performance computing system. GPU partition, for parsing used 25 CPUs with 90 GB memory.

I. Description of Notebooks
Notebook Parse_BeautifulSoup_files.ipynb
Used to parse files from 2010, 2015, and 2020 to extract following fields:
* UID: unique identifier assigned by Web of Science to each record. Note – this is also useful for cross-checking if a record was missing any elements, either while parsing or in the file itself, by getting the full (potentially updated) record in Web of Science.
* Source Title: Name of journal or book series etc. the article is published in.
* Publisher: Publisher of the article’s journal/series.
* All Authors: List of all authors in the “WOS standard name” format, i.e., last name, first and middle initial. Example: ‘Hu, B’ or ‘Lin, XU’.
* Authors with Aff text: Lists all authors with corresponding affiliations. For multiple authors/affiliations, this is in the format organization name followed by all authors affiliated to that organization, followed by the next organization and its affiliated authors, and so on.
* No. of Authors: Number of authors listed in the record. A count of ‘All Authors’.
* Number of Affiliations: Number of distinct affiliations found with the record.
* No. of Authors with Aff: Count of authors associated with an affiliation. This may be less that “No. of Authors” since all not individuals are necessarily linked to an affiliation.

Notebook 2010-2020_WOS.ipynb
Contains results from the analysis. Also includes steps for combining the publishers having multiple subsidiaries to create the column “Publisher_new”. For instance, Wiley, Wiley-Blackwell, John Wiley & Sons, etc. all correspond to “WILEY affiliates” in the new column. If combined and renamed the name will end with “affiliates”; in some cases, when the difference was only due to a missing comma (e.g. GEOLOGICAL SOC AMER, INC and GEOLOGICAL SOC AMER INC) they were simply combined in the new column without the word affiliates. We also separated and looked at records for the University of Rochester by matching string patterns, although those files were not specifically downloaded, since that part doesn’t take long to run.

Notebook 2020_files_summary.ipynb
Notebook initially used to do the analysis with the parsed 2020 data. Also contains pivot tables to view the mean, median, and standard deviation of the number of authors and affiliations by publisher and source title. Has the commands used to combine the sub-files to create the “full” file per year.


II. Packages and Dependencies for Python
Jupyter Kernel used for all notebooks: Python 3 (3.9.9)
Platform notes: Used BlueHive (jupyter.circ.rochester.edu) on the GPU partition generally with 25 CPUs and 90 GB memory. Depending on the XML file size need anywhere between 60-90 GB memory to parse each of them. Need a fresh connection for parsing each file.

Output of session_info.show() for Parse_BeautifulSoup_files.ipynb
Click to view session information 
-----
bs4                 4.12.2
cchardet            2.1.7
pandas              1.3.4
session_info        1.0.0
-----
Click to view modules imported as dependencies 
-----
IPython             7.29.0
jupyter_client      7.0.6
jupyter_core        4.9.1
notebook            6.4.6
-----
Python 3.9.9 (main, Nov 17 2021, 12:00:30) [GCC 11.2.0]
Linux-3.10.0-1160.95.1.el7.x86_64-x86_64-with-glibc2.17
-----
Session information updated at 2023-12-03 18:52

Output of session_info.show() for 2010-2020_WOS.ipynb
Click to view session information 
-----
matplotlib          3.5.0
numpy               1.21.4
pandas              1.3.4
plotly              5.18.0
seaborn             0.11.2
session_info        1.0.0
-----
Click to view modules imported as dependencies 
-----
IPython             7.29.0
jupyter_client      7.0.6
jupyter_core        4.9.1
notebook            6.4.6
-----
Python 3.9.9 (main, Nov 17 2021, 12:00:30) [GCC 11.2.0]
Linux-3.10.0-1160.95.1.el7.x86_64-x86_64-with-glibc2.17
-----
Session information updated at 2023-12-03 18:48

Output of session_info.show() for 2020_files_summary.ipynb
Click to view session information 
-----
matplotlib          3.5.0
numpy               1.21.4
pandas              1.3.4
seaborn             0.11.2
session_info        1.0.0
-----
Click to view modules imported as dependencies 
-----
IPython             7.29.0
jupyter_client      7.0.6
jupyter_core        4.9.1
notebook            6.4.6
-----
Python 3.9.9 (main, Nov 17 2021, 12:00:30) [GCC 11.2.0]
Linux-3.10.0-1160.95.1.el7.x86_64-x86_64-with-glibc2.17
-----
Session information updated at 2023-12-03 18:42
