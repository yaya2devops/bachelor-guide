
<br>

# Getting Started with LaTeX

Hey! Welcome where I help you become more proficient with the LaTeX system. We'll start with a basic "Hello Yaya" document and progress towards a more advanced structure, to finaly demonstrate what a good project structure should be.

- [Step 1: Creating Your First LaTeX](#step-1-creating-your-first-latex-document)
- [Step 2: See What You Created](#step-2-see-what-you-created)
- [Step 3 : LaTeX Convert to PDF](#step-3--latex-convert-to-pdf)
- [Go Harder On LaTeX](#go-harder-on-latex)

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

* `\documentclass{article}`: Specifies that this is an "article" document type.
* `\begin{document}` and `\end{document}`: Delimit the document content.
* `\Hello, Yaya!`\: The actual content of the document, which in this case is a simple greeting to me.

![LaTeX Developer](hello/Hello%20Yaya/hello-yaya.png)

Easy! This basic document sets up a LaTeX file with a standard article class and prints `Hello, Yaya!`.


### Step 2: See What You Created
For an easy way to work with LaTeX, consider using an **online LaTeX editor** like ***Overleaf***.

1. Access OverLeaf Platform following this URL [https://www.overleaf.com/login?](https://www.overleaf.com/login?)
2. Create an account on Overleaf if you don't have one.
3. Zip your Hello Yaya folder. 

![Zipping Process](hello/Hello%20Yaya/zip-yaya.png)

<details>
<summary>
🤐 Zipping Face-To-Face!

</summary>

![Zipping Realtime](hello/Hello%20Yaya/yaya-zipped.png)

</details>

4. Create a new project in **Overleaf** and click Import Project

5. Pick the zipped `Hello Yaya.zip` Folder.

![Project->Import->Pick Zip](hello/Hello%20Yaya/import-from-local.png)

> There was internet and It was imported.

6. Watch the Compiler do it for you, observe the output.

As soon as you import the project, it will seamlessly direct you to the following page.

![PoC Hello Yaya](hello/Hello%20Yaya/hello-yaya-preview.png)

Easy right!
Overleaf provides a real-time preview of your LaTeX document.<br>
Let's keep going King or Queen!

And yeah, you can find Hello Yaya just [here](https://github.com/yaya2devops/bachelor-guide/blob/main/docs/hello/zip-hello-yaya.zip).

### Step 3 : LaTeX Convert to PDF

While having files is great, you also need a PDF version.

Once you've completed your project, simply click the icon depicted below to convert your compilation into a PDF.

![LaTeX To PDF](hello/Hello%20Yaya/pdf-me.png)

Great and cool! Although this is quite minimal, it should give you a good idea of what your workflow will be like with the system.

Immediately [view the PDF version](https://github.com/yaya2devops/bachelor-guide/blob/main/docs/hello/Hello%20Yaya/Hello_Yaya.pdf) of `Hello Yaya`!

# Go Harder on LaTeX
To make the process crystal clear, I've structured this for your convenience.

```
project/
├── assets/
│   ├── architectures/
│   │   ├── logical-diagram.png
│   │   ├── conceptual-diagram.png
│   │   └── physical-diagram.png
│   └── screenshots/
│       ├── prove-of-my-work.jpg
│       └── my-thing.jpg
├── main.tex
├── pages/
│   ├── TitlePage.pdf
│   ├── one.tex
│   ├── two.tex
│   ├── three.tex
│   ├── four.tex
│   ├── five.tex
└───└── six.tex
```

Nothing that serious we just  created a `main.tex` file where we can call all your other **Hello Yaya** files but you can call them something more meaningful to you like one, two, .. **or?** Keep reading.

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
The time comes to expose the secret for you. An advanced and efficient **LaTeX project structure** should look something like this.

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
│   ├── H-more-insights
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
│   ├── H-more-insights.tex
│   ├── I-architect.tex
│   ├── J-Implement.tex
│   ├── K-Conclude.tex
│   ├── L-Appendix-A.tex
│   ├── L-Appendix-B.tex
│   └── M-Notes.tex
├── main.tex
└── README.md---why-me
```

### Action Required
1. On Your LaTeX Editor Create the following structure. You can also create it locally and then import all.
2. Incorporate this structure into your main.tex file to organize your document's sections.
3. Including Subdocuments
4. Store images, diagrams, and other assets in the assets directory for easy access and inclusion in your LaTeX document.

#### Just [hand me a Template](https://drive.google.com/drive/folders/1OLvX6kEaIFk-8JgGyrW1E_Wl-5sx_zhP?usp=sharing)

The attached document serves as a starting point made by our university ISTIC and provided to its students, You. 

Please ensure adherence to the title page format while incorporating your own content. 

### Progressing with Your Project

Now that you have established a well-structured LaTeX project, it's time to infuse it with substantial content. To maintain clarity and a smooth document flow, refer back to the content generation prompts provided earlier, and diligently work on populating each section. 

### [The Prompt You Need](prompt-poc.md)

Enjoy the power and flexibility of LaTeX for typesetting and document creation!
