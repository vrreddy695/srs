# startifiedRS
Stratified random sampling is a type of probability sampling using which a research organization can branch off the entire population into multiple non-overlapping, homogeneous groups (strata) and randomly choose final members from the various strata for research which reduces cost and improves efficiency. Members in each of these groups should be distinct so that every member of all groups get equal opportunity to be selected using simple probability. This sampling method is also called “random quota sampling”.

Age, socioeconomic divisions, nationality, religion, educational achievements and other such classifications fall under stratified random sampling.

Let’s consider a situation where a research team is seeking opinions about religion amongst various age groups. Instead of collecting feedback from 326,044,985 U.S citizens, random samples of around 10000 can be selected for research. These 10000 citizens can be divided into strata according to age,i.e, groups of 18-29, 30-39, 40-49, 50-59, and 60 and above. Each stratum will have distinct members and number of members.

In this approach, each stratum sample size is directly proportional to the population size of the entire population of strata. That means each strata sample has the same sampling fraction.

Proportionate Stratified Random Sampling Formula: nh = ( Nh / N ) * n
nh= Sample size for hth stratum
Nh= Population size for hth stratum
N = Size of entire population
n = Size of entire sample

Example: bleow is the example data frame
id	female	race	ses	schtyp	prog	read	write	math	science	socst
70	  0	  4	  1	  1	  1	  57	  52	  41	  47	  57
121	  1	  4	  2	  1	  3	  68	  59	  53	  63	  61
86	  0	  4	  3	  1	  1	  44	  33	  54	  58	  31
141	  0	  4	  3	  1	  3	  63	  44	  47	  53	  56
172	  0	  4	  2	  1	  2	  47	  52	  57	  53	  61

praportions of female strata
female  counts    pct
0        91  0.455
1       109  0.545

if you take the startified random sample, the sampel will also have sampe praportions for female variable
sample=startified_random_smaple(df, 'female', 0.25)
parameters
    dsn: population dataset
    stratas: column nsmaes as list format ex: ['strata1','strata2','strata3....']
    sample_size: how much percentage you want as a sample like 0.05, 0.10, 0.25...
    """
sample praportions
female	counts	pct
0   23	0.46
1 	27	0.54
