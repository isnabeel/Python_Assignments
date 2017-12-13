#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:00:14 2017

@author: ismailnabeel
"""
import pandas as pd


class Person(object):
    
    # TODO: add a data structure containing this person's variants, and methods that add a variant,
    # and list all variants
    
    
    # TODO: standardize the representations of gender, so that M, m, and male are valid inputs
    # for male, but only one standard stored constant represents male, and similarly for female.
    
    def __init__(self, name, gender, mother=None, father=None):
        self.name   = name
        self.gender = gender
        self.mother = mother
        self.father = father
        self.children = set() 
        self.variant_instance_list_one_person = []
    
    def Add_a_variant(self, Variant_instance):
        """ Add a Variant_instance """
        self.variant_instance_list.append(Variant_instance)
        
    def Add_list_of_variants(self, clean_variant_instant_list):
        ## loop over variant_list. if variant_i.person == 'ismail', append variant_i to variant_instance_list_one_person
        for i in clean_variant_instant_list:
            if i.name == self.name:
                print(i)
                self.variant_instance_list_one_person.append(i)
        
    
    def clean_gender(self):
        male_valid_inputs = ['male', 'Male', 'm', 'M']
        if self.gender in male_valid_inputs:
            self.gender = 'male'
        female_valid_inputs = ['female','Female','f', 'F']
        if self.gender in female_valid_inputs:
            self.gender ='female' 
            

    @staticmethod
    def get_persons_name(person):
        if person is None:
            return 'NA'
        return person.name
    
    """def add_child(self,child):
    #    self.children.add(child)
    #    return 'Your child name is'
    """

    def set_father(self, father):
        """ set father """
        self.father = father
        self.father.children.add(self)
        return (father)
        
    
    def set_mother(self, mother):
        """ set mother """
        self.mother = mother  
        self.mother.children.add(self)
        return (mother)
    
    
    def remove_father(self):
        self.father = None
        return
    
    def remove_mother(self):
        self.mother = None
        return
    
    def siblings(self):
        """ creating siblings """
        father_children = [i.name for i in self.father.children]
        mother_children = [i.name for i in self.mother.children]
        siblings = set(father_children).intersection(mother_children)
        siblings.remove(self.name)
        return (siblings)
        
    def half_siblings(self): 
        """ creating half_siblings """
        half_siblings = self.father.children.symmetric_difference(self.mother.children)
        return (half_siblings)                
        
    
    def sons(self):
        sons = []
        for child in self.children:
            if child.gender == 'male':
                sons.append(child)
        return sons
    
    def daughters(self):
        """ creating self daughter """
        daughters = []
        for child in self.children:
            if child.gender == 'female':
                daughters.append(child)
        return daughters
    
    def __str__(self):
        return '{}:gender,{}; mother {}; father {}'.format(\
            self.name,
            self.gender,
            Person.get_persons_name(self.mother),
            Person.get_persons_name(self.father))
    
    def grandparents_structured(self):        
        grandparents = []
        if self.mother:
            grandparents.extend([self.mother.mother, self.mother.father])
        else:
            grandparents.extend([None,None])
        if self.father:
            grandparents.extend([self.father.mother,self.father.father])
        else:
            grandparents.extend([None,None])
        return tuple(grandparents)
    
    def children_structured(self):        
        children = []
        if self.parents_children:
            children.extend([self.children])
        else:
            children.extend([None,None])
        return list(children)
    
    # TODO: EXTRA CREDIT: implement this descendants method, which has analogous semantics to the
    # ancestors method below. The implementation may use a while loop or be recursive. Use
    # your 'descendants' method to implement 'children', 'grand_children', and 'all_descendants'.
    
    def descendents(self, min_depth,max_depth=None):
        if max_depth is not None:
            if max_depth < min_depth:
                raise ValueError('max_depth ({}) cannot be less than min_depth ({})'.format(max_depth,min_depth))
        else:
            max_depth=min_depth
            collected_descendents = set()
        return descendents(collected_descendents,min_depth,max_depth)
    
    def _descendents(self, collected_descendents,min_depth,max_depth):
        if min_depth <=0:
            collected_descendents.add(self)
        if 0 < max_depth:
            for child in [self.mother, self.father]:
                if child is not None:
                    child._descendents(collected_descendents,min_depth, max_depth)
        return collected_descendents
            
    
    def ancestors(self, min_depth,max_depth=None):
        if max_depth is not None:
            if max_depth < min_depth:
                raise ValueError('max_depth ({}) cannot be less than min_depth ({})'.format(
                    max_depth,min_depth))
        else:
            max_depth=min_depth
        collected_ancestors = set()
        return self._ancestors(collected_ancestors,min_depth,max_depth)
    
    def _ancestors(self, collected_ancestors,min_depth,max_depth):
        if min_depth <=0:
            collected_ancestors.add(self)
        if 0 < max_depth:
            for parent in [self.mother,self.father]:
                if parent is not None:
                    parent._ancestors(collected_ancestors,min_depth, max_depth)
        return collected_ancestors
    
    def parents(self):
        return self.ancestors(1)
    
    def grandparents(self):
        return self.ancestors(2)
    
    def great_grandparents(self):
        return self.ancestors(3)
    
    def all_grandparents(self):
        return self.ancestors(1, max_depth=float('inf'))
    
    def all_ancestors(self):
        return self.ancestors(1, max_depth=float('inf'))
    
    def parents_children(self):
        return self._descendents(1)
    
    def grandchildren(self):
        return self._descendents(2)
    
    def great_grandchildren(self):
        return self._descendents(3)
    
    def all_grandchildren(self):
        return self._descendents(1, max_depth=float('inf'))
    
    def all_descendents(self):
        return self._descendents(1, max_depth=float('inf'))
    
def print_people(people):
    for p in people:
        print(p)
    
ismail = Person('Ismail','male')
assert ismail.name == 'Ismail'
ismail.mother = Person('Aziz','female')


ismail.father = Person('Altaf','male')
paternal_gf = ismail.father.father = Person('Altaf_father', 'male')
paternal_gf.father = Person('Altaf_father_ggf','male')

ismail.clean_gender()
print(ismail.gender)

print(print_people(ismail.ancestors(2)))

ismail.mother = Person('Aziz','female')
maternal_gm = ismail.mother.mother = Person('Aziz_mother', 'female')
maternal_gm.mother = Person('Aziz_Maternal_ggm','female')
ismail.father = Person('Altaf','male')
ismail.father.father = Person('Altaf_father', 'male')
paternal_gf.father = Person('Altaf_father_ggf','male')

print('++++++++');print_people(ismail.ancestors(1))


maternal_gm = ismail.mother.mother = Person('Aziz_mother', 'female')


ismail.father = Person('Altaf','male')
print_people(ismail.parents())

ismail.father.father = Person('Altaf_father', 'male')
paternal_gf.father = Person('Altaf_father_ggf','male')
maternal_gm.mother = Person('Aziz_Maternal_ggm','female')
print('\n');print_people(ismail.grandparents_structured())
print_people(ismail.grandparents())
print_people(ismail.great_grandparents())


inf=float('inf')
print_people(ismail.all_ancestors())
print_people(ismail.ancestors(0,inf))


ismail.set_mother(ismail.mother)
ismail.set_father(ismail.father)
print_people(ismail.mother.sons())
ismail.sons()
ismail.daughters()

# Making Zara Ismail's daughter
ismail.daughters = Person('Zara','female',father=ismail)
print_people(ismail.children)
print_people(ismail.children_structured())
print_people(ismail.children)

ismail_father=Person('Altaf','male')
ismail.set_father(ismail_father)

print("Listing Ismail's father's children")
print(list(ismail_father.children)[0])
#ismail.remove_father()
#ismail.remove_mother()
ismail_mother=Person('Aziz','female')
ismail.set_mother(ismail_mother)


# Make'Hani' brother

hani = Person('Hani','male')
hani.set_mother(ismail_mother)
hani.set_father(ismail_father)

# make 'Lubna' half_sister

lubna = Person('Lubna','female')
lubna.set_mother(ismail_mother)


# print siblings
print_people(ismail.siblings())

# print half_siblings

print_people(ismail.half_siblings())
ismail.__dict__

""" Adding list of variants to the person object """
ismail.Add_list_of_variants(clean_variant_instant_list)
ismail_mother.Add_list_of_variants(clean_variant_instant_list)
ismail_father.Add_list_of_variants(clean_variant_instant_list)
#print(ismail.variant_instance_list_one_person) ## all variant instances with Ismail as the name

##help(Person)###



class Variant(object):
    # creating a function for the Variance Class
    
    def __init__(self, chrom,loc,ref,alt,name):
        self.chrom = chrom
        self.loc = loc
        self.ref = ref
        self.alt = alt
        self.name = name
    def __str__(self):
        return 'name,{}; chrom {}; loc {}; ref {}; alt {}'.format\
            (self.name,self.chrom,self.loc, self.ref, self.alt)
    
##

variant_data = '/Users/ismailnabeel/Desktop/Google_Drive/Jupyter_notebook_exercises/datafiles/genetic_code.csv'
with open(variant_data, 'rt') as f:
    variant_data = pd.read_csv(f, header=None,names = ['chrom', 'loc','ref','alt','name'])


variant_data
variant_instance_list = []
## loop over every row in pandas dataframe
## check that every row is valid. chromosome is real, loc > 0 loc< chrom_length,
variant_instance = Variant('chr1', 1000, 'A', 'G', 'Ismail')
variant_instance_list.append(variant_instance)
variant_data


##help(Variant)##

class LoadInformation:
    """ class that load people and variant data from the files """
    @staticmethod
    def load_people(path):
        person_list = []
        for index, row in person_df.iterrows():
            mother_instance = Person(row['mother_name'], 'F')
            father_instance = Person(row['father_name'], 'M')
            person = Person(row['name'], row['gender'], mother_instance, father_instance) 
            print(person)
            person_list.append(person)
            
        person_list[0].Add_list_of_variants(clean_variant_instant_list)
        person_list[1].Add_list_of_variants(clean_variant_instant_list)
        person_list[2].Add_list_of_variants(clean_variant_instant_list)
        person_list[3].Add_list_of_variants(clean_variant_instant_list)
        person_list[4].Add_list_of_variants(clean_variant_instant_list)
        person_list[5].Add_list_of_variants(clean_variant_instant_list)
        
    
    @staticmethod
    def load_variant(path):
        valid_bases = ['A', 'C', 'T', 'G']
        with open(path, 'rt') as f:
            chrom_ref_table = pd.read_csv(f, header=None, delim_whitespace=True,\
                                     names = ['chrom', 'len_chrom']) # Parse file with pandas
        
        variant_instance_list = []
        for index, row in variant_data.iterrows():
            variant_instance = Variant(row['chrom'], row['loc'], row['ref'],row['alt'],row['name'])
            #print(variant_instance)
            variant_instance_list.append(variant_instance)
        
        bad_variant_list = []

        for variant_instance in variant_instance_list:
            if chrom_ref_table['chrom'].str.contains(variant_instance.chrom).any():
                print('chrom is correct')
            else:
                print('chrom is NOT correct', variant_instance.chrom)
                bad_variant_list.append(variant_instance) # bad_variant
                continue
                
            ## obtain length of current chromosome
            current_chrom_len = chrom_ref_table.loc[chrom_ref_table.chrom == variant_instance.chrom].len_chrom
            print(variant_instance.loc)

            ## check if the location is an integer
            try:
                if int(variant_instance.loc) < int(current_chrom_len) and int(variant_instance.loc) >= 0:
                    print('Length is correct')
                else:
                    bad_variant_list.append(variant_instance)
                    continue
            except ValueError:
                print('not int')
                bad_variant_list.append(variant_instance)
                continue
            ## check if the ref is in valid_bases
            if variant_instance.ref in valid_bases:
                print('this ref is correct')
            else:
                bad_variant_list.append(variant_instance)
                continue
            ## check if the alt is in valid_bases
            if variant_instance.alt in valid_bases:
                print('alt is correct')
            else:
                bad_variant_list.append(variant_instance)
                continue
        clean_variant_instant_list = [x for x in variant_instance_list if x not in bad_variant_list] # vallidation testing
        return(clean_variant_instant_list)
        


filename = '/Users/ismailnabeel/Desktop/Google_Drive/Jupyter_notebook_exercises/datafiles/hg38.chrom_modified.txt'
person_df=pd.read_csv('/Users/ismailnabeel/Desktop/Google_Drive/Jupyter_notebook_exercises/datafiles/Load_People.csv')
clean_variant_instant_list = LoadInformation.load_variant(filename)
#load_people(person_df)
LoadInformation.load_people(person_df)
print(len(clean_variant_instant_list))
print(len(variant_instance_list))
#print(len(bad_variant_list))
print(variant_instance_list)

print(person_df)
print(variant_data)
