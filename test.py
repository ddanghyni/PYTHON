#%%[1] 구구단 출력 예제

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")


#%%[2] plot 출력 예제
'''
아오~
'''
import numpy as np
from lets_plot import *

# Generate random data-points for the demo.
np.random.seed(12)
data = dict(
    cond=np.repeat(['A', 'B'], 200),
    rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
)
#Create plot specification.
p = ggplot(data, aes(x='rating', fill='cond')) + ggsize(500, 250) \
    + geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq')

# Display plot in 'SciView'.
p.show()


#%%



