# LDA

Here Reuters-21578 is used as input data.

Reuters-21578 has 10788 documents on the whole. They are basically text documents, that are articles including collection of 90 categories.

Before applying LDA, the documents are first stored in lists and then below steps are carried out for all the documents.
    1. Converted all the letters to lower case.
    2. Tokenize the words.
    3. Removed stopping words (like and, the, a, an, etc.).
    4. Performed stemming (Example: convert playing, played, plays etc., to play)

The output of LDA will it contains 12 topics and top three words in each topic will be displayed.
