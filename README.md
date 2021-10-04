# Converting non-tabular data into tabular data using Python

Integrating data of different formats is particularly challenging given the many different layouts of data. This project involved modifying a file that had non-tabular data displayed in a single column. Each term was separated by a [Term] entry, and fields for each term were separated by a colon, see below:

|                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[Term]                                                                                                                                                                                                                             |
|id: GO:0000001                                                                                                                                                                                                                     |
|name: mitochondrion inheritance                                                                                                                                                                                                    |
|namespace: biological_process                                                                                                                                                                                                      |
|def: The distribution of mitochondria, including the mitochondrial genome, into daughter cells after mitosis or meiosis, mediated by interactions between mitochondria and the cytoskeleton. [GOC:mcc PMID:10873824 PMID:11389764] |
|synonym: mitochondrial inheritance EXACT []                                                                                                                                                                                        |
|is_a: GO:0048308 ! organelle inheritance                                                                                                                                                                                           |
|is_a: GO:0048311 ! mitochondrion distribution                                                                                                                                                                                      |
|[Term]                                                                                                                                                                                                                             |
|id: GO:0000002                                                                                                                                                                                                                     |
|name: mitochondrial genome maintenance                                                                                                                                                                                             |
|namespace: biological_process                                                                                                                                                                                                      |
|def: The maintenance of the structure and integrity of the mitochondrial genome; includes replication and segregation of the mitochondrial chromosome. [GOC:ai GOC:vw]                                                             |
|is_a: GO:0007005 ! mitochondrion organization                                                                                                                                                                                      |
|[Term]                                                                                                                                                                                                                             |
|id: GO:0000003                                                                                                                                                                                                                     |
|name: reproduction                                                                                                                                                                                                                 |
|namespace: biological_process                                                                                                                                                                                                      |
|alt_id: GO:0019952                                                                                                                                                                                                                 |
|alt_id: GO:0050876                                                                                                                                                                                                                 |
|def: The production of new individuals that contain some portion of genetic material inherited from one or more parent organisms. [GOC:go_curators GOC:isa_complete GOC:jl                                                         |
|ISBN:0198506732]                                                                                                                                                                                                                   |
|subset: goslim_agr                                                                                                                                                                                                                 |
|subset: goslim_chembl                                                                                                                                                                                                              |
|subset: goslim_flybase_ribbon                                                                                                                                                                                                      |
|subset: goslim_generic                                                                                                                                                                                                             |
|subset: goslim_pir                                                                                                                                                                                                                 |
|subset: goslim_plant                                                                                                                                                                                                               |
|synonym: reproductive physiological process EXACT []                                                                                                                                                                               |
|xref: Wikipedia:Reproduction 

From above, you can see we have three terms (GO:0000001, GO:0000002, and GO:0000003). However, to join these to another dataset in tabular format we need to process this file into tabular format that appears as this:

|GO         |Name                                                     |Namespace          |alt_id                |Def                                                                                                                                                                                                                                                                                                                                |
|:----------|:--------------------------------------------------------|:------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|GO:0000001 |mitochondrion inheritance                                |biological_process |                      |The distribution of mitochondria, including the mitochondrial genome, into daughter cells after mitosis or meiosis, mediated by interactions between mitochondria and the cytoskeleton. [GOC:mcc, PMID:10873824, PMID:11389764]                                                                                                    |
|GO:0000002 |mitochondrial genome maintenance                         |biological_process |                      |The maintenance of the structure and integrity of the mitochondrial genome; includes replication and segregation of the mitochondrial chromosome. [GOC:ai, GOC:vw]                                                                                                                                                                 |
|GO:0000003 |reproduction                                             |biological_process |GO:0019952,GO:0050876 |                                                                                                                                                                                                                                                                                                                                   |
|GO:0000005 |obsolete ribosomal chaperone activity                    |molecular_function |                      |OBSOLETE. Assists in the correct assembly of ribosomes or ribosomal subunits in vivo, but is not a component of the assembled ribosome when performing its normal biological function. [GOC:jl, PMID:12150913]                                                                                                                     |
|GO:0000006 |high-affinity zinc transmembrane transporter activity    |molecular_function |                      |Enables the transfer of zinc ions (Zn2+) from one side of a membrane to the other, probably powered by proton motive force. In high-affinity transport the transporter is able to bind the solute even if it is only present at very low concentrations. [TC:2.A.5.1.1]                                                            |
|GO:0000007 |low-affinity zinc ion transmembrane transporter activity |molecular_function |                      |Enables the transfer of a solute or solutes from one side of a membrane to the other according to the reaction: Zn2+ = Zn2+, probably powered by proton motive force. In low-affinity transport the transporter is able to bind the solute only if it is present at very high concentrations. [GOC:mtg_transport, ISBN:0815340729] |

To do this, we will run a python script that will search through the file for particular breakpoints, then grab selected fields and store them in a new table. 

Additionally, this revised file will be used to make a joins to the annotation file in my [data wrangling with tidyr and dplyr](https://github.com/patmendoza330/annotationwrangling) repository.

# Background

This original file is a gene ontology definition file downloaded from [http://geneontology.org/](http://geneontology.org/) in OBO format. The annotation file that this will be joined to is already in tabular format, so we need to run a simple script that will do the conversion needed. 


# Python script

Fields pulled from the OBO file include the ID, Name, Namespace, alt_id (these are concatenated into a single column - comma separated), and Def.

The script is the file goconversion.py and needs to be downloaded along with the files in the supporting.files folder. Running the script will create a go.obo.txt file that is tab delimited with the fields indicated above.

# Citations
Ashburner, et al. (2000, 2000/05/01). Gene Ontology: tool for the unification of biology. Nature Genetics, 25(1), 25-29. https://doi.org/10.1038/75556

Gene Ontology, C. (2021). The Gene Ontology resource: enriching a GOld mine. Nucleic acids research, 49(D1), D325-D334. https://doi.org/10.1093/nar/gkaa1113 