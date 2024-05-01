import TFIDF

corpus = [
"Love is like pi – natural, irrational, and very important.",
"Love is being stupid together.",
"Love is sharing your popcorn.",
"Love is like Heaven, but it can hurt like Hell."
]

obj = TFIDF(corpus)
obj.preprocessing_text()

tf = obj.tf()

df = obj.df(tf)

idf, idf_d = obj.idf(df)

tfidf = obj.tfidf(tf, idf)

df = pd.DataFrame(np.round(tfidf,2), columns= list(tf.columns))
sorted_column_df = df.sort_index(axis=1)
sorted_column_df

