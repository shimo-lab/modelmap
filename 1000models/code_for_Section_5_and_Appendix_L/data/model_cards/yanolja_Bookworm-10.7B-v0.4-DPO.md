# Bookworm-10.7B-v0.4-DPO

## Join Our Community on Discord!

If you're passionate about the field of Large Language Models and wish to exchange knowledge and insights, we warmly invite you to join our Discord server. It's worth noting that Korean is the primary language used in this server. The landscape of LLM is evolving rapidly, and without active sharing, our collective knowledge risks becoming outdated swiftly. Let's collaborate and drive greater impact together! Join us here: [Discord Link](https://discord.gg/b27bAHg95m).

## Our Dedicated Team (Alphabetical Order)
| Research        | Engineering     | Product Management | UX Design   |
|-----------------|-----------------|--------------------|--------------
| Myeongho Jeong  | Geon Kim        | Bokyung Huh        | Eunsue Choi |
| Seungduk Kim    | Rifqi Alfi      |                    |             |
| Seungtaek Choi  | Sanghoon Han    |                    |             |
|                 | Suhyun Kang     |                    |             |

## About the Model

This model is a fine-tuned version of [yanolja/KoSOLAR-10.7B-v0.2](https://huggingface.co/yanolja/KoSOLAR-10.7B-v0.2), which is a Korean vocabulary-extended version of [upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0). Specifically, we employed Direct Preference Optimization (DPO) based on [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). 

### Training Data
  - Korean-translated version of [Open-Orca/SlimOrca-Dedup](https://huggingface.co/datasets/Open-Orca/SlimOrca-Dedup)
  - Korean-translated version of [argilla/ultrafeedback-binarized-preferences-cleaned](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned)
  - No other dataset was used

## Citation

```
@misc{cui2023ultrafeedback,
      title={UltraFeedback: Boosting Language Models with High-quality Feedback}, 
      author={Ganqu Cui and Lifan Yuan and Ning Ding and Guanming Yao and Wei Zhu and Yuan Ni and Guotong Xie and Zhiyuan Liu and Maosong Sun},
      year={2023},
      eprint={2310.01377},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```
@misc{SlimOrcaDedup,
  title = {SlimOrca Dedup: A Deduplicated Subset of SlimOrca},
  author = {Wing Lian and Guan Wang and Bleys Goodson and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium" and Nathan Hoos},
  year = {2023},
  publisher = {HuggingFace},
  url = {https://huggingface.co/datasets/Open-Orca/SlimOrca-Dedup/}
}
```
```
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```