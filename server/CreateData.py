from Bio import Entrez
from Bio import SeqIO
import pandas as pd

Entrez.email = "omkarborker@nitgoa.ac.in"


handle = Entrez.esearch(db="nucleotide", term="NCI[virus host] AND viruses[Organism]", retmax=1000)
record = Entrez.read(handle)

id_list = record["IdList"]

handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="gb", retmode="text")
records = handle.read()

accessions = []
lengths = []
hosts = []
sequences = []
titles = []
mutations = []
variants = []

for record in SeqIO.parse(handle, "gb"):
    accessions.append(record.id)
    lengths.append(len(record.seq))
    hosts.append(record.annotations["source"])
    sequences.append(str(record.seq))
    titles.append(record.description)
    mutations.append("") 
    variants.append("") 

df = pd.DataFrame({
    "Accession": accessions,
    "Length": lengths,
    "Host": hosts,
    "Sequence": sequences,
    "GenBankTitle": titles,
    "Mutation": mutations,
    "Variant": variants
})

df.to_csv('virus_data.csv', index=False)