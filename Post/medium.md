Can Artificial Intelligence Dream of Cannabis?
================
Juan Cruz Rodriguez
1/6/2021

*Remember DeepDream? Yes, the Deep Neural Network (NN) that transformed
pictures by adding psychedelic “dream” effects. If not, take a look at
[Wikipedia’s article](https://en.wikipedia.org/wiki/DeepDream).*

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Aurelia-aurita-3-0049.jpg/320px-Aurelia-aurita-3-0049.jpg" style="display: block; margin: auto;" />

## Non-technical DeepDream’s TL;DR

*For a slightly more technical explanation, I recommend the [Keras
blog](https://keras.io/examples/generative/deep_dream/).*

DeepDream uses a deep convolutional network, named
[“Inception”](https://paperswithcode.com/method/inception-v3), which was
trained with the aim of automatically classifying images. DeepDream
author [Alexander Mordvintsev](https://znah.net/) wanted to know what
calculations/transformations the model was performing on the input image
when trying to classify it.

Inception’s NN architecture contains ten independent *concatenate*
layers (“Concat”; red boxes in the following figure). By editing the
weights of different layers, after giving an input image, we could
visually check the transformation effect of each layer. To Alexander’s
surprise, the results were astonishing, finding artistic psychedelic
alterations in the images.

<div class="figure" style="text-align: center">

<img src="https://paperswithcode.com/media/methods/inceptionv3onc--oview_vjAbOfw.png" alt="The architecture of the Inception neural network."  />
<p class="caption">
The architecture of the Inception neural network.
</p>

</div>

Inception was trained with a large number of images, however, animal
images were predominant. And that is why in the dreams generated by
DeepDream, it is common for effects related to animals to appear. This
is where my interest arises to think “what will happen if we retrain
Inception’s architecture with images of cannabis?” 🤯.

## Retraining the Architecture

For this project, the NN architecture of Inception was retrained so that
it classifies cannabis images within four sub-categories. A total of
2822 images were used, tagged as “flower” 💐 (2243 images), “plant” 🌱
(90), “pre-roll” 🚬 (257), and “seeds” 🌰 (232), as exemplified by the
following images respectively:

![Example images for category “flower” and
“plant”.](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Orange_Cookies.png/320px-Orange_Cookies.png)![Example
images for category “flower” and
“plant”.](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Marijuana_plant.jpg/180px-Marijuana_plant.jpg)

![Example images for category “pre-roll” and
“seeds”.](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Marijuana_pre-roll.jpg/320px-Marijuana_pre-roll.jpg)![Example
images for category “pre-roll” and
“seeds”.](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Hempseed.jpg/320px-Hempseed.jpg)

## Analyzing Each Layer Individually

Once the model, called “WeedCeption\_v1” was trained, a procedure
similar to that developed in DeepDream was followed. In this first
stage, to analyze the contributions of each *concatenate* layer, on each
iteration only one weight (from 1 to 10) for one layer was taken into
account. Starting from the original image, the images generated
automatically by the model were obtained after using each layer and
weight. Next, for each layer, the image generated by one of the
evaluated weights (representative weight was chosen by me) is shown.

This is the original input image given to the WeedCeption\_v1 trained
model:

<img src="../original_img.jpg" width="1500" style="display: block; margin: auto;" />

Analyzing the effects of layer 1, there are no clear patterns related to
the 4 categories used for training. With some creativity, some
flower-like textures can be appreciated.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed1_7.0.png" alt="WeedCeption_v1 _concatenate_ layer 1 (weight=7) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 1 (weight=7) effects.
</p>

</div>

Now, in layers 2 and 3, more marked patterns begin to be noticed. Flower
textures are more recognizable, as well as seed-like figures begin to
appear. Also, some elongated figures appear, which could have some
relation to pre-rolls.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed2_10.0.png" alt="WeedCeption_v1 _concatenate_ layer 2 (weight=10) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 2 (weight=10) effects.
</p>

</div>

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed3_7.0.png" alt="WeedCeption_v1 _concatenate_ layer 3 (weight=7) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 3 (weight=7) effects.
</p>

</div>

Layer 4 does not present easily recognizable patterns, it could be
interpreted that figures related to pre-rolls or plants influence this
layer.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed4_10.0.png" alt="WeedCeption_v1 _concatenate_ layer 4 (weight=10) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 4 (weight=10) effects.
</p>

</div>

In layer 5, again no noticeable patterns are observed, although a few
seed-related figures can be seen mainly in the upper part of the red
heart.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed5_2.0.png" alt="WeedCeption_v1 _concatenate_ layer 5 (weight=2) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 5 (weight=2) effects.
</p>

</div>

Layer 6 presents well-marked patterns of flower textures, especially
when looking at the image of the red heart.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed6_3.0.png" alt="WeedCeption_v1 _concatenate_ layer 6 (weight=3) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 6 (weight=3) effects.
</p>

</div>

In layers 7 and 8, no easily recognizable patterns can be seen. Although
some quite interesting psychedelic effects are created.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed7_3.0.png" alt="WeedCeption_v1 _concatenate_ layer 7 (weight=3) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 7 (weight=3) effects.
</p>

</div>

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed8_7.0.png" alt="WeedCeption_v1 _concatenate_ layer 8 (weight=7) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 8 (weight=7) effects.
</p>

</div>

Finally, in layers 9 and 10, some beautiful flower textures are present.

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed9_3.0.png" alt="WeedCeption_v1 _concatenate_ layer 9 (weight=3) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 9 (weight=3) effects.
</p>

</div>

<div class="figure" style="text-align: center">

<img src="../LayersImgs/mixed10_3.0.png" alt="WeedCeption_v1 _concatenate_ layer 10 (weight=3) effects." width="1500" />
<p class="caption">
WeedCeption\_v1 *concatenate* layer 10 (weight=3) effects.
</p>

</div>

<!-- # 1   maybe flower -->
<!-- # 2   seed / flower -->
<!-- # 3   seed / flower / preroll shapes -->
<!-- # 4   preroll shapes / plant shapes -->
<!-- # 5   maybe seed -->
<!-- # 6   super flower -->
<!-- # 7   psyco -->
<!-- # 8   psyco -->
<!-- # 9   nice flower -->
<!-- # 10  nice flower -->

These are my personal appreciations of what I get from the effects of
each layer. But do you see anything else about the layers that I have
not seen? Please comment below!

## Using Selected Layers for Final Result

Having analyzed the individual effects of each layer, I selected the
layers with which I would like to analyze interactions. The selected
layers were layer 2 (seed/flower-like effects), 6 (super flower
effects), and 9 (nice flower effects). For this combination of layers,
analyzing random selections of weights, new transformations of the
original image were obtained. Next, I present what I consider the most
beautiful output image obtained. This image was obtained with weights
`2`, `5`, and `4`, for layers 2, 6, and 9 respectively:

<div class="figure" style="text-align: center">

<img src="../NiceDreams/mixed2_2.0_mixed6_5.0_mixed9_4.0.png" alt="Final WeedDream obtained image." width="1500" />
<p class="caption">
Final WeedDream obtained image.
</p>

</div>

We can observe the beautiful cannabis-related effects that WeedDream
automatically adds to the original image. Easily differentiable flower
textures can be observed, as well as some seeds tend to appear.

Tell me, would you like to get your picture WeedDreamed? Comment on this
post, and I will try to get the job done 🦾!

## Conclusions

The database with which WeedCeption\_v1 was trained was small and
unbalanced. However, it was shown that when using the model to generate
dreams, effects related to the training categories begin to appear. It
can be concluded that it is completely possible to generate a
“WeedDream” model.

## Next Steps

As previously mentioned, DeepDream tends to add animal figures, since it
was trained with an unbalanced amount of images for animals. In
WeedDream something similar happens, since the number of flower images
is times greater than the rest, “flowers” is the most distinguishable
effect obtained. Retraining the model with a larger number of images,
towards obtaining WeedCeption\_v2, would definitely result in a more
interesting analysis. Maybe Weedmaps or Leafly can help by allowing me
to use their gigantic image database 😅🙏. I am optimistic that analyzing
more images, as well as more categories, would result in amazing new
effects.

## Reproducibility

All the work presented in this post can be easily replicated. The full
code is available on
[GitHub](https://github.com/jcrodriguez1989/weeddream/). However, the
images used for training are not mine, so I cannot include them in the
repository.

## Acknowledgments

I thank [Nicolas Peretti](https://github.com/nicoperetti), my trusted
expert in Deep Learning, for the discussion and exchange of ideas.
