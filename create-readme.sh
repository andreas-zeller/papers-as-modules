#!/bin/sh
# Run this after changes

jupyter nbconvert --to markdown Papers-as-Modules.ipynb
mv Papers-As-Modules.md README.md
git commit -m "Generated automatically" README.md
exit 0