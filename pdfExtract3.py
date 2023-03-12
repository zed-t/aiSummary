import os.path
import sys
import math
import openai
from PyPDF2 import PdfReader

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path


# Divide option and arguement inputs into two arrays
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Get name of PDF from args
if len(args) > 0:
    pdfName = str(args[0])
else:
    sys.exit("No filename passed for summary");

# Create an instance of the GPT-3 model
openai.api_key = "!!!put your GPT-3 key here!!!"

# open the PDF file
pdfFile = open(pdfName, 'rb')

# create PDFFileReader object to read the file
pdfReader = PdfReader(pdfFile)
meta = pdfReader.metadata;

print("Printing the document info:")
if(meta is not None):
    print("\nAuthor: " + str(meta.author)
        +"\nTitle: " + str(meta.title))
print("- - - - - - - - - - - - - - - - - - - -")
print("Number of Pages: " + str(len(pdfReader.pages)))

numOfPages = len(pdfReader.pages)
rawText = ""
pageEndIndices = []

for i in range(0, numOfPages):
    nextText = pdfReader.pages[i].extract_text()
    rawText = rawText + nextText
    pageEndIndices.append(len(rawText))

acceptableLengthGPT = 3297
summaryPath = uniquify("summary of "+os.path.basename(pdfName).split(".")[0]+".txt")

for i in range(0, math.floor(len(rawText)/acceptableLengthGPT)):
    # Divide the text into lengths accepted by GPT3 (<3297 chars)
    if((i+1)*acceptableLengthGPT<len(rawText)):
        targetText = rawText[i*acceptableLengthGPT:(i+1)*acceptableLengthGPT]
    else:
        targetText = rawText[i*acceptableLengthGPT:len(rawText)]

    page = 0
    for j in range(0, numOfPages):
        if(pageEndIndices[j]<(i+1)*acceptableLengthGPT):
            page = j
        else:
            break

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Write a summary for this in the style of the New Yorker: " + targetText,
    max_tokens=800,
    n=1,
    temperature=0.5,
)
    # Print the generated summary
    print("\n\nPage "+str(page+1)+":\n"+response["choices"][0]["text"])

    # Open a text file for writing
    with open(summaryPath, 'a') as f:
        # Write the list of bullet point summaries to the file
        f.writelines("\n\nPage "+str(page+1)+":\n"+response["choices"][0]["text"])

# close the PDF file object
pdfFile.close()

