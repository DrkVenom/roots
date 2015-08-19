# roots
tools for calculating roots of a given function

<h2> Functions </h2>
<ul>
  <li><a href="#roots">roots(f,df,a,b,niter,epsilon)</a></li>
  <li><a href="#bisect">bisect(f,a,b,niter,epsilon)</a></li>
  <li><a href="#newton">newton(f,df,x0,niter,epsilon)</a></li>
  <li><a href="#secant">secant(f,a,b,niter,epsilon)</a></li>
</ul>

<h2> TO DO </h2>
<ul>
  <li>add function to plot for root</li>
  <li>add write up for roots</li>
</ul>

<h2> Descriptions </h2>

<h3> Bisect </h3>
<a name="bisect"></a> 
The bisect method requires a function and an interval. An extra parameter was added, eplison, to stop the iterations once a desired accuracy threshold has been reached. The output consists of several items, one of which is the estimated root for the function inside of the given interval.<br>
The bisect method is as follows:
<ol>
  <li>Choose a starting interval (a<sub>0</sub>,b<sub>0</sub>) which contains a root xstar</li>
  <li>Bisect (a<sub>i</sub>,b<sub>i</sub>) into (a<sub>i</sub>,c<sub>i</sub>) and (c<sub>i</sub>,b<sub>i</sub>), where c<sub>i</sub>=(a<sub>i</sub> + b<sub>i</sub>)/2</li>
  <ul>
    <li>if f(a<sub>i</sub>)f(c<sub>i</sub>)<0, then xstar is in (a<sub>i</sub>,c<sub>i</sub>)</li>
    <ul>
      <li>set the next interval to be (a<sub>i+1</sub>,b<sub>i+1</sub>)=(a<sub>i</sub>,c<sub>i</sub>)</li>
      <li>return to step 2</li>
    </ul>
    <li>else xstar is in (c<sub>i</sub>,b<sub>i</sub>)</li>
    <ul>
      <li>set the next interval to be (a<sub>i+1</sub>,b<sub>i+1</sub>)=(c<sub>i</sub>,b<sub>i</sub>)</li>
      <li>return to step 2</li>
    </ul>
  </ul>
  <li>if abs(a<sub>i+1</sub> - b<sub>i+1</sub>) &lt; epsilon, stop iterating over i</li>
  <ul>
    <li>set xstar=(a<sub>i+1</sub> + b<sub>i+1</sub>)/2</li>
  </ul>
</ol>
<h4>Input</h4>
<ul>
  <li>f: the function that we need to find roots for, should be defined prior to running bisect</li>
  <li>a: initial left bracket x-coord</li>
  <li>b: initial right bracket x-coord</li>
  <li>niter: max number of iterations, if the accuracy is within epsilon the method will quit prior to reaching max iterations</li>
  <li>epsilon: tolerance for the stopping rule</li>
</ul>
<h4>Output</h4>
<ul>
  <li>xstar: the root of f for given tolerance epsilon</li>
  <li>err: error at convergence</li>
  <li>fxstar: the value of f at xstar (should be very close to zero as we are expecting a root)</li>
  <li>i: the number of iterations taken to get to the tolerance</li>
  <li>xseq: the values of {x<sub>n</sub>} to see convergence</li>
</ul>

<h3> Newton </h3>
<a name="Newton"></a> 
The Newton method requires a function, its derivative and an estimated starting point. An extra parameter was added, eplison, to stop the iterations once a desired accuracy threshold has been reached. The output consists of several items, one of which is the estimated root for the function inside of the given interval.<br>
The Newton method is as follows:
<ol>
  <li>Select initial x<sub>0</sub></li>
  <li>Iterate x<sub>i</sub> = x<sub>i-1</sub> - f(x<sub>i-1</sub>)/f'(x<sub>i-1</sub>)</li>
  <li>Stop iterating when abs(x<sub>i</sub> - x<sub>i-1</sub>) &lt; epsilon</li>
</ol>
<h4>Input</h4>
<ul>
  <li>f: the function that we need to find roots for, should be defined prior to running Newton</li>
  <li>df: the derivative of the function f, should be defined prior to running Newton</li>
  <li>x0: initial guess for a root</li>
  <li>niter: max number of iterations, if the accuracy is within epsilon the method will quit prior to reaching max iterations</li>
  <li>epsilon: tolerance for the stopping rule</li>
</ul>
<h4>Output</h4>
<ul>
  <li>xstar: the root of f for given tolerance epsilon</li>
  <li>err: error at convergence</li>
  <li>fxstar: the value of f at xstar (should be very close to zero as we are expecting a root)</li>
  <li>i: the number of iterations taken to get to the tolerance</li>
  <li>xseq: the values of {x<sub>n</sub>} to see convergence</li>
</ul>

<h3> Secant </h3>
<a name="Secant"></a> 
The Secant method requires a function and an interval. An extra parameter was added, eplison, to stop the iterations once a desired accuracy threshold has been reached. The output consists of several items, one of which is the estimated root for the function inside of the given interval.<br>
The Secant method is as follows:
<ol>
  <li>Select initial interval (x<sub>0</sub>,x<sub>1</sub>)</li>
  <li>Iterate x<sub>i</sub> = x<sub>i-1</sub> - [f(x<sub>i-1</sub>)(x<sub>i-1</sub> - x<sub>i-2</sub>)]/[f(x<sub>i-1</sub>) - f(x<sub>i-2</sub>)]</li>
  <li>Stop iterating when abs(x<sub>i</sub> - x<sub>i-1</sub>) &lt; epsilon</li>
</ol>
<h4>Input</h4>
<ul>
  <li>f: the function that we need to find roots for, should be defined prior to running Newton</li>
  <li>a: initial left bracket x-coord</li>
  <li>b: initial right bracket x-coord</li>
  <li>niter: max number of iterations, if the accuracy is within epsilon the method will quit prior to reaching max iterations</li>
  <li>epsilon: tolerance for the stopping rule</li>
</ul>
<h4>Output</h4>
<ul>
  <li>xstar: the root of f for given tolerance epsilon</li>
  <li>err: error at convergence</li>
  <li>fxstar: the value of f at xstar (should be very close to zero as we are expecting a root)</li>
  <li>i: the number of iterations taken to get to the tolerance</li>
  <li>xseq: the values of {x<sub>n</sub>} to see convergence</li>
</ul>
