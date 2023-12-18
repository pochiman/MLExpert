# Deep Learning

# 16 - Generative Adversarial Neural Networks

Generator: "I promise this is a real Rolex."
Discriminator: "No, it's definitely not."
Generator: "What if I change the position of the hands slightly and then promise 
it's real again?"
Discriminator: "I'll almost certainly believe you then."

# Key Terms

# [Generative_Adversarial_Networks]
Also GANs, take advantage of a concept called adversarial min max. The generator 
generates fake data and tries to minimize a particular loss function and the 
discriminator tries to correctly identify fake data from real data in an effort 
to maximize a particular loss function.
    
# [Mode_Collapse]
A challenge of training GANs in which the generator generates data which successfully 
confuses the discriminator and so the generator exploits this vulnerability and only 
produces that particular data over and over. A way to mitigate this is to force the 
generator to see responses from the discriminator multiple timesteps ahead. One such 
method is called an Unrolled GAN.
