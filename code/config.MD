1. prompt

	fine-tuning 和 prompt learning中都需要用到prompt,这里需要统一实验中用到的prompt

	prompt list:

	* Summarize:[X][Y]

	* Summarize the highlight:[X][Y]

	* Summarize the mainly work:[X][Y]

	* Extract the highlight:[X][Y]

	* Extract the mainly work:[X][Y]

	* [X]. The highlights of this paper are: [Y]

	* [X]. The main work of this paper is: [Y]

	* [X]. The contributions of this paper are: [Y]

	* [X]. We can conclude the highlights as: [Y]

	* [X]. We can conclude the main work as: [Y]

	* [X]. We can conclude the contributions as: [Y]

2. max_length

	对于prompt过程来说，只需确定三个数据集下各自abstract的token总量，这里以能够涵盖90%的length作为max_length的取值

	对于fine-tuning过程来说，label的max_length取值过程也参照上面的方法


3. 生成过程中的参数设置 model.generate