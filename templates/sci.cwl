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

#!/usr/bin/env cwl-runner

cwlVersion: v1.0
$graph:
- id: mafft
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
    compiled:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

#!/usr/bin/env cwl-runner

cwlVersion: v1.0
$graph:
- id: readseq
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
    compiled:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

#!/usr/bin/env cwl-runner

cwlVersion: v1.0
$graph:
- id: model_gen
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
    compiled:
      type: File
      outputBinding:
        glob: $(inputs.object)
  baseCommand: gcc
  arguments:
    - "-c"
    - "-Wall"
# ##########################################

#!/usr/bin/env cwl-runner

cwlVersion: v1.0
$graph:
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
    compiled:
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
      outputSource: linkobj/executable

  steps:
      validation:
        run: "#remove_pipe"
        in:
            src:
              default:
                class: File
                location: dir1.c
                secondaryFiles:
                  - class: File
                    location: source1.h
        out: [validated]
