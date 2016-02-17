import pandoc
import os

pandoc.core.PANDOC_PATH = '/usr/local/bin/pandoc'

def convert_md_to_rst():
    doc = pandoc.Document()
    doc.markdown = open('README.md').read()
    filtered = str(doc.rst)
    f = open('README', 'w+')
    f.write(filtered)
    f.close()

def main():
    convert_md_to_rst()

if __name__ == '__main__':
    main()