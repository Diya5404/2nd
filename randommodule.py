import random
random_variable = random.random()
random_int_variable = random.randint(111111,999999)
random_range_variable = random.randrange(100,1000,2)
uniform_random_variable = random.uniform(3,5)
sample_list = [1,2,3,4,5,6,]
choice_variable = random.choice(sample_list)
random.shuffle(sample_list)
print(sample_list)