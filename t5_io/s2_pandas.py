import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)

fixed_df = pd.read_csv(
    "bikes.csv",
    sep=",",
    encoding="utf8",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
fixed_df[:3]
