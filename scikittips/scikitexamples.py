from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from get_data import get_all_data

# scikitlearn tip #1 


df = get_all_data()
df.head()


ohe = OneHotEncoder()
imp = SimpleImputer()

ct = make_column_transformer(
    (ohe, ['imS']),
    (imp, ['imL']),
    remainder='passthrough'
)

new_matrix = ct.fit_transform(df)


# scikitlearn tip #2
ct2 = make_column_transformer((ohe, ['imS']))
new_matyrix_2 = ct2.fit_transform(df)

new_matyrix_2.shape
