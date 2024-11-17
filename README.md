## Leaf Damage Esitmation from Leaf frames photos

When studying herbovory a leaf frame is often used. But to process each and individual image in ImageJ is laborous, as it has to be done by hand. Thus this slows down the processing of the ecological data. From leaf frames we can obtain a set of interesting information. Not only the area lost to herbivory, but also weight of the sample SLA and LDMC, and LWC, and possibly many other traits. 

This project aims to build a regression deep learning model to quickly and accurately process leaf frame photos in batches, to speed up the processing pipeline of scientific reasearch.


### Data Preparation

In the original training data folder there are three types of data:
1. Original photos with leaves flattened on a 50 $\times$ 50 cm surface.
2. High contrast photo from ImageJ software
3.
4. Tabular data with each leaf's coordinates, area and estimated leaf loss due to herbivory.

### Stack

Git to follow the code
DagsHub to version the data (?)
MLFLOW to track experiments and models.