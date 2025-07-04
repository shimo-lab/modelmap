
Frankenmerge 11b between HuggingFaceH4/zephyr-7b-beta and Intel/neural-chat-7b-v3-1

Merge with the following conditions (via mergekit on github)


      model: Intel/neural-chat-7b-v3-1
      layer_range: [0, 8]
      
      model: HuggingFaceH4/zephyr-7b-beta
      layer_range: [4, 12]
      
      model: Intel/neural-chat-7b-v3-1
      layer_range: [9, 16]
      
      model: HuggingFaceH4/zephyr-7b-beta
      layer_range: [13, 20]
      
      model: Intel/neural-chat-7b-v3-1
      layer_range: [17, 24]
      
      model: HuggingFaceH4/zephyr-7b-beta
      layer_range: [21, 28]
      
      model: Intel/neural-chat-7b-v3-1
      layer_range: [25, 32]

merge_method: passthrough

