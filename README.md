
# WeedDream - A cannabis-trained [DeepDream](https://en.wikipedia.org/wiki/DeepDream) approach

Code to reproduce the findings presented at the [_"Can Artificial Intelligence Dream of Cannabis?"_ blog post](https://medium.com/cannabis-explorations/can-artificial-intelligence-dream-of-cannabis-3ed9b34948bf).

## Usage

### Adding Images for Training

The images used to train Weedception\_v1 are not my property, and
therefore I cannot share them. To retrain the model you must provide
your own images. To do this, in the `TrainingImages/` folder there
should be a sub-folder for each category to be used, and within each
sub-folder its corresponding images. As an example, in each
`TrainingImages/` sub-folder, there is included one example image.

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

# If we want to train each individual layer for each weight from 1 to 10, we should type:
weeddream$ for layer in {1..10}; do
>     for weight in {1..10}; do
>         python Script/02_analyze_individual_layers.py $layer $weight
>     done
> done
```

### Using WeedDream to Dream With the Selected Setting

To use WeedDream to dream on a image, with the selected settings (layers
2 with weight `2`, 6 with `5`, and 9 with `4`), run the following:

``` bash
weeddream$ python Script/03_weeddream.py
```
