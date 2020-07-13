#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
inputs:
    sequence: File

outputs:
    phylogenimic_tree:
        type: File
        outputSource: Phylogenetic_tree_generation_operation_0547/out_port_tree_file_nxs

steps:
    Sequencing_quality_control:
        run:    programs/remove_pipe.yml
        in:  
                in_port_sequence_input: sequence
        out:    [out_port_sequence_validated]

    Sequence_alignment_operation_0292:
        run:    programs/mafft.yml
        in:
                out_port_sequence_validated: Sequencing_quality_control/out_port_sequence_validated
        out:    out_port_aligned_txt_file
    
    Sequence_alignment_refinament_operation_2089:
        run: programs/model_generator.yml
        in:  
            out_port_aligned_fasta_file: Sequence_alignment_operation_0292/out_port_aligned_fasta_file
        out:    [out_port_evolutive_model]

    Phylogenetic_tree_generation_operation_0547:
        run: programs/raxml.yml
        in:
            out_port_aligned_fasta_file: Sequence_alignment_operation_0292/out_port_aligned_fasta_file
            out_port_evolutive_model: Sequence_alignment_refinament_operation_2089/out_port_evolutive_model

        out: out_port_tree_file_nxs
        
$namespaces:
    edam: http://edamontology.org/
$schemas:
- http://edamontology.org/EDAM_1.18.owl