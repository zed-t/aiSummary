# Summarize PDFs Using GPT3
### A quick and dirty bit of Python code to help you skim through those pesky PDFs
1. GPT3's API has an upper limit on the amount of text you can send it to summarize at any given instance. 
2. This code sends one page at a a time to GPT3 and usually comes in under the cap (but if one page is too dense it will return an error).
3. Obviously there are limitations here, for example, paragraphs that bleed from one page to another. 

### Install
1. Use the python file and make sure you have the right libraries installed.
2. You'll need OpenAI's library and PyPDF2 (use the PIP install command for both, or you can ask chat.openai.com for step by step instructions).
3. You'll need to get your API key from OpenAI (again, ask chat GPT how to do that). 
4. You can change the file name reference in the code or rename your file to "target.pdf".
5. The output is both displayed on screen and printed to "summaries.txt" 

### Contribute
There are probably more elegant ways to create summaries from long PDFs, so if you have them, please share! 

---
###### [LinkedIn](http://linkedin.com/in/zed-tarar/)
