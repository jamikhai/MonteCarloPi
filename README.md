# MonteCarloPi

The Monte Carlo estimation of pi uses a square with side lengths of 1, and a circle centered inside with a radius of 0.5. We already know the area of the the circle is pi/4, and can use that to determine an estimation for pi by generating random points across the 2-D grid and calculating the ratio of points inside the circle to total points.

That is,
```
area of circle / area of sqaure = circle points / square points

pi = 4 * (number of points in the circle / number of points in the square)
```

![Sample Plot](/sample_plot.png)