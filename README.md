# Summarize PDFs Using GPT3
##### Original by Zed Tarar
##### Improved by Kai Turanski

### Python code to help you skim through PDFs
This program allows you to select a PDF, divides it into chunks readable by GPT3, and creates a summary of it next to the original PDF. 

### Current limitations
- GPT3 may have a hard time interpreting paragraphs that bleed from one chunk to another
- Text output can sometimes contain badly formatted text, which can usually be deleted easily with no harm to comprehension

### Editing 
1. To edit the python file, make sure you have the right libraries installed. ```sys```, ```math```, and ```os``` should be local to your computer. Here are links for the [```openai```](https://github.com/openai/openai-python), [```PyPDF2```](https://pypdf2.readthedocs.io/en/3.0.0/user/installation.html), and [```tkinter```](https://www.tutorialspoint.com/how-to-install-tkinter-in-python) libraries.
2. You'll need to get your API key from OpenAI (ask chat GPT how to do that), then copy it into the script where indicated 
3. The output is both printed on the command line and saved to ```summary of <your document name>.txt```

### Usage

1. Navigate to your ```./dist/<your operating system>_version_pdf_extract/<your operating system>_version_pdf_extract.<extension>``` file
2. Double click to run the file and you're done!

### Contribute
There are probably more elegant ways to create summaries from long PDFs, so if you have them, please share! 

---
###### [Original author LinkedIn](http://linkedin.com/in/zed-tarar/) 
###### [Improvement author LinkedIn](https://www.linkedin.com/in/kaituranski/)
