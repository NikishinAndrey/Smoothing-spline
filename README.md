# Smoothing-spline
Approximation using a smoothing cubic spline, whose nodes coincide with the interpolation nodes on the Chebyshev grid.

Given: Some grid and a grid function with an error from a tabulated function, for which it is required to construct a smoothing cubic spline.

$$ a_i = \frac{1}{3} (h_{i-1} + h_{i}) + \frac{1}{h_{i-1}^2}\rho_{i-1} + (\frac{1}{h_{i-1}} + \frac{1}{h_{i}})^2\rho_i + \frac{1}{h_i^2} \rho_{i+1}, \ i = 1, 2, \dots , m-1 $$

$$ b_i = \frac{1}{6}h_i - \frac{1}{h_i}((\frac{1}{h_{i-1}}+ \frac{1}{h_i})\rho_i + (\frac{1}{h_{i-1}}+ \frac{1}{h_i})\rho_{i+1}) \ i = 1, 2, \dots , m-2 $$

$$c_i = \frac{1}{h_{i}h_{i+1}} \rho{i+1}, \ i = 1, 2, \dots , m-3 $$
			    
$$ g_i = \frac{y_{i+1} - y_{i}}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}, \ i = 1, 2, \dots , m-1 $$

Boundary conditions:

$$ a_0 = 1 \ b_0 = 1 \ c_0 = 0 \ g_0 = 0 $$

$$ a_m = 1 \ b_{m-1} = 1 \ c_{m-2} = 0 \ g_m = 0 $$

System of algebraic equations: 

$$ a_0n_0 + b_0n_1 + c_on_2 = g_0, $$

$$ b_0n_0 + a_1n_1 + b_1n_2 + c_1n_3 = g_1, $$

$$ \dots \dots \dots \dots \dots \dots \dots $$

$$ c_{i-2}n_{i-2} + b_{i-1}n_{i-1} + a_in_i +b_in_{i+1} + c_in_{i+2} = g_i, \ i = 2, 3, \dots, m-2, $$

$$ c_{m-3}n_{m-3} + b_{n-2}n_{m-2} + a_{m-1}n_{m-1} + b_{m-1}n_{m} = g_{m-1}, $$

$$ c_{m-2}n_{m-2} + b_{m-1}n_{m-1} + a_mb_m = g_m $$

![image](https://github.com/NikishinAndrey/Smoothing-spline/assets/113716137/fa78d7b7-09ee-4b8c-865c-a0d32d2a338a)

![image](https://github.com/NikishinAndrey/Smoothing-spline/assets/113716137/4d6f58f4-574d-4be3-857a-1e30f13ae943)

![image](https://github.com/NikishinAndrey/Smoothing-spline/assets/113716137/d2b3c072-28f0-4079-a64b-c693a30493ab)

![image](https://github.com/NikishinAndrey/Smoothing-spline/assets/113716137/320ccae2-bacf-46af-b327-bfe0f218d55f)


![image](https://github.com/NikishinAndrey/Smoothing-spline/assets/113716137/664db767-4e23-4941-80dc-0cedf9418a24)
