## Basic Search - A positional/kgram based Search Engine.

### Usage
1. To run the program and get an interactive interface, type: `./main.py`

2. A set of books should be kept in the ./books folder from which the program builds the indices. Such a set is available [here](http://courses.cse.tamu.edu/caverlee/csce670/hw/books.zip)
3. To search for something, type your query into the command-line:
`what` OR `w*t` OR `*hat` OR `wha*`
or any other combinations (only * supported)

4. To get help, type `help` or `?`

5. To terminate the program, type `exit` or hit `Ctrl+D`

### General Notes
The first time you run the search engine, it'll attempt to generate the positional and K-gram indices. The engine will prompt you to wait while it writes them. This usually takes about ~5 seconds and builds positional and K-gram indices that are ~45MB and ~7MB in size respectively. The engine will also display the time taken for the actions it performs. 

After indices are written to disk, you can type your query and get results back. On subsequent runs, indices are going to be read from disk instead of being built each time. The total ~52MB takes about 3 seconds to be loaded into memory.

User input is cleaned up from special characters, lower-cased, and finally parsed for Boolean, Phrase, and Wildcard queries. Any combination of query types is accepted.

### Authors
1. Rahul.A.R
2. Amar Lalwani
