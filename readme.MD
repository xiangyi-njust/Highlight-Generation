# Enhancing Highlight Generation from Academic Articles Using Prompt-based Learning

## Overview
This repository contains code and data for the paper: Enhancing Highlight Generation from Academic Articles Using Prompt-based Learning

The aim of this paper is to improve the highlight generation performance using prompt-based learning in a low scenario, we used three open datasets as benchmark, and explored below pretrained language model inference performance that just provided the prompts and without parameters update: 
* **decoder-only**: gpt2
* **encoder-decoder**: T5, FlanT5, BARD
* **large language model**: ChatGPT (gpt3.5-turbo-0613)

Specifically, we explored below questions in this paper:

  * Can prompt-based learning improve the performance of pre-trained language models on downstream tasks?

  *  How do factors such as prompt content, demonstration, etc. affect the performance of pretrained language models in prompt-based learning?

  *  Can prompt-based learning achieve performance comparable to current supervised learning methods?

To address the three mentioned issues, we have taken the following experiments: 

   * Firstly, manually formulated prompts and compared the changes in the generation performance of pretrained language models before and after adding prompts

   * Secondly, optimized the prompt design for the best-performing model
     
   * Lastly, compare the model performance with optimized designed prompts and state-of-the-art in the few-shot settings

Overall, We applied the prompt-based learning approach to the task of highlight generation, surpassing the performance of previous supervised learning methods while reducing the demand for training data.

## Project Structure
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

You can get the papers'(corresponding above three datasets) link of Elsevier in these two repositories: 
 * https://github.com/EdCo95/scientific-paper-summarisation (CSPubSum)
 * https://github.com/MorenoLaQuatra/domain-specific-academic-dataset (AIPubSum, BioPubSum)

In this paper, we provide the content of the paper that contains the highlight and abstract, we get this information by crawling the Elsevier website based on the above links

We provide our code in the format of the Jupyter Notebook, so you can follow cells to run our experiment step by step
 * In order to run the chatgpt for inference, you need to obtain your API key from the OpenAI website, and then replace it in the notebook
 * In order to run models like gpt2, T5, and so on, you may need the GPU to accelerate your process of inference

## Citation
Please cite the following paper if you use these codes and datasets in your work.

> Yi Xiang, Chengzhi Zhang. Enhancing Highlight Generation from Academic Articles Using Prompt-based Learning. ***Scientometrics***, 2023. [[doi]()] [[Dataset & Source Code]](https://github.com/xiangyi-njust/Highlight-Generation)
