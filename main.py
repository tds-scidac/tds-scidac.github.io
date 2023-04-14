import pybtex.database.input.bibtex
import pybtex.plugin
import codecs
import latexcodec
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.template import *
from pybtex.richtext import Symbol, Text
import re

def define_env(env):
    "Hook function"

    class MyStyle(BaseStyle):

        @staticmethod
        def dashify(text):
            dash_re = re.compile(r'-+')
            return Text(Symbol('ndash')).join(text.split(dash_re))

        def format_names(self, role, as_sentence=True):
            formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=', and ')
            if as_sentence:
                return sentence [formatted_names]
            else:
                return formatted_names
        
        def format_article(self, entry):
            pages = field('pages', apply_func=self.dashify)
            date = words [field('year')]
            if 'volume' in entry['entry'].fields.keys():
                volume_and_pages = join [field('volume'), optional [':', pages]]
            else:
                volume_and_pages = words [ optional [pages]]
            if 'url' in entry['entry'].fields.keys():
                url = field('url', raw=True)
                title = href[url, field('title')]
            elif 'doi' in entry['entry'].fields.keys():
                url = join ["https://doi.org/", field('doi', raw=True)]
                title = href[url, field('title')]
            else:
                title = field('title')

            template = toplevel [
               self.format_names('author'),
               sentence [title],
               sentence [tag('emph') [field('journal')], 
                         volume_and_pages], 
               sentence [tag('strong') [date]],
            ]
            return template.format_data(entry)


    @env.macro
    def parse_bibtex(filename,year="*"):
        style = MyStyle(abbreviate_names=True)
        backend = pybtex.plugin.find_plugin('pybtex.backends', 'markdown')()
        parser = pybtex.database.input.bibtex.Parser()
        with codecs.open(filename, encoding="utf-8") as stream:
            data = parser.parse_stream(stream)
        s = ""
        for fmt_entry,entry in zip(style.format_entries(data.entries.values()),data.entries.values()):
            if year == "*":
                s += "1. "+ fmt_entry.text.render(backend) + "\n" 
            elif entry.fields['year'] == year:
                s += "1. "+ fmt_entry.text.render(backend) + "\n" 
        return s
