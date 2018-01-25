#!/usr/bin/python3
# coding: utf-8

import json
import yaml
import sys


DIRECTORY = "files/"
LINKS = "links.yaml"
LAYOUT = "layout.yaml"
CSS_PATH = "templates/style.css"
HTML_PATH = "templates/template.html"
HTML_FINAL = "startpage.html"


def import_links(directory=DIRECTORY, file_name=LINKS):
    """Imports the YAML data file."""
    with open(directory+file_name, 'r') as f:
        stream = f.read()
    data = yaml.load(stream)
    return data


def import_layout(directory=DIRECTORY, file_name=LAYOUT):
    """Imports the YAML layout file."""
    with open(directory+file_name, 'r') as f:
        stream = f.read()
    layout = yaml.load(stream)
    return layout


def generate_page(layout, data, template_css=CSS_PATH,
                  template_html=HTML_PATH):
    """Generates the HTML and CSS of the startpage as a string"""
    with open(template_html, 'r') as f:
        html = f.read()
    with open(template_css, 'r') as f:
        css = f.read()
    css += '\n\n'

    links_divs = ''
    for i, vertical_divs in enumerate(layout):
        links_divs += '<div id="links">\n'

        for j, vertical_div in enumerate(vertical_divs):
            links_divs += '<div class="linksbox">\n'
            inputs = ''
            sections = ''
            tabs_name = 'tabs{}{}'.format(i, j)

            for k, category in enumerate(vertical_div):
                tab_id = 'tab{}{}{}'.format(i, j, k)
                # deal with checked categories
                if type(category) is dict:
                    category = next(iter(category))
                    checked = True
                elif len(vertical_div) == 1:
                    # only 1 tab, check it
                    checked = True
                else:
                    checked = False
                inputs += '<input id="{}" type="radio" name="{}"{}>\n'.format(
                        tab_id,
                        tabs_name,
                        ' checked' if checked else '')
                inputs += '<label for="{}">{}</label>\n'.format(tab_id, category)
                sections += '<section id="{}">\n'.format(category)
                css += '#{}:checked ~ #{},\n'.format(tab_id, category)

                for link in data[category]:
                    site = next(iter(link))
                    url = link[site]
                    sections += '<a href="{}">{}</a>\n'.format(url, site)
                sections +="</section>\n"
            links_divs += inputs
            links_divs += sections
            links_divs += '</div>\n\n'
        links_divs += '</div>\n\n'

    # take out last comma in CSS
    css = css[:-2]
    css += """\n{
    display: block;
}"""

    html = html % {'css': css, 'divs': links_divs}
    return html, css


def write_page(html, directory=DIRECTORY, file_name=HTML_FINAL):
    """Exports the HTML in the page file."""
    with open(directory+file_name, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    commands = sys.argv[1:]
    if commands:
        directory = commands[0]
        if directory[-1] != '/':
            directory += '/'
    else:
        print('no directory given, using default: {}'.format(DIRECTORY))
        directory = DIRECTORY

    data = import_links(directory)
    layout = import_layout(directory)
    html, css = generate_page(layout, data)
    write_page(html, directory)

