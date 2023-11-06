# Radon-222 Decay Monte Carlo
 A Monte Carlo Simulation of Radon-222 Decay.

** Note: there are two different implementations. 
**

# Monte Carlo Implementation (radon_decay_monte_carlo.py)

 This code simulates the full decay tree of Ra-222 (not just the main decay chain) using monte carlo techniques.
 
<img width="132" alt="image" src="https://github.com/xan3c/Radon-222-Decay-Monte-Carlo/assets/87034306/d29a06b3-0434-4916-bf23-a38ff9dd4f35">


Image courtesy of:https://periodictable.com/

# Coupled Differential Equations (radon_decay_coupled_ODEs.py)

This code only simulates the main chain. It uses a wrapper of a C++ implementation of LSODA to be 1000x faster in solving the ODE over scipy's solve_ivp(). 
Find the wrapper here: https://github.com/Nicholaswogan/numbalsoda
