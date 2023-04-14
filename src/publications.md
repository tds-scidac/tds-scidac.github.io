# Publications

{% set years = ['2023', '2022', '2021', '2020', '2019', '2018'] %}

{% for year in years %}
## {{ year }}
{{ parse_bibtex("src/publications.bib", year) }}
----
{% endfor %}
