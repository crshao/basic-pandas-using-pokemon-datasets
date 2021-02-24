import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pokemon_df = pd.read_excel("Pokemon_Gen_1-8.xlsx")
team_attack = pokemon_df.loc[0:600, ['Name', 'Type 1', 'Attack']]
team_attack = team_attack.rename(columns={"Type 1": "Type_1"})
team_attack_fire = team_attack[team_attack.Type_1 == "Fire"]


print(team_attack_fire.sort_values("Attack", ascending=False)) #original variable stay put
print(team_attack_fire)
