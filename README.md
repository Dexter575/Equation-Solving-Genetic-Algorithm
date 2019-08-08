# Solving a Linear Equation using Genetic Algorithm (Python)
I have used Genetic Algorithms for solving Equations.
## Q: a+2b+3c+4d = 30 using GA find the value of a,b,c and d.

### step 1 :initialisation

* no. of chromosome in pop. is 6
* c[1] = [a:b:c:d] = [12;05;23;08]
* upto c[6] = [a:b:c:d] = [20;5;17;1]

### step 2 : computation of fitness function

* f_ob[1] = abs((12 + 2*5 + 23*3 +4*8) - 30)
* and so on f_ob[6] = abs((20 + 5*2 + 17*3 + 4*1) -30)

### step 3 : selection

* the fittest chromosome having higher prob. will be selected for next gen.
* fitness[1] = 1/(1+ f_ob[1])
           = 1/94 = 0.0106
and so on upto fitness[6]
after that add them
* total  = fitness[1] + ... + fitness[6] = 0.0845

### step 4 : prob. for eah chromosome

* p[1] = 0.0106/0.0845  = 0.1254
and so on p[6]
* p[4] has the highest fitness to get selected for the next gen.

### step 5 : selection is performed using roulette wheel

* roulette wheel take scumulative prob. value for individual chromosomes

* c[0] = 0
* c[1]  = 0.1254
* c[2] = p[1]+p[2]= 0.2710
* c[3] = 0.4118
* c[4] = 0.6639
* c[5] = 0.7882
* c[6] = p[1] + ...p[6] = 1.0

### step 6 : next we generate random number R in the range 0-1 as follows:

* R[1] = 0.201
* R[2] = 0.284
* R[3] = 0.099
* R[4] = 0.822
* R[5] = 0.398
* R[6] = 0.501

* if R[1] lies bet. c[1] and c[2]  then select chromosome[2] as a chromosome in
 the new pop for the next gen. as it is a higher value.

* new_chromosome[1] = chromosome[2]
* new_chromosome[2] = chromosome[3]
* new_chromosome[3] = chromosome[1]
* new_chromosome[4] = chromosome[6]
* new_chromosome[5] = chromosome[3]
* new_chromosome[6] = chromosome[4]

* chromosomes in the pop. thus become
* chromosome[1] = [2;21;18;3]
* chromosome[2] = [10;4;13;14]
* chromosome[3] = [12;5;23;8]
* chromosome[4] = [20;5;17;1]
* chromosome[5] = [10;4;13;14]
* chromosome[6] = [20;1;10;6]

### step 7 : crossover 

* chromosome is controlled using crossover rate(pc = 0.25)

* begin
* k = 0
* while(k<pop):
 * R[k] = random(0-1)
 * if(R[k] < pc):
  * select chromosome[k] as parent
  * end
 * k +=1
* end
* end

* accordingly for R[1],R[4],R[5] parents  are chromosome[1],chromosome[4]
chromosome[5] selected.

* chromosome[1] = chromosome[1] >< chromosome[4]
* chromosome[4] = chromosome[4] >< chromosome[5]

* chromosome[5] = chromosome[5] >< chromosome[1]

### step 8:  deciding the crossover point
* c[1] = 1
* c[2] = 1
* c[3] = 2 

we selected the random values between 1 to 3

* chromosome[1] = chromosome[1] ><chromosome[4]
                 = [2;21;18;3]><[20;5;17;1]
                  = [2;5;17;1]
* chromosome[4] = chromosome[4] ><chromosome[5]
                 = [20;5;17;1]><[10;4;13;14]
                  = [20;4;13;14]
* chromosome[5] = chromosome[5] ><chromosome[1]
                 = [10;4;13;14]><[2;21;18;3]
                  = [10;4;18;3]
                  
* hence the new chromosome are:

* chromosome[1] = [2;5;17;1]
* chromosome[2] = [10;4;13;14]
* chromosome[3] = [12;5;23;8]
* chromosome[4] = [20;4;13;14]
* chromosome[5] = [10;4;18;3]
* chromosome[6] = [20;1;10;6]

### step 9 :mutation is done by replacing the gene at a random position with
 a new value. we must compute the total length of gen.
  total_gen = no_of_gene_in_chromosome * no. of pop.
   = 4*6 = 24

* mutation process is generating a random no. bet. 1 to 24
if generated random no. is smaller than mutation rate(pm) variable 

* suppose we define pm(mutation_rate) 10% . it is expected that 10% (0.1) of 
 total_genes in the pop. that will be mutated:
no. of mutations = 0.1*24 = 2.4 = 2(apprx.)

* suppose generation of random number yield 12 and 18 then the chromosome 
which have mutation are chromosome number 3 gen number 4 and chromosome 5 
gen. number 2. the value of mutated point is replaced by a random number 
between 0-30 .

* suppose generated random number are 2 and 5 then chromosome composition
after mutation are :

* chromosome[1] = [2;5;17;1]
* chromosome[2] = [10;4;13;14]
* chromosome[3] = [12;5;18;3]
* chromosome[4] = [20;4;13;14]
* chromosome[5] = [10;5;18;3]
* chromosome[6] = [20;1;10;6]

* these new chromosomes will undergo
chromosomes such as evaluation selction,crossover,mutation and at the end it produce
new generation of chromosomes for the next iteration. this process will
be repeated until a predetermined no. of gen. 
after running 50 generations best chromosome is obt.
a = 7,b = 5,c = 3 and d = 1.

Thanks for reading.
