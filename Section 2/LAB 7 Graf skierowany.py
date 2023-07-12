V = ['Berlin', 'Paris', 'Rome', 'Madrid', 'Warsaw', 'Praque', 'Wien']
E = [ ('Madrid', 'Paris'),
('Paris', 'Berlin'),
('Berlin', 'Warsaw'),
('Warsaw','Praque'),
('Praque', 'Wien'),
('Wien', 'Rome'),
('Berlin', 'Wien'),
('Rome', 'Praque'),
('Praque', 'Warsaw')
]

print([y for x,y in E if x == 'Berlin'])
print([x for x,y in E if y == 'Warsaw'])