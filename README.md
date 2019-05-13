# multiprocessing_py
Multiprocessing in Python 3 through different workloads

## How to Use
The usage of this application is fairly simple. It is a simple CLI that takes user input in order to test through various workloads. The user can choose from various workloads and specify how many processes they would like to complete it on. The runtimes are they given. One is also able to make a graph of the test results. 


### Step 1
Use Conda to enter into a Python 3.6 environment. On the iLab, this can be done by the following command: 
`source activate python36`

### Step 2
Navigate to the directory of main.py in the multiprocessing_py folder. Once here, you will see a requirements.txt file.
Run the command: `conda install --file requirements.txt`

### Step 3
Once the dependencies have been installed, you are ready to run the application. This is done by running: `python main.py`

## Tests and Functions
### Web Scraping
This test will scrape weather from various cities. The information will be put into CSVs and stored into the weatherCSVs folder. 

### Calculating Primes
This test will calculate all of the prime numbers up until 100000. The numbers will be stored in the `primeNumbers.txt` file.

### Compressing Text
This test will compress and decompress several text files stored in `/testFiles/`. The compressed output files are put in `/compressedFiles` and once decompressed again will be put in the `/decompressedFiles` folder.

### Encoding Images
This test will grab images from Reddit and enconde them using Unidecode.

### Sorting Integer List
This test will sort 100000 arrays of size 100. The output is not stored.

### Fibonacci
This test will find the first 15 fibonacci numbers in a recursive algorithm. The output is not stored. 

### Create Graph
This function will run each test with 1-16 processes and will create a line graph showing the runtimes of each. This will be stored as a `.png` file in the root directory of the project

### Clean Workspace
This function will delete all the files that were created as output during the previously listed tests.

### Quit Program
This function will exit from the program
