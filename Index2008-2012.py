import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

            # Indeks Harga Saham Gabungan / Jakarta Composite Index
                                # YoY 2008-2012

# Data for Composite Index
     #     Q1        Q2        Q3         Q4
ci12 = [2447.299, 2349.105, 1832.507, 1355.408, 
        1434.074, 2026.780, 2467.591, 2534.356,
        2777.301, 2913.684, 3501.296, 3703.512,
        3678.674, 3888.569, 3549.032, 3821.992,
        4121.551, 3955.577, 4262.561, 4316.687]

# Year / Period(s)
    # X-Axis
yq12 = ['2008\nQ1', '2008\nQ2', '2008\nQ3', '2008\nQ4',
        '2009\nQ1', '2009\nQ2', '2009\nQ3', '2009\nQ4',
        '2010\nQ1', '2010\nQ2', '2010\nQ3', '2010\nQ4',
        '2011\nQ1', '2011\nQ2', '2011\nQ3', '2011\nQ4',
        '2012\nQ1', '2012\nQ2', '2012\nQ3', '2012\nQ4']
    #
# Merge Datasets into Dataframe
a_df = {'ci12': ci12, 'yq12': yq12}
alpha = pd.DataFrame(a_df)

# Axis for Beban Pengembangan Usaha
fig, ax1 = plt.subplots(figsize = (10,6))
plt.ylim(1000, 4600)
color = 'Teal'
ax1.set_title('Perkembangan Indeks Harga Saham Gabungan (IHSG) \n 2008-2012', fontsize = 15, pad = 15)
ax1.set_xlabel('Periode', fontsize = 13)
ax1.set_ylabel('Indeks', fontsize = 13)
ax2 = sns.lineplot(x = 'yq12', y = 'ci12', data = alpha, sort = False, marker = 'd', color = color)
ax1.tick_params(axis = 'y')

# Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Checkout
plt.show()