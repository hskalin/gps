

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

<a id="org58c85cf"></a>

# RetinaNet


<a id="org883b47f"></a>

## About

-   [Article](https://towardsdatascience.com/review-retinanet-focal-loss-object-detection-38fba6afabe4)

-   It is a one-stage detector

-   It is discovered that there is extreme **foreground-background class imbalance** problem in one-stage detector. And it is believed that this is the central cause which makes the performance of **one-stage detectors** inferior to two-stage detectors.

-   It uses **focal loss** i.e. lower loss is contributed by “easy” negative samples so that the loss is focusing on “hard” samples, which improves the prediction accuracy.
    
    $$FL\left(p_{t}\right)\ =\ -\left(1-p_{t}\right)^{\gamma}\log\left(p_{t}\right)$$

-   The loss function is reshaped to down-weight easy examples and thus focus training on hard negatives. A modulating factor (1-p<sub>t</sub>)<sup>&gamma;</sup> is added to the cross entropy loss where &gamma; is tested from [0,5] in the experiment


<a id="orgb98a251"></a>

# Diagram Parser Pipeline

-   Each symbol in Geometry3k has been annotated
-   `xml_to_csv.py` generates a csv file from the xml files corresponding to the annotated diagrams
    
    eg, the diagram : 
    
    ![img](https://github.com/hskalin/gps/blob/main/doc/images/2738.png)
    
    
    and the xml:
    
    ```xml
    <annotation>
      <folder>geometry_annotation</folder>
      <filename>2738.png</filename>
      <source>
        <database>Unknown</database>
      </source>
      <size>
        <width>311</width>
        <height>216</height>
        <depth>3</depth>
      </size>
      <segmented>0</segmented>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>124</xmin>
          <ymin>73</ymin>
          <xmax>155</xmax>
          <ymax>100</ymax>
        </bndbox>
      </object>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>15</xmin>
          <ymin>170</ymin>
          <xmax>39</xmax>
          <ymax>200</ymax>
        </bndbox>
      </object>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>136</xmin>
          <ymin>175</ymin>
          <xmax>167</xmax>
          <ymax>204</ymax>
        </bndbox>
      </object>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>260</xmin>
          <ymin>169</ymin>
          <xmax>285</xmax>
          <ymax>200</ymax>
        </bndbox>
      </object>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>267</xmin>
          <ymin>99</ymin>
          <xmax>285</xmax>
          <ymax>126</ymax>
        </bndbox>
      </object>
      <object>
        <name>text</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>258</xmin>
          <ymin>9</ymin>
          <xmax>285</xmax>
          <ymax>41</ymax>
        </bndbox>
      </object>
      <object>
        <name>perpendicular</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
          <xmin>232</xmin>
          <ymin>142</ymin>
          <xmax>267</xmax>
          <ymax>175</ymax>
        </bndbox>
      </object>
    </annotation>
    ```
    
    gets converted to the following csv :
    
    ```csv
    ../../data/geometry3k/symbols/2738.png,124,73,155,100,text
    ../../data/geometry3k/symbols/2738.png,15,170,39,200,text
    ../../data/geometry3k/symbols/2738.png,136,175,167,204,text
    ../../data/geometry3k/symbols/2738.png,260,169,285,200,text
    ../../data/geometry3k/symbols/2738.png,267,99,285,126,text
    ../../data/geometry3k/symbols/2738.png,258,9,285,41,text
    ../../data/geometry3k/symbols/2738.png,232,142,267,175,perpendicular
    ```
