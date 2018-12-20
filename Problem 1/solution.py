def most_chromosomes(chromosome_data):
    # this is one of many possible implementations.
    counter = {}
    for key, val in chromosome_data.items():
        counter[val] = 1 if val not in counter else counter[val]+1
    max_chrom, max_count = 0, 0
    for key, val in counter.items():
        if val > max_count:
            max_chrom = key
            max_count = val
    return max_chrom
