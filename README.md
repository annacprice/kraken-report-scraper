# kraken-report-scraper
kraken-report-scraper collates information from multiple kraken report files into one csv. It expects the input kraken reports to have the file extension .txt

## **Requirements**
kraken-report-scraper requires python 3.x

## **Usage**
```
usage: reportscraper.py [-h] -i INPUT -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input-dir INPUT
                        path to the input directory
  -o OUTPUT, --output-dir OUTPUT
                        path to the output directory
```
E.g. to run
```
python reportscraper.py -i /directory/with/input/report/files -o /directory/for/output/csv
```
