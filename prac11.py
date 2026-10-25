import pandas as pd
import numpy as np

np.random.seed(42)
numbers = np.random.randint(1, 100, 10)

s = pd.Series(numbers)
print(&quot;Original Series:&quot;)
print(s)

print(&quot;\nElement at index 3:&quot;, s[3])
print(&quot;First five elements:&quot;)
print(s[:5])

print(&quot;\nNumbers greater than 50:&quot;)
print(s[s &gt; 50])

print(&quot;\nMean:&quot;, s.mean())
print(&quot;Median:&quot;, s.median())
print(&quot;Minimum:&quot;, s.min())
print(&quot;Maximum:&quot;, s.max())
