
# solar megamerge 10.7b

The following models were merged with DARE using [https://github.com/martyn/safetensors-merge-supermario](https://github.com/martyn/safetensors-merge-supermario)

## Mergelist

```
models:
  - model: upstage/SOLAR-10.7B-v1.0
  - model: upstage/SOLAR-10.7B-Instruct-v1.0
    parameters:
      weight: 0.20
      density: 0.8
  - model: kyujinpy/SOLAR-Platypus-10.7B-v1
    parameters:
      weight: 0.19
      density: 0.75
  - model: We-Want-GPU/SOLAR-10.7B-orca-alpaca-gpt4-math
    parameters:
      weight: 0.18
      density: 0.75
  - model: maywell/Synatra-10.7B-v0.4
    parameters:
      weight: 0.18
      density: 0.7
  - model: kyujinpy/SOLAR-Platypus-10.7B-v2
    parameters:
      weight: 0.17
      density: 0.7
  - model: Sao10K/Frostwind-10.7B-v1
    parameters:
      weight: 0.16
      density: 0.65
  - model: rishiraj/meow
    parameters:
      weight: 0.15
      density: 0.6
```

## Merge command

```
python3 hf_merge.py mergelist.yaml solar-1
```

### Notes

* in the yaml: `p=weight` and `lambda=1/density`
