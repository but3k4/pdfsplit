# pdfsplit

A Python command-line tool for split large pdf files into single pages or smaller files.

## Usage

Here are some example uses:

    $ python pdfsplit.py -f document.pdf -c true
    $ python pdfsplit.py -f document.pdf -o document-1-100.pdf -p 1-100

There is help available at the command-line as well.

    $ python pdfsplit.pdf --help

Usage: pdfsplit.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILENAME, --input-file=FILENAME
                        input file name
  -c COUNT, --count=COUNT
                        count file page numbers
  -o OUTPUT, --output-file=OUTPUT
                        output file name
  -p PAGES, --pages=PAGES
                        document pages, ex: -p 1,3,5,7 or -p 10-20
