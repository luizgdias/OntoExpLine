#!/usr/bin/env cwl-runner

cwlVersion: v1.0
$graph:
    -id: remove_pipe
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
    
    -id: mafft
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
        
    -id: model_gen
    class: CommandLineTool
    inputs:
        objects:
        type:  File[]
        inputBinding:
        position: 2
    output:
        type: string
        inputBinding:
            position: 1
            prefix: "-o"
    outputs:
    executable:
        type: File
        outputBinding:
            glob: $(inputs.output)
    baseCommand: gcc

    -id: readseq
    class: CommandLineTool
    inputs:
        objects:
        type:  File[]
        inputBinding:
        position: 2
    output:
        type: string
        inputBinding:
            position: 1
            prefix: "-o"
    outputs:
    executable:
        type: File
        outputBinding:
            glob: $(inputs.output)
    baseCommand: gcc

    -id: mrbayes
    class: Workflow
    requirements:
        - class: MultipleInputFeatureRequirement
    inputs: []
    outputs:
        -id: output
        type: File
        outputSource: linkobj/executable

    steps:
        validation:
            run: "#remove_pipe"
            in:
                src:
                    default:
                        class: File
                        location: source1.c
                        secondaryFiles:
                            -class: File
                            location: source1.h
                    object: { default: "source1.o" }
            out: [compiled]
        
        alignment:
            run: "#mafft"
            in:
                src:
                    default:
                        class: File
                        location: source1.c
                        secondaryFiles:
                            -class: File
                            location: source1.h
                    object: { default: "source1.o" }
            out: [compiled]

        converter:
        run: "#compile"
        in:
            src: { default: {class: File, location: "source2.c" } }
            object: { default: "source2.o" }
        out: [compiled]

        model_gen:
        run: "#model_gen"
        in:
            src: { default: {class: File, location: "source2.c" } }
            object: { default: "source2.o" }
        out: [compiled]


        tree:
        run: "#remove_pipe"
        in:
            src: { default: {class: File, location: "source2.c" } }
            object: { default: "source2.o" }
        out: [compiled]

    linkobj:
        run: "#mrbayes"
        in:
            objects: [compilesources-src1/compiled, compilesources-src2/compiled]
            output: { default: "a.out" }
        out: [executable]


