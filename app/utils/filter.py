def filter_by_specialty(df, query):

    query = query.lower()

    return df[df["specialties"].str.lower().str.contains(query, na=False)]