
# Startpage in pure HTML/CSS

A simple startpage with custom links arranged in categories. Supports tabs thanks to CSS3.

Background fades in on page load.

No Javascript, page is manually generated with the Python script.

Default background photo from [Unsplash](https://unsplash.com).

## How to use

Create a folder for your new startpage, you can use the folder *files/* as a base.

Fill the file *links.yaml* with your links like this:

```yaml
Category:
  - Name of website: https://website.url
```

Detail the layout you want in the file *layout.yaml* like this:

```yaml
-  # first horizontal div
  -  # first vertical div
    - Category  # one category means no tabs
  -  # second vertical div
    - Tab Category 1: checked  # checked tab on page load
    - Tab Category 2
-  # second horizontal div
```

Name the background image *background.jpg*.
