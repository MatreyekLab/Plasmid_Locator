
#enter your list of plasmids (line-by-line, GXXX code only) into HiFis.txt. Do NOT press ENTER after the last HiFi. Save.
#make sure that PlasmidLocator_Output.csv is closed. Otherwise, you will get an error that permission is denied
#Enter the \MatreyekLab_GoogleDrive\Inentories directory

#Clear contents of PlasmidLocator_Output.csv, enter in the header, and close
PlasmidLocator_Output = open('PlasmidLocator_Output.csv', mode = 'w')
PlasmidLocator_Output.seek(0)
PlasmidLocator_Output.truncate(0)
PlasmidLocator_Output.writelines(' , Designation, Name, ng/ul, Comment1, Antibiotic_res, \n')
PlasmidLocator_Output.close()

import pandas as pd 

#import each sheet from the Plasmid_Archive excel file as a DataFrame; replace empty spaces with "NaN"
Box1 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box1', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box2 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box2', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box3 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box3', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box4 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box4', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box5 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box5', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box6 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box6', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box7 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box7', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box8 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box8', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box9 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box9', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box10 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box10', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box11 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box11', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box12 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box12', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box13 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box13', usecols = ('Name', 'Designation', 'ng/ul', 'Comment1'), na_filter=False)
Box14 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box14', usecols = ('Name', 'Designation', 'ng/ul', 'Antibiotic_res', 'Comment1'), na_filter=False)
Box15 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box15', usecols = ('Name', 'Designation', 'ng/ul', 'Antibiotic_res', 'Comment1'), na_filter=False)
#Box16 = pd.read_excel('MatreyekLab_Plasmid_Archive.xlsx', sheet_name='Box15', usecols = ('Name', 'Designation', 'ng/ul', 'Antibiotic_res', 'Comment1'), na_filter=False)

#Create a DataFrame that includes all of the above DataFrames
#Don't forget to append any new sheets added
Plasmid_Archive = Box1.append([Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, Box10, Box11, Box12, Box13, Box14, Box15])

#define empty list HiFis
HiFis = []

#Open HiFis.txt, line-by-line
#run the df[df['A'].str.contains()] function on each line in HiFis to find the partially matching name in the Plasmid Archive
#print to terminal and save to PlasmidLocator_Output.csv
with open('HiFis.txt', 'r') as file:
	HiFis = [GXXX.rstrip() for GXXX in file.readlines()]
	for line in HiFis:
		print(Plasmid_Archive[Plasmid_Archive['Name'].str.contains(line)])
		PlasmidLocator = Plasmid_Archive[Plasmid_Archive['Name'].str.contains(line)]
		PlasmidLocator.to_csv("PlasmidLocator_Output.csv", header = False, mode = 'a')

