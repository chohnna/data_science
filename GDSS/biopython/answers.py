from Bio import SeqIO
from collections import defaultdict, Counter

def count_records(fasta_file):
    return sum(1 for _ in SeqIO.parse(fasta_file, "fasta"))

def sequence_lengths(fasta_file):
    lengths = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        lengths.append(len(record.seq))
    return lengths

def find_orfs(sequence, reading_frame):
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs = []
    
    for i in range(reading_frame - 1, len(sequence), 3):
        if sequence[i:i+3] == start_codon:
            for j in range(i, len(sequence), 3):
                if sequence[j:j+3] in stop_codons:
                    orfs.append((i, j + 3 - i))
                    break
    return orfs

def longest_orf_in_frame(fasta_file, frame):
    longest_orf_length = 0
    longest_orf_start = None
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        orfs = find_orfs(str(record.seq), frame)
        if orfs:
            max_orf = max(orfs, key=lambda x: x[1])
            if max_orf[1] > longest_orf_length:
                longest_orf_length = max_orf[1]
                longest_orf_start = max_orf[0] + 1
                
    return longest_orf_length, longest_orf_start

def longest_orf_any_frame(fasta_file):
    longest_orf_length = 0
    
    for frame in range(1, 4):
        length, _ = longest_orf_in_frame(fasta_file, frame)
        if length > longest_orf_length:
            longest_orf_length = length
            
    return longest_orf_length

def longest_orf_in_seq(fasta_file, seq_id, frame):
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id == seq_id:
            orfs = find_orfs(str(record.seq), frame)
            if orfs:
                max_orf = max(orfs, key=lambda x: x[1])
                return max_orf[1]
    return 0

def most_frequent_repeat(fasta_file, n):
    repeat_counts = Counter()
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        for i in range(len(sequence) - n + 1):
            repeat = sequence[i:i + n]
            repeat_counts[repeat] += 1
            
    most_common_repeat = repeat_counts.most_common(1)[0]
    
    return most_common_repeat

def repeats_count(fasta_file, n):
    repeat_counts = Counter()
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        for i in range(len(sequence) - n + 1):
            repeat = sequence[i:i + n]
            repeat_counts[repeat] += 1
            
    max_count = max(repeat_counts.values())
    max_repeats = [repeat for repeat, count in repeat_counts.items() if count == max_count]
    
    return len(max_repeats)

def specific_repeat_count(fasta_file, repeat):
    count = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        count += str(record.seq).count(repeat)
    return count

fasta_file = "dna2.fasta"  # Ensure this file is in the working directory

# Q1: Number of records
num_records = count_records(fasta_file)
print(f"Number of records: {num_records}")

# Q2: Length of the longest sequence
lengths = sequence_lengths(fasta_file)
longest_length = max(lengths)
print(f"Length of the longest sequence: {longest_length}")

# Q3: Length of the shortest sequence
shortest_length = min(lengths)
print(f"Length of the shortest sequence: {shortest_length}")

# Q4: Length of the longest ORF in reading frame 2
longest_orf_length_frame_2, _ = longest_orf_in_frame(fasta_file, 2)
print(f"Length of the longest ORF in reading frame 2: {longest_orf_length_frame_2}")

# Q5: Starting position of the longest ORF in reading frame 3
_, longest_orf_start_frame_3 = longest_orf_in_frame(fasta_file, 3)
print(f"Starting position of the longest ORF in reading frame 3: {longest_orf_start_frame_3}")

# Q6: Length of the longest ORF in any forward reading frame
longest_orf_any = longest_orf_any_frame(fasta_file)
print(f"Length of the longest ORF in any forward reading frame: {longest_orf_any}")

# Q7: Longest forward ORF in the sequence with the identifier 'gi|142022655|gb|EQ086233.1|16'
longest_orf_in_specified_seq = longest_orf_in_seq(fasta_file, 'gi|142022655|gb|EQ086233.1|16', 1)  # Assuming frame 1
print(f"Longest forward ORF in the specified sequence: {longest_orf_in_specified_seq}")

# Q8: Most frequent repeat of length 6
most_frequent_6 = most_frequent_repeat(fasta_file, 6)
print(f"Most frequent repeat of length 6: {most_frequent_6[0]} (occurs {most_frequent_6[1]} times)")

# Q9: Number of different 12-base sequences that occur Max times
num_max_12_repeats = repeats_count(fasta_file, 12)
print(f"Number of different 12-base sequences that occur Max times: {num_max_12_repeats}")

# Q10: Max occurrences of a specific repeat of length 7
repeat_counts_7 = {
    "AATGGCA": specific_repeat_count(fasta_file, "AATGGCA"),
    "TGCGCGC": specific_repeat_count(fasta_file, "TGCGCGC"),
    "CATCGCC": specific_repeat_count(fasta_file, "CATCGCC"),
    "CGCGCCG": specific_repeat_count(fasta_file, "CGCGCCG")
}
max_repeat_7 = max(repeat_counts_7, key=repeat_counts_7.get)
print(f"Repeat of length 7 with maximum occurrences: {max_repeat_7} (occurs {repeat_counts_7[max_repeat_7]} times)")
