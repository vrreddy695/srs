# startifiedRS
Stratified random sampling is a type of probability sampling using which a research organization can branch off the entire population into multiple non-overlapping, homogeneous groups (strata) and randomly choose final members from the various strata for research which reduces cost and improves efficiency.

Let’s consider a situation where a research team is seeking opinions about religion amongst various age groups. Instead of collecting feedback from 326,044,985 U.S citizens, random samples of around 10000 can be selected for research. These 10000 citizens can be divided into strata according to age,i.e, groups of 18-29, 30-39, 40-49, 50-59, and 60 and above. 

In this approach, each stratum sample size is directly proportional to the population size of the entire population of strata. That means each strata sample has the same sampling fraction.

Proportionate Stratified Random Sampling Formula: nh = ( Nh / N ) * n
nh= Sample size for hth stratum
Nh= Population size for hth stratum
N = Size of entire population
n = Size of entire sample

example usage
sample=startified_random_smaple(df, 'female', 0.25)

parameters
    dsn: population dataset
    stratas: column nsmaes as list format ex: ['strata1','strata2','strata3....']
    sample_size: how much percentage you want as a sample like 0.05, 0.10, 0.25...
    """
