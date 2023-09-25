# Academic paper Highlight Generation Using Prompt-based Learning

## Overview
<b> Code and Data for the paper: Academic paper Highlight Generation Using Prompt-based Learning

The aim of this paper is to improve the highlight generation performance in a low scenario, we used three open datasets as benchmark, and explored below pretrained language model inference performance in the zero-shot setting:
* **decoder-only**: gpt2
* **encoder-decoder**: T5, FlanT5, BARD
* **large language model**: ChatGPT (gpt3.5-turbo-0613)

### Project Structure
<pre>
Highlight-Generation
├─ code
│    ├─ ChatGPT                                Generate using chatgpt model
│    │    ├─ evaluation.ipynb                  evaluate the model performance
│    │    ├─ statistic.ipynb                   calculates the basic information of the dataset and calculates the demonstration
│    │    ├─ generate.ipynb                    generates the highlight for the provided' abstract, including zero-shot,few-shot setting
│    │    ├─ new_prompt                        the result files of model generation in the new_prompt(check out our paper) situation
│    │    ├─ raw_prompt                        the result files of model generation in the raw_prompt(check out our paper) situation
│    │    ├─ opendata_result                   the result files of model generation in the few-shot setting
│    ├─ Decoder-only.ipynb                     Generate using a decoder-only model like gpt2
│    └─ Encoder-Decoder.ipynb                  Generate using encoder-decoder model T5、BARD、FlanT5
├─ data
│    ├─ AIPubSum                               highlights dataset that contains the paper from the artificial intelligence field
│    │    ├─ AIPubSum_test.xlsx
│    │    ├─ AIPubSum_test_aug.xlsx
│    │    └─ AIPubSum_train.xlsx
│    ├─ BioPubSum                              highlights dataset that contains the paper from the biological field
│    │    ├─ BioPubSum_test.xlsx
│    │    ├─ BioPubSum_test_filter.xlsx
│    │    └─ BioPubSum_train.xlsx
│    └─ CsPubSum                               highlights dataset that contains the paper from the computer science field
│           ├─ CsPubSum_test.xlsx
│           └─ CsPubSum_train.xlsx
└─ ReadME.md
</pre>

## Citation
Please cite the following paper if you use these codes and datasets in your work.

> Yi Xiang, Chengzhi Zhang. Academic paper Highlight Generation Using Prompt-based Learning. ***Aslib Journal of Information Management***, 2023. [[doi]()] [[Dataset & Source Code]](https://github.com/xiangyi-njust/Highlight-Generation)
