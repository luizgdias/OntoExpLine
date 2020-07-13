#!/usr/bin/env cwl-runner
cwlVersion: v1.0
$graph:
- id: remove_pipe
  class: CommandLineTool
  inputs:
    src:
      type: File
      inputBinding: {}
    object:
      type: string
      inputBinding:
          prefix: "-o"
  outputs:
    validated:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

- id: mafft
  class: CommandLineTool
  inputs:
    src:
      type: File
      inputBinding: {}
    validated_sequence:
      type: string
      inputBinding:
          prefix: "-o"
  outputs:
    aligned_sequence:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

- id: readseq
  class: CommandLineTool
  inputs:
    src:
      type: File
      inputBinding: {}
    aligned_sequence:
      type: string
      inputBinding:
          prefix: "-o"
  outputs:
    converted_sequence:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

- id: model_gen
  class: CommandLineTool
  inputs:
    src:
      type: File
      inputBinding: {}
    aligned_sequence:
      type: string
      inputBinding:
          prefix: "-o"
  outputs:
    ev_model:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

- id: raxml
  class: CommandLineTool
  inputs:
    src:
      type: File
      inputBinding: {}
    object:
      type: string
      inputBinding:
          prefix: "-o"
  outputs:
    tree:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

- id: main
  class: Workflow
  requirements:
    - class: MultipleInputFeatureRequirement
  inputs: []
  outputs:
    - id: output
      type: File
      outputSource: tree_generator/tree

  steps:
      validation:
        run: "#remove_pipe"
        in:
            src:
              default:
                class: File
                location: dir1.sequence
        out: [validated]
      
      alignment:
        run: "#mafft"
        in:
          validated_sequence: validation/validated
          # output: { default: "a.out" }
        out: [aligned_sequence]

      evolutive_model:
        run: "#model_gen"
        in:
          aligned_sequence: alignment/aligned_sequence
          # output: { default: "a.out" }
        out: [ev_model]

      converter:
        run: "#readseq"
        in:
          aligned_sequence: alignment/aligned_sequence
          # output: { default: "a.out" }
        out: [converted_sequence]

      tree_generator:
        run: "#raxml"
        in:
          objects: [alignment/aligned_sequence, evolutive_model/ev_model]
          # output: { default: "a.out" }
        out: [tree]

