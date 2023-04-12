import pandas as pd

df = pd.read_csv("GenDataset.csv")

data = {
    "Accession": ["NC_045512", "NC_045512", "NC_045512", "NC_045512"],
    "Length": [29903, 29903, 29903, 29903],
    "Host": ['Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]'],
    "Sequence": [
        "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
        "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
        "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
        "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG"
    ],
    "GenBankTitle": [
        "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
        "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
        "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
        "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome"
    ]
}
df1 = pd.DataFrame(data)
# json object to dataframe of upcoming data stream from user
df = pd.DataFrame.from_dict(data , orient="columns")
concatenated_df = pd.concat([df, df1], ignore_index=True)
concatenated_df.to_csv("GenDataset.csv", index=False)