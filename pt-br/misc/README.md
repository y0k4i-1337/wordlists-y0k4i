## Miscellaneous wordlists

These are wordlists created for different contexts using text from Wikipedia.

An example of creating budhism wordlist using Wikipedia in PT-BR is given below:

  - Crawl Wikipedia and extract words using `cewl`:
    ```bash
    cewl -d 2 --lowercase -c --allowed 'wiki/.*' --convert-umlauts -w budhism-raw.txt -v https://pt.wikipedia.org/wiki/Budismo
    ```
  - Remove accents from words, remove words that appears only once and those
    that contains anything different than letters:
    ```bash
    cat budhism-raw.txt | sed 's/, /,/' | tr 'áéíóúãõâêîôûàèìòùäëïöüç' 'aeiouaoaeiouaeiouc' | egrep -v "[^a-z].*,[0-9]|,1$" | sort -t , -k 2  -g -r > budhism-count.txt
    ```
  - Make some manual cleaning like removing stop words.
  - Remove duplicate words while keeping original order:
    ```bash
    cat budhism-count.txt| cut -d, -f1 | awk '!x[$0]++' > budhism.txt
    ```
