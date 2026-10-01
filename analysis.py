import pandas as pd

data = pd.read_csv("ipl_data.csv")

print(data)
team_runs = data.groupby("Team")["Runs"].mean()

print("\nTeam-wise Average Runs:")

print(team_runs.round(2))
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

team_runs.plot(kind="bar")

plt.xlabel("IPL Teams")
plt.ylabel("Average Runs")
plt.title("Team-wise Average Runs")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
highest_team = team_runs.idxmax()
highest_runs = team_runs.max()

print("\nHighest Scoring Team:")
print("Team:", highest_team)
print("Average Runs:", round(highest_runs, 2))
team_summary = data.groupby("Team")[["Runs", "Wickets"]].sum()

print("\nTeam-wise Total Runs and Wickets:")
print(team_summary)
highest_wickets = team_summary["Wickets"].idxmax()
wicket_count = team_summary["Wickets"].max()

print("\nMost Wickets in Dataset:")
print("Team:", highest_wickets)
print("Wickets:", wicket_count)
team_summary["Runs"].plot(kind="bar")

plt.xlabel("IPL Teams")
plt.ylabel("Total Runs")
plt.title("Team-wise Total Runs")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
team_summary["Runs"].plot(kind="bar")

plt.xlabel("IPL Teams")
plt.ylabel("Total Runs")
plt.title("Team-wise Total Runs")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
venue_runs = data.groupby("Venue")["Runs"].mean()

print("\nVenue-wise Average Runs:")
print(venue_runs.round(2))
venue_runs.plot(kind="bar")

plt.xlabel("Venue")
plt.ylabel("Average Runs")
plt.title("Venue-wise Average Runs")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
highest_match = data.loc[data["Runs"].idxmax()]

print("\nHighest Scoring Match:")
print("Match ID:", highest_match["Match_ID"])
print("Team:", highest_match["Team"])
print("Opponent:", highest_match["Opponent"])
print("Runs:", highest_match["Runs"])
print("Venue:", highest_match["Venue"])
team_summary["Runs"].plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)

plt.title("Team-wise Total Runs Distribution")
plt.ylabel("")
plt.show()
print("\n--- IPL FINAL ANALYSIS REPORT ---")

print("Total Matches:", len(data))
print("Total Teams:", data["Team"].nunique())
print("Total Runs:", data["Runs"].sum())
print("Total Wickets:", data["Wickets"].sum())

print("Highest Team Average:", round(team_runs.max(), 2))
print("Highest Scoring Team:", team_runs.idxmax())

print("Highest Scoring Match:", data.loc[data["Runs"].idxmax(), "Match_ID"])

print("Total Venues:", data["Venue"].nunique())
data.to_csv("ipl_analysis_result.csv", index=False)

print("IPL analysis data saved successfully!")