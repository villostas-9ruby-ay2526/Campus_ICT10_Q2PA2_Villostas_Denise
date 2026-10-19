# Participation Activity

from pyscript import display, document

def kunin_ang_pangalan(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('first').value.lower().strip()
    second_name = document.getElementById('last').value.lower().strip()
    name_input = first_name + second_name


    grade_7 = {'Francesca Ong', 'Matthea Ong'}
    grade_9 = {'Lorin Jose', 'Sky Campo'}
    grade_10 = {'Isabelle Cabatu', 'Leiane Gabia'}
    grade_11 = {'Jade Cabatingan', 'Ashley Gozum'}
    all_dance_club = grade_7 | grade_9 | grade_10 | grade_11
    all_dance_club.add(name_input)
    
    display(all_dance_club, target='result')
    display(len(all_dance_club), target='result')

