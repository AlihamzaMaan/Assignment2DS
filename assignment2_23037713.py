# %% [markdown]
# load and read
# 

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('D:\\US Stock Market Dataset.csv') 


# %% [markdown]
# function for descriptive statistics

# %%
def descriptive_stats(data):
    """
    Calculate and display descriptive statistics for a DataFrame.

    Args:
    - data (DataFrame): The input DataFrame.

    Returns:
    - None
    """
    print(data.describe())

# Usage
descriptive_stats(df)

# %% [markdown]
# making a histogram for apple stock prices

# %%
# Histogram of stock prices
plt.hist(df['Apple_Price'], bins=20)
plt.xlabel('Apple Stock Price')
plt.ylabel('Frequency')
plt.title('Histogram of Apple Stock Prices')
plt.show()



# %% [markdown]
# linr chart

# %%
plt.plot(df['Date'], df['Apple_Price'])
plt.xlabel('Date') 
plt.ylabel('Apple Stock Price')
plt.title('Apple_Price')
plt.show()

# %%
print(df['Apple_Price'].describe())

# %% [markdown]
# box plot

# %%

# Box plot
plt.boxplot(df['Apple_Price'])
plt.ylabel('Apple Stock Price')
plt.title('Box Plot of Apple Stock Prices')
plt.show() 

# Violin plot 
sns.violinplot(data=df, x='Date', y='Apple_Price')
plt.ylabel('Apple Stock Price')
plt.title('Violin Plot of Apple Stock Prices')
plt.show()


