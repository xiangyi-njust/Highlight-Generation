### The code for this paper: Academic paper Highlight Generation Using Prompt-based Learning

#### Project Structure

<pre>
Highlight-Generation
├─ code
│    ├─ ChatGPT                                Generate using chatgpt model
│    │    ├─ evaluation.ipynb                  evaluate the model performance
│    │    ├─ statistic.ipynb                   calculate the basic information of dataset and calculate the demonstration
│    │    ├─ generate.ipynb					   generate the highlight for the provided' abstract, include zero-shot、few-shot setting
│    │    ├─ new_prompt                        the result files of model generation in the new_prompt(check out our paper) situation
│    │    ├─ raw_prompt                        the result files of model generation in the raw_prompt(check out our paper) situation
│    │    ├─ opendata_result				   the result files of model generation in the few-shot setting
│    ├─ Decoder-only.ipynb                     Generate using decoder-only model like gpt2
│    └─ Encoder-Decoder.ipynb				   Generate using encoder-decoder model T5、BARD、FlanT5
├─ data
│    ├─ AIPubSum                               highlight dataset that contains the paper from artificial intelligence field
│    │    ├─ AIPubSum_test.xlsx
│    │    ├─ AIPubSum_test_aug.xlsx
│    │    └─ AIPubSum_train.xlsx
│    ├─ BioPubSum_test_filter	               highlight dataset that contains the paper from biological field
│    │    ├─ BioPubSum_test.xlsx
│    │    ├─ BioPubSum_test_filter.xlsx
│    │    └─ BioPubSum_train.xlsx
│    └─ CsPubSum_train						   highlight dataset that contains the paper from computer science field
│           ├─ CsPubSum_test.xlsx
│           └─ CsPubSum_train.xlsx
└─ readme.MD
</pre>



## Citation
Please cite the following paper if you use these codes and datasets in your work.

> Yi Xiang, Chengzhi Zhang. Academic paper Highlight Generation Using Prompt-based Learning. ***Aslib Journal of Information Management***, 2023. [[doi]()] [[Dataset & Source Code]](https://github.com/xiangyi-njust/Highlight-Generation)
