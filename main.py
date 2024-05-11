import pandas as pd

data = pd.read_csv(
    r'C:\-AL-\all projects\vs code projects\personal-projects\data-analyzer\responses.csv')

# Questions from data
count_questions = [
    "What types of devices do you use frequently?",
    "What is your preferred learning method?",
    "Do the amount of hours you spend studying change during midterm/final exam weeks?",
    "Which of the following digital apps do you use?",
    "How often do you use these digital apps?",
    "Which of the following physical organization tools do you use?",
    "How often do you use these physical organization tools?",
    "What do you like about the digital and physical organization tools you use?",
    "What do you dislike about the digital and physical organization tools you use?",
    "Which of these initiatives/projects interest you?",
    "Which of these sustainability campaigns/projects are you interested in and would like to see in your community?"
]

# Count and display percentage of respondents
for question in count_questions:
    print(f'\nCount and % for "{question}":')

    counts = data[question].value_counts()
    percentages = (counts / data.shape[0]) * 100

    display_data = pd.DataFrame({'Count': counts, 'Percentage': percentages})
    print(display_data)
