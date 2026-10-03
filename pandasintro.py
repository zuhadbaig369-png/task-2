import pandas as pd

print('-------Pandas Series-------')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['Nightwolf', 'StarBlaze', 'PixelKing', 'cyberFox', 'IronStorm'])
print(players)

print()
print('-------Part 2: Pandas DataFrame-------')
data = {
    'Player': ['Nightwolf', 'StarBlaze', 'PixelKing', 'cyberFox', 'IronStorm'],
    'level': [42, 38, 35, 30, 27],
    'score': [98500, 87200, 76400, 65100, 54800],
    'Wins': [210, 185, 162, 140, 118]
}

df = pd.DataFrame(data)
print(df)

print()
print('-------Part 3: Accessing Rows-------')
print('Row 0 (top player):')
print(df.loc[0])

print()
print('Rows 2 and 3:')
print(df.loc[2:3])

print()
print('-------Part 4: Reading a CSV File-------')
full_df = pd.read_csv('leaderboard.csv')

print('First 5 rows (head):')
print(full_df.head())

print()
print('Last 3 rows (tail):')
print(full_df.tail(3))

print()
print('Dataset Info:')
print(full_df.info())

print()
print('-------Part 5: Cleaning Data-------')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())

print()
print('Missing values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())

print()
print('-------Part 6: Total and Average-------')

filled_df.columns = filled_df.columns.str.lower()

filled_df['Total'] = filled_df[['level', 'score', 'wins']].sum(axis=1)
filled_df['Average'] = filled_df[['level', 'score', 'wins']].mean(axis=1)

print(filled_df.to_string())

filled_df.to_csv('student_marks.csv', index=False)