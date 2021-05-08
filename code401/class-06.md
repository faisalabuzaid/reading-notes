# Random Module

The random module provides access to functions that support many operations. Perhaps the most important thing is that it allows you to generate random numbers.



## When to use it

We want the computer to pick a random number in a given range Pick a random element from a list, pick a random card from a deck, flip a coin etc. When making your password database more secure or powering a random page feature of your website.

## Random functions 

The Random module contains some very useful functions.

**Randint**

If we wanted a random integer, we can use the randint function Randint accepts two parameters: a lowest and a highest number. Generate integers between 1,5. The first value should be less than the second.


``` import random ```

``` print random.randint(0, 5) ```

This will output either 1, 2, 3, 4 or 5.


# Risk Analysis in Software Testing

The probability of any unwanted incident is defined as Risk. In Software Testing, risk analysis is the process of identifying the risks in applications or software that you built and prioritizing them to test. After that, the process of assigning the level of risk is done. The categorization of the risks takes place, hence, the impact of the risk is calculated.

## Why use Risk Analysis?

it helps the developers and managers to mitigate the risks. When a test plan has been created, risks involved in testing the product are to be taken into consideration along with the possibility of the damage they may cause to your software along with solutions.

![risk-analysis-image](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/08/risk-analysis.jpg)


**possible risks that you could encounter:**

1. Use of new hardware
2. Use of new technology
3. Use of new automation tool
4. The sequence of code
5. Availability of test resources for the application

**Unavoidable risks:**

1. The time that you allocated for testing

2. A defect leakage due to the complexity or size of the application

3. Urgency from the clients to deliver the project

4. Incomplete requirements

## **Risk magnitude indicator**

**High**: means the effect of the risk would be very high and non-tolerable. The company might face loss.

**Medium**: it is tolerable but not desirable. The company may suffer financially but there is a limited risk.

**Low**: it is tolerable. There lies little or no external exposure or no financial loss.

## Risk Identification


There are different sets of risks included in the risk identification process. Those are as follows:

**Business Risks**: This risk is the most common risk associated with our topic. It is the risk that may come from your company or your customer, not from your project.

**Testing Risks**: You should be well acquainted with the platform you are working on, along with the software testing tools being used.

**Premature Release Risk**: a fair amount of knowledge to analyze the risk associated with releasing unsatisfactory or untested software is required

**Software Risks**: You should be well versed with the risks associated with the software development process.


## Risk assessments 

Perspectives of Risk Assessment:

- Effect: To assess risk by Effect. In case you identify a condition, event or action and try to determine its impact.

- Cause: To assess risk by Cause is opposite of by Effect. Initialize scanning the problem and reach to the point that could be the most probable reason behind that.

- Likelihood: To assess risk by Likelihood is to say that there is a probability that a requirement won’t be satisfied.
