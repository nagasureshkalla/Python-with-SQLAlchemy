
"""
HW 1
Problem 2
Author : Kalla Naga Suresh

"""

def genes_method(genomestring):
    i=0
    list1 = []
    begin = "ATG"
    end = ["TAG", "TAA", "TGA"]
    while i < len(genomestring):
        # checking the every 3 digits for the begin string to start
        if genomestring[i:i + 3] == begin:
            j = i + 3
            # loop until any end string is found
            while j < len(genomestring):
                if genomestring[j:j + 3] in end:
                    # if found append the string between the begin and end in list1
                    gene = genomestring[i + 3:j]
                    # it satisfies the modulus 3 length
                    if len(gene) % 3 == 0:
                        list1.append(gene)
                    break
                j += 3
        i += 1
    return list1


if __name__ == '__main__':
    # Prompt the user to enter a genomestring string
    genomestring = input("Enter a genomestring string: ")

    # Find and display all genes in the genomestring
    genes = genes_method(genomestring)

    if genes:
        for gene in genes:
            print(gene)
    else:
        print("no gene is found")
