import math

mu=75
xbar=72
s=6
n=10
alpha=0.05
#Defining the population mean, sample mean, sample deviation, sample size and significance level.

Zc=1.96
#Taking the critical Z value for a two-tailed test at 5% significance level.

SE=s/math.sqrt(n)
#Calculating the standard error using s/root(n).

lower_CV=mu-Zc*SE
upper_CV=mu+Zc*SE
#Finding the lower and upper critical value range limits.

print("Critical Value Method Result")
print("Lower Limit =",round(lower_CV,2))
print("Upper Limit =",round(upper_CV,2))
#Displaying the critical range values.

if lower_CV<=xbar<=upper_CV:
    print("\nSample mean is within the acceptance range.")
    print("Decision = Fail to Reject H0 (Claim is accepted)")
    #If xbar lies within the range then null hypothesis is accepted.
else:
    print("\nSample mean is outside the acceptance range.")
    print("Decision = Reject H0 (Claim is not accepted)")
    #If xbar lies outside the range then null hypothesis is rejected.
