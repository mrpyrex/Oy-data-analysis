import pandas

data = pandas.read_csv('utca.csv')
# 1. Count the number of properties and cal the tax income per property class and print to the screen

property_type_a_count = len(data[data.propertyType == 'A'])
property_type_b_count = len(data[data.propertyType == 'B'])
property_type_c_count = len(data[data.propertyType == 'C'])

type_a = data[data.propertyType == 'A']
type_b = data[data.propertyType == 'A']
type_c = data[data.propertyType == 'C']


data_a_dict = type_a.to_dict()
data_b_dict = type_b.to_dict()
data_c_dict = type_c.to_dict()

df = pandas.DataFrame(data_a_dict)
df_b = pandas.DataFrame(data_b_dict)
df_c = pandas.DataFrame(data_c_dict)

ft_tax_a = ((df.area) * 800).sum()
ft_tax_b = ((df.area) * 600).sum()
ft_tax_c = ((df.area) * 100).sum()


# print(f'Class A: {property_type_a_count} properties, {ft_tax_a} Ft tax.')
# print(f'Class B: {property_type_b_count} properties, {ft_tax_b} Ft tax.')
# print(f'Class C: {property_type_c_count} properties, {ft_tax_c} Ft tax.')

# 2. Count the number of tax free properties

# ft_tax_a = (df.area) * 800
# ft_tax_b = (df.area) * 600
# ft_tax_c = (df.area) * 100



# sum_ft_tax_a = ((df.area) * 800)
# for i in sum_ft_tax_a:
#     if i < 10000:
#         print(i)

# sum_ft_tax_b = ((df.area) * 600)
# for i in sum_ft_tax_b:
#     if i < 10000:
#         print(i)

sum_ft_tax_c = ((df.area) * 100)
for i in sum_ft_tax_c:
    if i < 10000:
        print(i)
