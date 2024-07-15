import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import os
import re

def parse_bibtex(bibtex_file):
    with open(bibtex_file, 'r', encoding='utf-8') as bibfile:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibfile, parser=parser)
    return bib_database.entries

def dir_create_if_not_exist(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

def create_bib_file(entry, path):

    filename = 'cite.bib'
    with open(os.path.join(path,filename),'w') as f:
            content="@article{" + entry['ID']+ ",\n"
            f.write(content)

    with open(os.path.join(path,filename),'a') as f:
        for key, value in entry.items():
            if key not in ["ID", "ENTRYTYPE"]:
                content=" " + key +"={"+ value +"},\n"
                f.write(content)

    with open(os.path.join(path,filename),'a') as f:
            content="}\n"
            f.write(content)

def create_author_list(entry):
    author_list = entry['author']
    detection = re.findall(r'\band\b',author_list)
    if detection:
        author_list_val = re.sub(r'\band\b\s*',';',author_list)
        author_list_val = author_list_val.split(';')
    else: 
        author_list_val = author_list.split(',')

    author_list_md = ""
    for author in author_list_val:
        author = re.sub(r',','',author)
        print(author)
        author_list_md +="\n- {}".format(author)
    return author_list_md




def input_markdown_template(entry,path):
     
    article_title = f"""
---
title: "{entry['title']}"

"""
    author_list_md = "authors:" + create_author_list(entry)
    author_contrib_list = f"""
author_notes:
- 
date: "2015-09-01T00:00:00Z"
doi: "VALUE"


publishDate: 

publication_types: ["article-journal"]



# Publication name and optional abbreviated publication name.
publication: "{entry['journal']}"
publication_short: ""

abstract: Abs

# Summary. An optional shortened abstract.
summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

url: "link"
url_pdf: 'arxiv link'
url_code: 'code link'

image:
  caption: '[](./featured.jpg)'
  focal_point: ""
  preview_only: false

projects: []

slides: 
---

"""
    with open(os.path.join(path,"index.md"),'w') as f:
        f.write(article_title)
        f.write(author_list_md)
        f.write(author_contrib_list)

     


def create_bib_files(entries, base_dir):

    for entry in entries:
        path_folder = os.path.join(base_dir,entry['ID'])
        dir_create_if_not_exist(path_folder)
        create_bib_file(entry, path_folder)
        input_markdown_template(entry,path_folder)


def save_markdown(markdown, output_file):
    with open(output_file, 'w', encoding='utf-8') as mdfile:
        mdfile.write(markdown)

def main():
    bibtex_file = 'bibfile.bib'
    output_file = 'references.md'

    entries = parse_bibtex(bibtex_file)
    markdown = create_bib_files(entries,'.')
    # save_markdown(markdown, output_file)
    # print("Markdown file generated successfully.")

if __name__ == "__main__":
    main()

# f"""
# ---
# title: "{title}"
# authors:
# - admin
# - Robert Ford
# author_notes:
# - "Equal contribution"
# - "Equal contribution"
# date: "2015-09-01T00:00:00Z"
# doi: ""

# # Schedule page publish date (NOT publication's date).
# publishDate: "2017-01-01T00:00:00Z"

# # Publication type.
# # Accepts a single type but formatted as a YAML list (for Hugo requirements).
# # Enter a publication type from the CSL standard.
# publication_types: ["article-journal"]

# # Publication name and optional abbreviated publication name.
# publication: "*Journal of Source Themes, 1*(1)"
# publication_short: ""

# abstract: 

# # Summary. An optional shortened abstract.
# summary: 

# tags:
# - Source Themes
# featured: false

# # links:
# # - name: ""
# #   url: ""
# url_pdf: http://arxiv.org/pdf/1512.04133v1
# url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
# url_dataset: ''
# url_poster: ''
# url_project: ''
# url_slides: ''
# url_source: ''
# url_video: ''

# # Featured image
# # To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
#   focal_point: ""
#   preview_only: false

# # Associated Projects (optional).
# #   Associate this publication with one or more of your projects.
# #   Simply enter your project's folder or file name without extension.
# #   E.g. `internal-project` references `content/project/internal-project/index.md`.
# #   Otherwise, set `projects: []`.
# projects: []

# # Slides (optional).
# #   Associate this publication with Markdown slides.
# #   Simply enter your slide deck's filename without extension.
# #   E.g. `slides: "example"` references `content/slides/example/index.md`.
# #   Otherwise, set `slides: ""`.
# slides: example
# ---

# {{% callout note %}}
# Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
# {{% /callout %}}

# {{% callout note %}}
# Create your slides in Markdown - click the *Slides* button to check out the example.
# {{% /callout %}}

# Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
# """