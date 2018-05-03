**What are activation functions and why do we need them?**
Activation functions are important components of neural networks. Both in Perceptron models or Neural Network models, they take in some data, add non linearity to the data before giving the output to the next layer. The terms linear and non-linear can be intuitively understood by considering them as straight lines and non-straight curves. Without the activation functions, the perceptron models that take weighted sum of inputs in each layer or the convolution models that use kernels by element wise multiplication, are just a stack of layers that perform linear regression and can only detect or model data that is linearly detectable or separable.

There are many activation functions that are used.Let's see how some of the most used activation functions work.

**Sigmoid Function**

Sigmoid is one of the most used activation functions. Given a value to it, it squashes it and outputs value between 0 and 1. So Sigmoid's output can be treated as probability values. As seen in the curve below, from a certain negative value, the curve gets flat and close to 0. Similarly for some positive values, the curve gets flat and constant. The gradients at these regions will be 0 and this leads to vanishing gradient.
![](https://cdn-images-1.medium.com/max/1600/1*XxxiA0jJvPrHEJHD4z893g.png)

**Rectified Linear Unit** 

As shown in the plot, ReLu is a simple activation function. It takes some numerical input **z** and outputs **0** if z is negative, **z** otherwise. Though ReLu is not entirely linear, we can see that it has a linear form for values that are positive. <br>
ReLu is easy to compute. Its curve is horizontal for values below 0 and incrementing linearly for values above 0. What this means is that, during the forward pass, the neurons that are fed with negative data will be set to 0. This might seem like a problem but considering the fact that the initial weights are random,could be negative and should be vastly optimized to minimize the cost, it is ok to have some neurons that are set to 0. This induces some kind of sparsity into the network.
<br>
But the same reasons that make ReLu simple and easy to implement also lead to some drawbacks. Consider the horizontal line again for values below 0. During the backpropagation phase, the gradient for this region will be 0 which means the neurons with this gradient will never be updated. There are other variants of ReLu that try to fix this problem.

**Leaky ReLu**

As we identified, the problem is with the horizontal region in the ReLu curve. So instead of giving 0 for all negative values, it's better to have some output for the region with the horizontal curve. This can be done using Leaky ReLu:

**R(z) = max(0.1z,z)**

With Leaky ReLu, for the negative values, the slope will not be zero. We give it a slight positive slope of 0.1 so that all the neurons with negative values wont be set to 0. Though this partially fixes the dying gradient problem in ReLu, it can still face the same problems in some cases.


**ELU**

Exponential Linear Unit function is of the form:

![](http://saikatbasak.in/public/img/elu.jpg)

In ELU, instead of giving the negative region a slight slope of 0.1, we have α(exp(x) - 1) which gives mean activations of zero that helps in faster convergance.

**SELU**

Scaled Exponential Linear Units is of the form:
![](https://www.hardikp.com/assets/selu.png)  

From the paper [here](https://arxiv.org/abs/1706.02515), SELUs induce self-normalizing properties which makes training deep networks with many layers and their learning robust. Though SELUs can give better outcomes than RELUs, it takes some specific configuration that should be used to achieve those results.

The field of Deep Learning and Neural Network is evolving too quickly. Though Sigmoid was widely used as activation function earlier, now the Deep Learning community has switched to Relu as its favorite activation function.  
