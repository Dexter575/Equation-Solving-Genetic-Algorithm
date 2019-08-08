import numpy as np
"""
f(x) = a +2b + 3c +4d -30
"""
# Initializing n = 6
n = 6
# Initialization of chromosomes
# chromosome
chromosome = np.random.randint(0,30 ,(n,4))
print("chromosomes :",chromosome)
epoch = 0

while epoch <  200 :
    # Computation of fitness function
    objective = abs(30 - chromosome[:,0] - 2*chromosome[:,1] -3*chromosome[:,2] -
                    4*chromosome[:,3] )
    print("Fitness object :", objective)
    
    # Selection of fittest chromosome
    fitness =  1/(1 + objective)
    print("Fitness :",fitness)
    
    # Calculating the total of fitness function
    total = fitness.sum()
    print("Total :",total)
    
    # Calculating Probablility for each chromosome
    prob = fitness/total
    print("Probability :",prob)
    
    # Selection using Roulette Wheel And Calculating Cumulative Probability
    cum_sum = np.cumsum(prob)
    print("Cumulative Sum :", cum_sum)
    
    # Generating Random Numbers in the range 0-1
    Ran_nums = np.random.random((chromosome.shape[0]))
    print("Random Numbers :",Ran_nums)
    
    # Making a new matrix of chromosome for calculation purpose
    chromosome_2 = np.zeros((chromosome.shape[0],4))
    
    for i in range(Ran_nums.shape[0]):
        for j in range(chromosome.shape[0]):
            if Ran_nums[i]  < cum_sum[j]:
                chromosome_2[i,:] = chromosome[j,:]
                break
            
    chromosome = chromosome_2
    print("Chromosomes after updation :",chromosome)
        
    # crossover
    R = [np.random.random() for i in range(n)]
    print("Random Values :",R)
    
    # Crossover Rate
    pc = 0.25
    flag = Ran_nums < pc
    print("Flagged Values :",flag)
    
    # Determining the cross chromosomes
    cross_chromosome = chromosome[[(i == True) for i in flag]]
    print("Cross chromosome :",cross_chromosome)
    len_cross_chrom = len(cross_chromosome)
    
    # Calculating cross values
    cross_values = np.random.randint(1,3,len_cross_chrom)
    print("Cross Values :",cross_values)
    
    cpy_chromosome = np.zeros(cross_chromosome.shape)
    
    # Performing Cross-Over
    
    # Copying the chromosome values for calculations
    for i in range(cross_chromosome.shape[0]):
        cpy_chromosome[i , :] = cross_chromosome[i , :]
        
    if len_cross_chrom == 1:
        cross_chromosome = cross_chromosome
    else :
        for i in range(len_cross_chrom):
            c_val = cross_values[i]
            if i == len_cross_chrom - 1 :
                cross_chromosome[i , c_val:] = cpy_chromosome[0 , c_val:]
            else :
                cross_chromosome[i , c_val:] = cpy_chromosome[i+1 , c_val:]
        
    print("Crossovered Chromosome :",cross_chromosome)
    
    index_chromosome = 0
    index_newchromosome = 0
    for i in flag :
        if i == True :
            chromosome[index_chromosome, :] = cross_chromosome[index_newchromosome, :]
            index_newchromosome = index_newchromosome + 1
        index_chromosome = index_chromosome + 1 
    
    print("New Chromosomes:", chromosome)
    
    # Calculating the total no. of generations
    a ,b = chromosome.shape[0] ,chromosome.shape[1]
    total_gen = a*b
    print("Total Generations :",total_gen)
    
    #mutation rate = pm
    pm = 0.1
    no_of_mutations = int(np.round(pm * total_gen))
    print("No. of Mutations :" ,no_of_mutations)
    
    # Calculating the Generation number
    gen_num = np.random.randint(0,total_gen - 1, no_of_mutations)
    print(" Generated Random Numbers : " , gen_num)
    
    # Generating a random number which can replace the selected chromosome to be mutated
    Replacing_num = np.random.randint(0,30, no_of_mutations)
    print(" Numbers to be replaced : " , Replacing_num)
    
    for i in range(no_of_mutations):
        a = gen_num[i]
        row = a//4
        col = a%4
        chromosome[row , col] = Replacing_num[i]
    
    print(" Chromosomes After Mutation : " , chromosome)
  
    epoch = epoch + 1