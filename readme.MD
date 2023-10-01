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

## Directory structure
<pre>
Highlight-Generation
├─ code
│    ├─ ChatGPT                                Generate using chatgpt model
│    │    ├─ evaluation.ipynb                  Evaluate the model performance
│    │    ├─ statistic.ipynb                   Calculates the basic information of the dataset and calculates the demonstration
│    │    ├─ generate.ipynb                    Generates the highlight for the provided' abstract, including zero-shot,few-shot setting
│    │    ├─ new_prompt                        Result files of model generation in the new_prompt(check out our paper) situation
│    │    ├─ raw_prompt                        Result files of model generation in the raw_prompt(check out our paper) situation
│    │    ├─ opendata_result                   Result files of model generation in the few-shot setting
│    ├─ Decoder-only.ipynb                     Generate using a decoder-only model like gpt2
│    └─ Encoder-Decoder.ipynb                  Generate using encoder-decoder model T5、BARD、FlanT5
├─ data
│    ├─ AIPubSum                               Highlights dataset that contains the paper from the artificial intelligence field
│    │    ├─ AIPubSum_test.xlsx
│    │    ├─ AIPubSum_test_aug.xlsx
│    │    └─ AIPubSum_train.xlsx
│    ├─ BioPubSum                              Highlights dataset that contains the paper from the biological field
│    │    ├─ BioPubSum_test.xlsx
│    │    ├─ BioPubSum_test_filter.xlsx
│    │    └─ BioPubSum_train.xlsx
│    └─ CsPubSum                               Highlights dataset that contains the paper from the computer science field
│           ├─ CsPubSum_test.xlsx
│           └─ CsPubSum_train.xlsx
└─ ReadME.md
</pre>

### Dataset Discription
On the one hand, the three data sets used in the experiment are in different fields of selected papers, and on the other hand, the size of the data sets is also quite different.
The original data set is used for supervised learning training. Since in this study we only consider the situation without parameter updates, we do not care about the size of the training set, so only the number of test samples for each data set is described here:
 * CsPubSum_test: 150
 * AIPubSum_test: 65
 * BioPubSum_test: 2685

You can get the papers'(corresponding above three datasets) link of Elsevier in these two repositories: 
 * https://github.com/EdCo95/scientific-paper-summarisation (CSPubSum)
 * https://github.com/MorenoLaQuatra/domain-specific-academic-dataset (AIPubSum, BioPubSum)

In this paper, we provide the content of the paper that contains the highlight and abstract, we get this information by crawling the Elsevier website based on the above links

### Quick Start
We provide our code in the format of the Jupyter Notebook, so you can follow cells to run our experiment step by step
 * In order to run the chatgpt for inference, you need to obtain your API key from the OpenAI website, and then replace it in the notebook
 * In order to run models like gpt2, T5, and so on, you may need the GPU to accelerate your process of inference

## Citation
Please cite the following paper if you use these codes and datasets in your work.

> Yi Xiang, Chengzhi Zhang\*. Enhancing Highlight Generation from Academic Articles Using Prompt-based Learning. ***Scientometrics***, 2023.（under review) [[doi]()] [[Dataset & Source Code]](https://github.com/xiangyi-njust/Highlight-Generation)
