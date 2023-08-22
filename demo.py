def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
 
print(fibonacci(9))

# Define a list of participant
participant = ['Monalisa', 'Akbar Hossain',
               'Jakir Hasan', 'Zahadur Rahman', 'Zenifer Lopez']

# Define the function to filters selected candidates
def SelectedPerson(participant):
    selected = ['Akbar Hossain', 'Zillur Rahman', 'Monalisa']
    if (participant in selected):
        return True

selectedList = filter(SelectedPerson, participant)
print('The selected candidates are:')
for candidate in selectedList:
    print(candidate)
