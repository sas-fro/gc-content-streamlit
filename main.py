import streamlit as st
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Seq import Seq
from io import StringIO


def show_results(sequences_string):
    stringio = StringIO(sequences_string)
    has_fasta_records = False
    
    for record in SeqIO.parse(stringio, "fasta"):
        st.write(record.description)
        st.write(gc_fraction(record.seq))
        has_fasta_records = True
    
    if not has_fasta_records:
        st.write(gc_fraction(Seq(sequences_string)))


st.title("GC Content")

st.subheader("Upload a sequence in fasta format")
input_text = st.text_area("Enter sequence", height=200, help="Can handle single DNA sequence or fasta style input")

if st.button("Calculate"):
    show_results(sequences_string=input_text)

uploaded_file = st.file_uploader("Upload a fasta file")

if uploaded_file is not None:
    stringio = uploaded_file.getvalue().decode("utf-8")
    show_results(stringio)
