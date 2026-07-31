#!/usr/bin/env python

import sys

blastout = sys.argv[1]     #First argument after the script file itself
bedfile = sys.argv[2]

with open(blastout) as fin:
    blast_lines = fin.readlines()    #Returns a list with each line of blast output file as an element

with open(bedfile) as fin:
    bed_lines = fin.readlines()      #Returns a list with each line of bed file as an element

good_hits = []

for hit in blast_lines:
    _, seqid, pcnt, matchlen, _, _, _, _, blast_sstart, blast_send, _, _, qlen = hit.split()
    pcnt = float(pcnt)
    matchlen = int(matchlen)
    blast_sstart = int(blast_sstart)
    blast_send = int(blast_send)
    qlen = int(qlen)


    if(
        pcnt < 30
        or
        matchlen < 0.9*qlen
        ):
        continue

    if blast_sstart < blast_send:
        blast_orientation = "+"
    else:
        blast_orientation = "-"


    for feat in bed_lines:

        bed_sid, bed_start, bed_end, gene, _, bed_orientation = feat.split()

        bed_start = int(bed_start)
        bed_end = int(bed_end)

        if bed_end< blast_sstart:
            continue
        if seqid != bed_sid:
            continue
        if bed_start > blast_send:
            break

        if blast_orientation != bed_orientation:
            continue

        if (
            blast_sstart > bed_start 
            and
            blast_sstart < bed_end 
            and
            blast_send > bed_start 
            and
            blast_send < bed_end
            ):

            good_hits.append(gene)

unique_homologs = set(good_hits)

print(unique_homologs)
print(len(unique_homologs))