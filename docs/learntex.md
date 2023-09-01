# Getting Started with LaTeX

### Step 1: Creating Your First LaTeX Document
Start by creating a simple LaTeX document to get a feel for the system. 

1. Go to a directory where you want to create your LaTeX document.
2. Create a file named `hello-yaya.tex` and add the following content:

```
\documentclass{article}

\begin{document}

Hello, Yaya!

\end{document}
```

![LaTeX Developer](hello/Hello%20Yaya/hello-yaya.png)

This basic document sets up a LaTeX file with a standard article class and prints "Hello, Yaya!".


### Step 2: See What You Created
For an easy way to work with LaTeX, consider using an **online LaTeX editor** like ***Overleaf***.

1. Access OverLeaf Platform following this URL
2. Create an account on Overleaf if you don't have one.
3. Zip your Hello Yaya folder. 

![Zipping Process](hello/Hello%20Yaya/zip-yaya.png)

4. Create a new project and import the zipped `hello-yaya.tex` file you created in that folder.

![Import Zipped](hello/Hello%20Yaya/yaya-zipped.png)

5. Compile the document and observe the output. 

![PoC Hello Yaya](hello/Hello%20Yaya/hello-yaya-preview.png)

Easy right!
Overleaf provides a real-time preview of your LaTeX document.<br>
Let's keep going King or Queen!

And yeah, you can find Hello Yaya just [here](hello/Hello%20Yaya.zip).


## Go Harder on LaTeX
To make the process crystal clear, I've structured this for your convenience.

```
project/
├── assets/
│   ├── architectures/
│   │   ├── logical-diagram.png
│   │   ├── conceptual-diagram.png
│   │   └── sentinel-to-.png
│   ├── screenshots/
│   │   └── prove-of-my-work.jpg
├── main.tex
├── pages/
│   ├── TitlePage.pdf
│   ├── one.tex
│   ├── two.tex
│   ├── three.tex
│   ├── four.tex
│   ├── five.tex
└   └── six.tex
```

Nothing that serious we just  created a `main.tex` file where we can call all your other **Hello Yaya** files but you can call them something more meaningful to you.


Arrange them in the order you want them to be viewed.
```
\begin{document}

% Title Page
\input{pages/A-Title-Page}

% Other Sections
\input{pages/one}
\input{pages/two}
\input{pages/three}
% ...

\end{document}
```

You're likely getting the hang of it by now. This structure helps you keep your project organized and makes it easier to manage your large report.



## A Well-Structured LaTeX Project
An advanced and efficient LaTeX project structure should look something like this.


1. On Your LaTeX Editor Create the following structure- You can also create it locally and then import all.
```
./
├── assets/
│   ├── A-Title-Page/
│   │   └── A-Title-Page.pdf
│   ├── B-Tribute/
│   ├── C-Acknowledge/
│   ├── D-Synopsis/
│   ├── E-Acronyms/
│   ├── F-Introduction/
│   ├── G-your-path/
│   ├── H-more insights
│   ├── I-architect/
│   ├── J-Implement/
│   ├── K-Conclude/
│   ├── L-Appendix-A/
│   ├── L-Appendix-B/
│   └── M-Notes/
├── story/
│   ├── A-Title-Page.tex
│   ├── B-Tribute.tex
│   ├── C-Acknowledge.tex
│   ├── D-Synopsis.tex
│   ├── E-Acronyms.tex
│   ├── F-Introduction.tex
│   ├── G-your-path.tex
│   ├── H-more insights.tex
│   ├── I-architect.tex
│   ├── J-Implement.tex
│   ├── K-Conclude.tex
│   ├── L-Appendix-A.tex
│   ├── L-Appendix-B.tex
│   └── M-Notes.tex
├── main.tex
└── README.md---why-me
```

2. Incorporate this structure into your main.tex file to organize your document's sections.
3. Including Subdocuments
4. Store images, diagrams, and other assets in the assets directory for easy access and inclusion in your LaTeX document.


### Progressing with Your Project

Now that you have established a well-structured LaTeX project, it's time to infuse it with substantial content. To maintain clarity and a smooth document flow, refer back to the content generation prompts provided earlier, and diligently work on populating each section. 

Enjoy the power and flexibility of LaTeX for typesetting and document creation!
