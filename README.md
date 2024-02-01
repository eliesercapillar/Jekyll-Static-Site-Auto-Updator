# Jekyll Static Site Auto Updator
 A simple Python3 script that converts a text file into a markdown file ready to be deployed to a static site.

## Table of Contents
- [How To Use](#Howto)
- [What I Learned](#Learned)
- [Technologies](#Tech)

## How To Use <a name = "Howto"></a>
In a command line interface, go to the directory where this script is stored. 

Type `python path/to/file.txt path/to/save/markdown/file.md`.

The script takes 2 parameters:

    1. The name of the text file to be converted.
    2. A path to save the created Markdown file.    (Optional)
        - This will typically be the _posts folder in your Jekyll site.

## What I Learned <a name = "Learned"></a>
Shortly while writing this script, I quickly realized it was pretty useless LOL. I went into a bit more detail into it [on my website](https://eliesercapillar.github.io/My-Development-Blog/experiences/automated-poster).

Regardless, I still ended up getting some more practice with opening, reading, and writing files, as well as new experience  using the [datetime](https://docs.python.org/3/library/datetime.html) and [GitPython](https://gitpython.readthedocs.io/en/stable/index.html) libraries.

## Technologies <a name = "Tech"></a>
- `Python3`
- `Git`
- `GitPython`
- `datetime`