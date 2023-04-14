import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("GenDataset.csv")

# data = {
#     "Accession": ["NC_045512", "NC_045512", "NC_045512", "NC_045512"],
#     "Length": [29903, 29903, 29903, 29903],
#     "Host": ['Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]', 'Entity["Species", "Species:HomoSapiens"]'],
#     "Sequence": [
#         "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
#         "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
#         "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG",
#         "ATTGTTTGCTTGGTCCCAAACAAACCAACCAACTTTCGATCTCTTGTTAGATCTGTTCTCTAAACGAACTTTAAAAAGGCCAACCAACGTTCGGTGTTACG"
#     ],
#     "GenBankTitle": [
#         "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
#         "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
#         "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",
#         "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome"
#     ]
# }
# df1 = pd.DataFrame(data)
# # json object to dataframe of upcoming data stream from user
# df = pd.DataFrame.from_dict(data , orient="columns")
# concatenated_df = pd.concat([df, df1], ignore_index=True)
# concatenated_df.to_csv("GenDataset.csv", index=False)

def plot_dna_helix(gene):
    """Plots a DNA double-stranded helix for a given genetic code."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim([-len(gene), len(gene)])
    ax.set_ylim([-1.5, 1.5])
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Draw the two strands of DNA
    for i in range(len(gene)):
        if gene[i] == "A":
            ax.plot([i, i+1], [0.5, -0.5], color="green", lw=2)
            ax.plot([i, i+1], [-0.5, 0.5], color="green", lw=2)
        elif gene[i] == "T":
            ax.plot([i, i+1], [0.5, -0.5], color="red", lw=2)
            ax.plot([i, i+1], [-0.5, 0.5], color="red", lw=2)
        elif gene[i] == "C":
            ax.plot([i, i+1], [0.5, -0.5], color="blue", lw=2)
            ax.plot([i, i+1], [-0.5, 0.5], color="blue", lw=2)
        elif gene[i] == "G":
            ax.plot([i, i+1], [0.5, -0.5], color="orange", lw=2)
            ax.plot([i, i+1], [-0.5, 0.5], color="orange", lw=2)
            
    # Add labels for the bases
    for i in range(len(gene)):
        ax.text(i + 0.5, 0.7, gene[i], ha="center", fontsize=14)
        
    # Add labels for the nucleotides
    ax.text(-0.5, 0, "5'", ha="right", fontsize=16)
    ax.text(len(gene) + 0.5, 0, "3'", ha="left", fontsize=16)
    ax.text(-0.5, -1, "phosphate", ha="right", fontsize=12, color="gray")
    ax.text(len(gene) + 0.5, -1, "phosphate", ha="left", fontsize=12, color="gray")
    ax.text(-0.5, 1, "sugar", ha="right", fontsize=12, color="gray")
    ax.text(len(gene) + 0.5, 1, "sugar", ha="left", fontsize=12, color="gray")
    
    plt.show()
    
df = pd.read_csv("server\GenDataset.csv")

for gene in df["Sequence"]:
    plot_dna_helix(gene)