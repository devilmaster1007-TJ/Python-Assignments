import numpy as np

arr = np.arange(1, 11)
print(&quot;Original Array:&quot;, arr)

print(&quot;\nFirst five elements:&quot;, arr[:5])
print(&quot;Elements from index 3 to 7:&quot;, arr[3:8])
print(&quot;Alternate elements:&quot;, arr[::2])
print(&quot;Array in reverse order:&quot;, arr[::-1])

print(&quot;\nSum:&quot;, np.sum(arr))
print(&quot;Mean:&quot;, np.mean(arr))
print(&quot;Maximum:&quot;, np.max(arr))
print(&quot;Minimum:&quot;, np.min(arr))

add_arr = arr + 5
print(&quot;\nArray after adding 5:&quot;, add_arr)

mul_arr = arr * 2
print(&quot;Array after multiplying by 2:&quot;, mul_arr)
