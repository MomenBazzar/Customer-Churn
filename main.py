import pandas as pd
import matplotlib.pyplot as plt

# Load the customer churn dataset
df = pd.read_csv("Customer Churn.csv")

# Group the data by age group and plot a histogram for each group
for i, (age_group, group_df) in enumerate(df.groupby("Age Group")):
    group_df["Churn"].hist(label=age_group)
    # Add a legend to the plot
    plt.legend()
    plt.xlabel("Churn")
    plt.ylabel("Count")
    # Save the plot as an image
    plt.savefig(f"output_{i}.png", dpi=72, bbox_inches="tight")
    plt.clf()
