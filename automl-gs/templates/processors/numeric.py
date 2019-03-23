    # {{ field_raw }}
    {% if params['numeric_strat'] in ['minmax', 'standard'] %}
    {{ field }}_enc = encoders['{{ field }}_encoder'].transform(df['{{ field_raw }}'].values.reshape(-1, 1))
    {% endif %}
    {% if params['numeric_strat'] in ['quantiles', 'percentiles'] %}
    {{ field }}_enc = pd.cut(df['{{ field_raw }}'].values, encoders['{{ field }}_bins'], labels=False, include_lowest=True)
    {{ field }}_enc = encoders['{{ field }}_encoder'].transform({{ field }}_enc)
    {% endif %}