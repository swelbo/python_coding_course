def fasta_alignment_from_vcf(vcf_file):
    """Get snp site alt bases as sequences from all samples in a vcf file"""

    import vcf
    from collections import defaultdict
    vcf_reader = vcf.Reader(open(vcf_file, 'rb'))  
    def default():
        return []
    result = defaultdict(default)
    sites = []
    for record in vcf_reader:
        ref = record.REF
        result['ref'].append(record.REF)
        sites.append(record.POS)
        for sample in record.samples:
            name = sample.sample
            if sample.gt_bases != None:
                result[name].append(sample.gt_bases)
            else:
                result[name].append(record.REF)
    print ('found %s sites' %len(sites))
    recs = []
    for sample in result:
        seq = ''.join(result[sample])
        seqrec = SeqRecord(Seq(seq),id=sample)
        recs.append(seqrec)

    smat = pd.DataFrame(result)
    smat.index = sites
    return recs, smat