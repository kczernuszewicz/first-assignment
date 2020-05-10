import pandas as pd
import matplotlib.pyplot as plt

df_results = pd.read_csv('survey_results_public.csv', usecols=['Respondent', 'ConvertedComp', 'Age', 'OpSys'], index_col='Respondent')
df_results.dropna(inplace=True)
df_results_windows = df_results.loc[df_results['OpSys'] == 'Windows']
df_results_linux = df_results.loc[df_results['OpSys'] == 'Linux-based']
df_results_macos = df_results.loc[df_results['OpSys'] == 'MacOS']

plt.plot(df_results_windows['Age'], df_results_windows['ConvertedComp']/1000, 'bo', markersize=0.5)
plt.xlabel('Age')
plt.ylabel('ConvertedComp in K')
plt.title('Windows')
plt.show()

plt.plot(df_results_linux['Age'], df_results_linux['ConvertedComp']/1000, 'bo', markersize=0.5)
plt.xlabel('Age')
plt.ylabel('ConvertedComp in K')
plt.title('Linux')
plt.show()

plt.plot(df_results_macos['Age'], df_results_macos['ConvertedComp']/1000, 'bo', markersize=0.5)
plt.xlabel('Age')
plt.ylabel('ConvertedComp in K')
plt.title('macOS')
plt.show()