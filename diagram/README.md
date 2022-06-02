

# InterGPS

-   **Hough Transformation** - geometry primitives (points, lines, arcs, and circles) 
      
      Code used : <https://github.com/seominjoon/geosolver>

-   **RetinaNet** - diagram symbols and text regions ([paper](https://arxiv.org/abs/1708.02002), [code](https://github.com/yhenon/pytorch-retinanet))

-   **MathPix** - textual content


<a id="orgec69923"></a>

## Grounding

Primitive set $P$ and symbol set $S$, optimization problem with the constraint of geometry relations:

$$\operatorname*{min}\sum_{s}d i s t(s_{i},p_{j})\times\mathbbm{1}\{s_{i}{\mathrm{~assigns~to~}}p_{j}\}$$

s.t. $(s_{i},p_{j})$ &isin; Feasibility set $F$, where $F$ defines the geometric constraints for symbol grounding.


<a id="org8ed3406"></a>

## Imporvements

-   17% improvement in performance when used ground truth diagram formal language

-   MathpixOCR is NOT fee and it charges $0.004 to process one image. Alternatives
    -   <https://github.com/lukas-blecher/LaTeX-OCR>
    
    -   <https://tex.stackexchange.com/questions/116863/image-equation-to-tex>
    
    -   <https://www.cs.rit.edu/~rlaz/ffes/>
    
    -   <https://tex.stackexchange.com/questions/266989/ocr-pdf-image-to-latex-mat>


<a id="org820eae8"></a>

## Todo list <code>[25%]</code>

-   [X] Run the opensource [Latex-ocr](https://github.com/lukas-blecher/LaTeX-OCR) tool and determine feasibility

    `Result` : Problem in parsing some low res images

-   [ ] Replace MathPix with Latex-ocr in the InterGPS pipeline

-   [ ] Try using RetinaNet for segmenting question text and diagrams for parsing in order to build a generalised pipeline

-   [ ] Evaluate Latex-ocr results on geometry3k
