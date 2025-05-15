#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os.path
from pathlib import Path
from bs4 import BeautifulSoup
from typing import List, Tuple


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def get_file_names (directory):
    """
    Given a directory, return a list of all the HTML files in that directory
    Returns: List of Path objects for HTML files
    """
    path = Path(directory)
    file_names = [f for f in path.iterdir() if f.is_file() and f.suffix == '.html']
    # Print files for debugging
    file_names.sort()
    file_names = [f.name for f in file_names]
    for name in file_names:
      print(f"Found file: {name}")
    return file_names

def get_file_names_extract_year(directory):
    """
    Given a directory, return a list of all the HTML files in that directory
    Returns: List of Path objects for HTML files
    """
    path = Path(directory)
    file_names = [f for f in path.iterdir() if f.is_file() and f.suffix == '.html']
    # Print files for debugging
    file_names.sort()
    file_names = [f.name for f in file_names]
    year_list = [int(i[4:8]) for i in file_names]
    # for name in file_names:
    #   year = name[4:8]
    #   print(f"Found file: {year}")
    return year_list

def extract_names_and_ranks(html_file: str) -> List[Tuple[str, str]]:
    """
    Extract names and their rankings from a baby names HTML file.
    
    Args:
        html_file: Path to the HTML file containing baby name rankings
        
    Returns:
        List of tuples containing (name, rank)
        
    Raises:
        FileNotFoundError: If the HTML file doesn't exist
        ValueError: If the file isn't HTML or required data isn't found
    """
    file_path = Path(html_file)
    
    if not file_path.exists():
        raise FileNotFoundError(f"HTML file not found: {file_path}")
    if file_path.suffix != '.html':
        raise ValueError("File must be an HTML file")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        # Add this after opening the file
        print(f"Debug: File contents length: {len(f.read())}")
        f.seek(0)  # Reset file pointer to beginning
        
        # Extract year
        year_header = soup.find('h3', align='center')
        if not year_header:
            raise ValueError("Year header not found in HTML file")
        year = re.search(r'\d+', year_header.text).group()
        
        # Extract names and ranks
        rows = soup.find_all('tr', align='right')
        if rows:
            print(f"Debug: First row HTML: {rows[0]}")
        names_ranks = []
        for row in rows:
            cells = row.find_all('td', recursive=False)
            # print(f"Debug: Found {len(cells)} cells in row")
            if len(cells) == 3:
                rank = cells[0].text
                male_name = cells[1].text
                female_name = cells[2].text
                names_ranks.extend([(male_name, rank), (female_name, rank)])
        print (f"Year: {year}")
        print("Names and ranks:")
        for name, rank in names_ranks:
            print(f"{name}: {rank}")
        return year, names_ranks  

directory = Path('/Users/alexander.smith/git/google-python-exercises/babynames')    
html_file_names = get_file_names(directory)
sample_file = directory / 'baby1990.html'  # Combine paths properly
extract_names_and_ranks(str(sample_file))





def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  

  # Process each filename in args, extracting the names and ranking
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file


if __name__ == '__main__':
  main()
