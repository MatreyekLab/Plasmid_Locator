# Plasmid_Locator
This script takes in a text file as a list of plasmids and outputs a csv file providing information regarding their locations in the lab and other notes that are helpful for preparing cloning reactions:

Our lab does a lot of cloning and has a lot of plasmids that we use for the cloning reactions.  We have a spreadsheet- MatreyekLab_Plasmid_Archive.gsheet- that lists all the plasmids we own, including their locations in the lab, concentrations, antibiotic resistances, etc.  Without the following script, we would have to manually browse through this large spreadsheet to find the plasmids we need for cloning.  This script takes in a list of plasmids from HiFis.txt, matches their names to the names provided in the Plasmid_Archive spreadsheet, and produces a file: PlasmidLocator_Output.csv, which contains the information we need for only the plasmids we are currently interested in.

# Save MatreyekLab_Plasmid_Archive Excel spreadsheet to your working directory:
  Go to MatreyekLab_Plasmid_Archive.gsheet: https://docs.google.com/spreadsheets/d/1Jum9esm3ro2U_HGY4ZvMwEcti9W8bj8Oq8Cdrkh7ANk/edit#gid=0
  Download as .xlsx: 
      Go to: File --> Download --> Microsoft Excel (.xlsx) and save to your working directory.
      
# Edit HiFis.txt
  Add your list of plasmids, line-by-line, GXXX code only, to HiFis.txt.
  Do NOT press "Enter" after the last plasmid.
  Save to your working directory.
  
# Save PlasmidLocator.py to your working directory and run
  Open the terminal and enter in: python plasmidlocator.py.
  The script will print the information for the plasmids that were entered into Hifis.txt into the terminal and save the output into PlasmidLocator_Output.csv
    
