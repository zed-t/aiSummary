# Summarize PDFs Using GPT3
#### Original by Zed Tarar
#### Improved by Kai Turanski

### Python code to help you skim through PDFs
Obviously there are limitations here, for example, paragraphs that bleed from one page to another. This version has eliminated previous bugs by dividing the PDF into chunks readable by GPT3 and by making the script work anywhere on your computer. 

### Install
1. Use the python file and make sure you have the right libraries installed. sys, math, and os should be local to your computer. Here are links for the [openai](https://github.com/openai/openai-python) and [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/user/installation.html) libraries.
2. You'll need to get your API key from OpenAI (ask chat GPT how to do that), then copy it into the script where indicated 
3. The output is both printed on the command line and saved to ```summary of <your document name>.txt```

### Ease of access
This guide will show you how to set up a custom command to use this program anywhere on your computer via command line

1. Open the command line
2. Enter ```cd ~``` and then ```ls -a```
3. Open you bash config file (.zshrc on Mac and .bashrc on Linux) with ```open -e <file name>```
4. Put your absolute path to the python file as shown and then copy this line to the end of your bash config file ```alias summarize="python3 <absolute path to file>/pdfExtract3.py $1"``` 
5. You're done! Now go to the directory of the file you want to summarize and run ```summarize "name of the file you want to summarize"```

### Contribute
There are probably more elegant ways to create summaries from long PDFs, so if you have them, please share! 

---
###### [Original author LinkedIn](http://linkedin.com/in/zed-tarar/) 
###### [Improvement author LinkedIn](https://www.linkedin.com/in/kaituranski/)
