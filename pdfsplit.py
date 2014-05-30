#!/usr/bin/env python
# coding: utf-8

try:
    import warnings
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=DeprecationWarning)
        from pyPdf import PdfFileWriter, PdfFileReader
    except ImportError as e:
        raise(e)
from optparse import OptionParser
import types

class PdfSplit(object):

    def __init__(self):
        pass

    def count(self, f):
        reader = PdfFileReader(file(f, "rb"))
        return reader.getNumPages()

    def split(self, src, dst, pages):
        if pages.startswith('-') or pages.endswith('-') or pages.startswith(',') or pages.endswith(','):
            return "Error: Invalid page sequence"
        elif '-' in pages:
            try:
                fpage, lpage = [ int(x) for x in pages.split('-') ]
                if fpage == 0:
                    return "Error: The first page must be greater than zero"
                elif lpage <= fpage:
                    return "Error: The last page must be greater than first page"
                elif fpage > 0 and lpage > fpage:
                    pages = [ x for x in range(fpage, lpage) ]
                    pages.append(pages[-1] + 1)
            except:
                return "Error: Invalid page sequence"
        elif ',' in pages:
            pages = [ int(x) for x in pages.split(',') if int(x) > 0 ]

        try:
            reader = PdfFileReader(file(src, "rb"))
            writer = PdfFileWriter()
            outputStream = file(dst, "wb")
            if isinstance(pages, types.StringType):
                try:
                    pages = int(pages)
                except:
                    pass
            if isinstance(pages, types.ListType):
                if self.count(src) < pages[-1]:
                    return "Error: The last page number is greater than last document page"
                pages = [ x - 1 for x in pages ]
                [ writer.addPage(reader.getPage(page)) for page in pages ]
            elif isinstance(pages, types.IntType) and pages > 0:
                if self.count(src) < pages:
                    return "Error: The page number is greater than last document page"
                writer.addPage(reader.getPage(pages - 1))
            else:
                return "Error: The page must be a integer number greater than zero"
            writer.write(outputStream)
            outputStream.close()
            return "The %s file has been created successfully" % dst
        except IOError as e:
            return "Error: %s" % repr(e)

def main():
    parser = OptionParser()
    parser.add_option("-f", "--input-file", dest="filename", help="input file name")
    parser.add_option("-c", "--count", dest="count", help="count file page numbers")
    parser.add_option("-o", "--output-file", dest="output", help="output file name")
    parser.add_option("-p", "--pages", dest="pages", help="document pages, ex: -p 1,3,5,7 or -p 10-20")
    (options, args) = parser.parse_args()

    pdf = PdfSplit()

    if options.filename is not None and options.count is not None:
        print "The %s file has %s pages" % (options.filename, pdf.count(options.filename))
    elif options.filename is None or options.output is None or options.pages is None:
        parser.print_help()
    else:
        result = pdf.split(options.filename, options.output, options.pages)
        print result

if __name__ == '__main__':
    main()
