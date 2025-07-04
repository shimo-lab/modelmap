
# Peagle-9b

Hey there! 👋 Welcome to the Peagle-14b! This is a merge of multiple models brought together using the awesome [VortexMerge kit](https://colab.research.google.com/drive/1YjcvCLuNG1PK7Le6_4xhVU5VpzTwvGhk#scrollTo=UG5H2TK4gVyl).

Let's see what we've got in this merge:
* [mlabonne/NeuralBeagle14-7B](https://huggingface.co/mlabonne/NeuralBeagle14-7B) 🚀
* [eldogbbhed/NeuralPearlBeagle](https://huggingface.co/eldogbbhed/NeuralPearlBeagle) 🚀

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: mlabonne/NeuralBeagle14-7B
        layer_range: [0, 20]
  - sources:
      - model: eldogbbhed/NeuralPearlBeagle
        layer_range: [12, 32]
merge_method: passthrough 
