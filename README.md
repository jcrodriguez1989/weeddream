
# WeedDream - A cannabis-trained [DeepDream](https://en.wikipedia.org/wiki/DeepDream) approach

<!-- TODO: Add post link. -->

Code to reproduce the findings presented at the *“Can Artificial
Intelligence Dream of Cannabis?”* blog post.

## Usage

### Training the Weedception\_v1 Model

To retrain inception, file `01_retrain_inception.py` should be executed,
for this, run the following from a bash console:

``` bash
weeddream$ mkdir Models # Create the folder to save the trained model.
weeddream$ python Script/01_retrain_inception.py 
```

### Analyze Individual Layer Effects

To create dreams using only one layer and one weight run the following:

``` bash
# Let's say we want to train layer 10 with weight 3, we should type:
weeddream$ python Script/02_analyze_individual_layers.py 10 3
```

### Using WeedDream to Dream With the Selected Setting

To use WeedDream to dream on a image, with the selected settings (layers
2 with weight `2`, 6 with `5`, and 9 with `4`), run the following:

``` bash
weeddream$ python Script/03_weeddream.py
```
