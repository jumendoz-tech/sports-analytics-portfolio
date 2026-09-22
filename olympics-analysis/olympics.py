"""
Final Portfolio Problem: Olympics

This script uses the athlete_events.csv dataset to analyze Olympic athlete
height, age, and gold medals over time.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    data_path = "athlete_events.csv"

    olympics = pd.read_csv(data_path)

    print("Olympics dataset")
    print("----------------")
    print(olympics.head())

    print("\nDataset shape:")
    print(olympics.shape)

    print("\nColumn names:")
    print(olympics.columns)

    print("\nMissing values:")
    print(olympics.isna().sum())

    # Drop columns that have fewer than 5 non-null values.
    olympics_clean = olympics.dropna(axis=1, thresh=5)

    print("\nColumns after dropping columns with fewer than 5 non-null values:")
    print(olympics_clean.columns)

    # Separate data by season and sex.
    summer = olympics_clean[olympics_clean["Season"] == "Summer"]
    winter = olympics_clean[olympics_clean["Season"] == "Winter"]

    female_summer = summer[summer["Sex"] == "F"]
    male_summer = summer[summer["Sex"] == "M"]

    female_winter = winter[winter["Sex"] == "F"]
    male_winter = winter[winter["Sex"] == "M"]

    # Mean height tables.
    female_summer_height = (
        female_summer
        .groupby(["Year", "Event"])["Height"]
        .mean()
        .reset_index()
        .sort_values(["Event", "Year"])
    )

    female_winter_height = (
        female_winter
        .groupby(["Year", "Event"])["Height"]
        .mean()
        .reset_index()
        .sort_values(["Event", "Year"])
    )

    male_summer_height = (
        male_summer
        .groupby(["Year", "Event"])["Height"]
        .mean()
        .reset_index()
        .sort_values(["Event", "Year"])
    )

    male_winter_height = (
        male_winter
        .groupby(["Year", "Event"])["Height"]
        .mean()
        .reset_index()
        .sort_values(["Event", "Year"])
    )

    print("\nMean height of female athletes in Summer Games:")
    print(female_summer_height.head(20))

    print("\nMean height of female athletes in Winter Games:")
    print(female_winter_height.head(20))

    print("\nMean height of male athletes in Summer Games:")
    print(male_summer_height.head(20))

    print("\nMean height of male athletes in Winter Games:")
    print(male_winter_height.head(20))

    # Find events with highest variance in mean height over time.
    female_summer_variance = (
        female_summer_height
        .groupby("Event")["Height"]
        .var()
        .dropna()
        .sort_values(ascending=False)
    )

    male_summer_variance = (
        male_summer_height
        .groupby("Event")["Height"]
        .var()
        .dropna()
        .sort_values(ascending=False)
    )

    female_winter_variance = (
        female_winter_height
        .groupby("Event")["Height"]
        .var()
        .dropna()
        .sort_values(ascending=False)
    )

    male_winter_variance = (
        male_winter_height
        .groupby("Event")["Height"]
        .var()
        .dropna()
        .sort_values(ascending=False)
    )

    print("\nFemale Summer events with highest variance in mean height:")
    print(female_summer_variance.head(10))

    print("\nMale Summer events with highest variance in mean height:")
    print(male_summer_variance.head(10))

    print("\nFemale Winter events with highest variance in mean height:")
    print(female_winter_variance.head(10))

    print("\nMale Winter events with highest variance in mean height:")
    print(male_winter_variance.head(10))

    # Plot mean height over time for interesting events.
    interesting_events = [
        "Basketball Women's Basketball",
        "Volleyball Women's Volleyball",
        "Gymnastics Women's Individual All-Around",
        "Basketball Men's Basketball",
        "Swimming Men's 100 metres Freestyle",
    ]

    for event in interesting_events:
        event_data = olympics_clean[olympics_clean["Event"] == event]

        if event_data.empty:
            continue

        event_height = (
            event_data
            .groupby("Year")["Height"]
            .mean()
            .reset_index()
        )

        plt.figure()
        plt.plot(event_height["Year"], event_height["Height"], marker="o")
        plt.title(f"Mean Height Over Time: {event}")
        plt.xlabel("Year")
        plt.ylabel("Mean Height")
        plt.xticks(rotation=45)
        plt.tight_layout()

        safe_event_name = (
            event.lower()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("'", "")
        )

        plt.savefig(f"{safe_event_name}_height_over_time.png")
        plt.close()

    print("\nStory about height trends:")
    print(
        "The events with the highest variance in mean height changed the most over time. "
        "This may happen because the sport became more specialized, because different "
        "countries became more competitive, or because training and athlete selection "
        "changed over time. Sports such as basketball and volleyball may show taller "
        "average heights because height gives athletes an advantage. Some events may "
        "stay more stable because body size is less directly connected to performance."
    )

    # Gold medal table by country and year.
    gold_medals = olympics_clean[olympics_clean["Medal"] == "Gold"]

    gold_medals_by_country_year = (
        gold_medals
        .groupby(["NOC", "Year"])
        .size()
        .reset_index(name="gold_medals")
        .sort_values(["NOC", "Year"])
    )

    print("\nGold medals by country and year:")
    print(gold_medals_by_country_year.head(30))

    # Average age of athletes per year per country.
    average_age_by_country_year = (
        olympics_clean
        .groupby(["NOC", "Year"])["Age"]
        .mean()
        .reset_index(name="average_age")
        .sort_values(["NOC", "Year"])
    )

    print("\nAverage age of athletes by country and year:")
    print(average_age_by_country_year.head(30))

    # Plot average age of athletes for each games over time.
    average_age_by_games = (
        olympics_clean
        .groupby(["Year", "Season"])["Age"]
        .mean()
        .reset_index(name="average_age")
        .sort_values(["Season", "Year"])
    )

    print("\nAverage age by Olympic Games:")
    print(average_age_by_games.head(30))

    plt.figure()

    for season in average_age_by_games["Season"].unique():
        season_data = average_age_by_games[average_age_by_games["Season"] == season]
        plt.plot(
            season_data["Year"],
            season_data["average_age"],
            marker="o",
            label=season,
        )

    plt.title("Average Age of Olympic Athletes Over Time")
    plt.xlabel("Year")
    plt.ylabel("Average Age")
    plt.legend()
    plt.tight_layout()
    plt.savefig("average_age_olympics_over_time.png")
    plt.close()

    print("\nThe average age plot was saved as:")
    print("average_age_olympics_over_time.png")


if __name__ == "__main__":
    main()
