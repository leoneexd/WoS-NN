# WoS-NN
Implementing neural networks on Walk on Sphere with spatial discretization, for elliptic PDEs with Laplacian operator.

Reference:  
1. Walk on Spheres basic:  
  Mervin E. Muller. “Some Continuous Monte Carlo Methods for the Dirichlet Problem”.  
    Original Walk on Sphere, learn the algorithm process  
  B.S. Elepov and G.A. Mikhailov. “Solution of the Dirichlet problem for the equation∆u − cu = q by a model of "walks on spheres"”.  
    Sample inside to solve the source term, for Poisson equation  
2. Walk on Spheres implementation: Rohan & Keenan’s work  
  Rohan Sawhney and Keenan Crane. “Monte Carlo geometry processing: a grid-free approach to PDE-based methods on volumetric domains”.   
    A simple implementation of WoS in geometry processing.   
    Code: https://www.cs.cmu.edu/~kmcrane/Projects/MonteCarloGeometryProcessing/index.html  
  Rohan Sawhney et al. Grid-Free Monte Carlo for PDEs with Spatially Varying Coefficients.   
    With more complete implementation codes, including adaptive sampling and more examples and details.  
    Code: https://cs.dartmouth.edu/~wjarosz/publications/sawhneyseyb22gridfree.html  
3. PDE – BSDE:   
  Shizuo Kakutani. “Two-dimensional Brownian motion and harmonic functions”.   
  Feynman Kac formula and Ito’s process  
  E. Pardoux and S.G. Peng. “Adapted solution of a backward stochastic differential equation”   
    PDE –> BSDE, the definition of BSDE   
  fully non-linear parabolic PDE –> 2BSDE  
4. Neural Network on time discretization:  
  Jiequn Han, Arnulf Jentzen, and Weinan E. “Solving high-dimensional partial differential equations using deep learning”.   
    semi-linear PDE to BSDE and time discretization with a stacked, big NN.  
    Code: https://github.com/frankhan91/DeepBSDE   
  Come Hure, Huyen Pham, and Xavier Warin. “Deep backward schemes for high-dimensional nonlinear PDEs”  
    Dynamic Programming Deep Learning, backward propagation of time discretization  
  Maximilien Germain, Huyen Pham, and Xavier Warin. “Approximation error analysis of some deep backward schemes for nonlinear PDEs”.  
    Multistep idea  
    Code: https://github.com/MaxGermain/MultistepBSDE   


