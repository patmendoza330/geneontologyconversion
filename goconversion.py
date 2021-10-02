## So this file will transform the download from the Gene Ontology website
## and convert it to something that has the Term, Category (Biological, Cellular,
## or Molecular) as well as the description and potentially any other fields that are
## useful from the download.  All data was downloaded from:
## http://geneontology.org/docs/download-ontology/ on 2/2/21

## get the path to the file and filename as well as the out file
import os
filePath = os.path.dirname(os.path.abspath(__file__))
fileName = "go.obo"
outFileName = "go.obo.txt"

# BLOCK of variables that will be needed for the file written

## These are the column headers in the new table that will be created
GoID = ""
GoName = ""
GoNameSpace = ""
GoDef = ""

## The headers in the new file which will be a tab delimited text file
out1Headers = "ID\tName\tNamespace\talt_id\tDef\n"

# Variables to run through the original file
i = 0
rowCounter = 0
printCounter = 10000
#maxRows = 50 #REMOVE LATER

# Open the file to be read and read in the first line
file1 = open(filePath + "\\" + "supporting.files" + "\\" + fileName, 'r')
line1 = file1.readline()

# Open the file to be written
out1 = open(filePath + "\\" + outFileName, 'w')
out1.write(out1Headers)

while line1:
    if rowCounter == printCounter:
        print("Working on line " + str(printCounter))
        printCounter = printCounter + 10000

        # This checks to see if the line includes a new definition, if so
        # we will grab that value, then cycle through the lines until a
        # blank line is found (i.e. a break that indicates a new definition may
        # be coming
    if line1.startswith('id:'):
        # if the line starts with id then we grab the ID and reset all
        # variables
        GoID = ""
        GoID = line1.strip()[4:]
        GOName = ""
        GoNameSpace = ""
        GoDef = ""
        out1Line = ""
        alt_id = ""
        alt_id_count = 0
        # Cycling through all of the lines after the id, we grab any of the
        # variables that we are interested in.
        while line1.strip() != "":
            if line1.startswith('name:'):
                GoName = line1.strip()[6:]
            elif line1.startswith('namespace:'):
                GoNameSpace = line1.strip()[11:]
            elif line1.startswith('alt_id:'):
                # because there can be multiple alt_ids we need to cycle
                # through them and add them comma separated into the file
                while line1.startswith('alt_id:'):
                    alt_id = alt_id + line1.strip()[8:] + ','
                    line1 = file1.readline()
                alt_id = alt_id[:-1]
            elif line1.startswith('def:'):
                GoDef = line1.strip()[5:]
            line1 = file1.readline()
        # Once we grab all of the fields that we need from the block of
        # text, we consolidate them into a tab delimited format and write
        # it to the new file
        out1Line = GoID + "\t" + GoName + "\t" + GoNameSpace + "\t" \
                   + alt_id + "\t" + GoDef + "\n"
        out1.write(out1Line)
        line1 = file1.readline()
        rowCounter = rowCounter + 1
    else:
        pass
        rowCounter = rowCounter + 1
        line1 = file1.readline()

file1.close()
out1.close()
print("Job Done!")