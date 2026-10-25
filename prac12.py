import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a sample customer churn dataset
np.random.seed(42)

n = 200

df = pd.DataFrame({
&quot;CustomerID&quot;: range(1, n + 1),
&quot;Age&quot;: np.random.randint(18, 70, n),
&quot;Tenure&quot;: np.random.randint(1, 72, n),
&quot;MonthlyCharges&quot;: np.random.uniform(20, 120, n).round(2),
&quot;TotalCharges&quot;: np.random.uniform(100, 8000, n).round(2),
&quot;Contract&quot;: np.random.choice([&quot;Month-to-month&quot;, &quot;One year&quot;, &quot;Two year&quot;], n),
&quot;InternetService&quot;: np.random.choice([&quot;DSL&quot;, &quot;Fiber optic&quot;, &quot;No&quot;], n),

&quot;Churn&quot;: np.random.choice([&quot;Yes&quot;, &quot;No&quot;], n, p=[0.30, 0.70])
})

# Introduce missing values for demonstration
df.loc[[5, 15, 25, 35], &quot;Age&quot;] = np.nan
df.loc[[10, 20, 30], &quot;MonthlyCharges&quot;] = np.nan
df.loc[[12, 22], &quot;Contract&quot;] = np.nan

print(&quot;Original Dataset:&quot;)
print(df.head())

# 2. Explore dataset structure
print(&quot;\nDataset Shape:&quot;)
print(df.shape)

print(&quot;\nDataset Information:&quot;)
df.info()

print(&quot;\nColumn Names:&quot;)
print(df.columns.tolist())

# 3. Check duplicate records
print(&quot;\nDuplicate Records:&quot;)
print(df.duplicated().sum())

df = df.drop_duplicates()

# 4. Identify missing values
print(&quot;\nMissing Values:&quot;)
print(df.isnull().sum())

print(&quot;\nMissing Value Percentage:&quot;)
print((df.isnull().mean() * 100).round(2))

# 5. Handle missing values
# Fill numerical columns with median
numeric_cols = df.select_dtypes(
include=np.number
).columns

for col in numeric_cols:
df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(
include=&quot;object&quot;
).columns

for col in categorical_cols:
if df[col].isnull().any():
df[col] = df[col].fillna(df[col].mode()[0])

print(&quot;\nMissing Values After Cleaning:&quot;)
print(df.isnull().sum())

# 6. Generate summary statistics
print(&quot;\nNumerical Summary:&quot;)
print(df.describe().round(2))

print(&quot;\nCategorical Summary:&quot;)
print(df.describe(include=&quot;object&quot;))

# 7. Calculate churn rate
churn_rate = (
df[&quot;Churn&quot;].eq(&quot;Yes&quot;).mean() * 100
)

print(&quot;\nOverall Churn Rate:&quot;)
print(round(churn_rate, 2), &quot;%&quot;)

# 8. Analyze churn by contract
print(&quot;\nChurn by Contract:&quot;)
contract_churn = pd.crosstab(
df[&quot;Contract&quot;],
df[&quot;Churn&quot;],
normalize=&quot;index&quot;
) * 100

print(contract_churn.round(2))

# 9. Analyze churn by internet service
print(&quot;\nChurn by Internet Service:&quot;)
service_churn = pd.crosstab(
df[&quot;InternetService&quot;],

df[&quot;Churn&quot;],
normalize=&quot;index&quot;
) * 100

print(service_churn.round(2))

# 10. Compare numerical features by churn
print(&quot;\nAverage Customer Details by Churn:&quot;)
print(
df.groupby(&quot;Churn&quot;)[
[&quot;Age&quot;, &quot;Tenure&quot;, &quot;MonthlyCharges&quot;, &quot;TotalCharges&quot;]
].mean().round(2)
)

# 11. Visualization 1: Churn distribution
sns.countplot(data=df, x=&quot;Churn&quot;)
plt.title(&quot;Customer Churn Distribution&quot;)
plt.xlabel(&quot;Churn&quot;)
plt.ylabel(&quot;Number of Customers&quot;)
plt.tight_layout()
plt.show()

# 12. Visualization 2: Churn by contract
sns.countplot(
data=df,
x=&quot;Contract&quot;,
hue=&quot;Churn&quot;
)
plt.title(&quot;Customer Churn by Contract&quot;)

plt.xlabel(&quot;Contract Type&quot;)
plt.ylabel(&quot;Number of Customers&quot;)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 13. Visualization 3: Tenure and churn
sns.boxplot(
data=df,
x=&quot;Churn&quot;,
y=&quot;Tenure&quot;
)
plt.title(&quot;Tenure Distribution by Churn&quot;)
plt.xlabel(&quot;Churn&quot;)
plt.ylabel(&quot;Tenure (Months)&quot;)
plt.tight_layout()
plt.show()

# 14. Visualization 4: Monthly charges and churn
sns.boxplot(
data=df,
x=&quot;Churn&quot;,
y=&quot;MonthlyCharges&quot;
)
plt.title(&quot;Monthly Charges by Churn&quot;)
plt.xlabel(&quot;Churn&quot;)
plt.ylabel(&quot;Monthly Charges&quot;)
plt.tight_layout()
plt.show()

# 15. Visualization 5: Correlation heatmap
corr = df[
[&quot;Age&quot;, &quot;Tenure&quot;, &quot;MonthlyCharges&quot;, &quot;TotalCharges&quot;]
].corr()

sns.heatmap(
corr,
annot=True,
cmap=&quot;coolwarm&quot;,
fmt=&quot;.2f&quot;
)
plt.title(&quot;Correlation Heatmap&quot;)
plt.tight_layout()
plt.show()

# 16. Identify patterns
print(&quot;\nPattern Analysis:&quot;)

print(&quot;\nChurn rate by contract:&quot;)
print(
df.assign(
ChurnFlag=df[&quot;Churn&quot;].eq(&quot;Yes&quot;)
).groupby(&quot;Contract&quot;)[&quot;ChurnFlag&quot;].mean()
.mul(100).round(2)
)

print(&quot;\nAverage tenure by churn:&quot;)
print(df.groupby(&quot;Churn&quot;)[&quot;Tenure&quot;].mean().round(2))

print(&quot;\nAverage monthly charges by churn:&quot;)
print(
df.groupby(&quot;Churn&quot;)[&quot;MonthlyCharges&quot;]
.mean().round(2)
)

# 17. Save cleaned dataset
df.to_csv(&quot;cleaned_customer_churn.csv&quot;, index=False)

print(&quot;\nCleaned dataset saved successfully.&quot;)
