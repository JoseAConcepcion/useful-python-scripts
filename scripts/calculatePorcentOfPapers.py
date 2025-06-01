import re
from collections import defaultdict
from datetime import datetime

def analyze_text_with_time(text):
    pattern = r'(\d{4})' #most modify depending on your references
    occurrences = re.findall(pattern, text)
    
    counter = defaultdict(int)
    current_year = datetime.now().year
    
    for year_str in occurrences:
        try:
            year = int(year_str)
            counter[year_str] += 1
        except ValueError:
            continue
    
    total_occurrences = sum(counter.values()) if counter else 1
    
    percentages = {
        year: (count / total_occurrences) * 100 
        for year, count in counter.items()
    }
    
    #last 5, 10 and 20 years percent
    years_5 = [y for y in counter.keys() if current_year - int(y) <= 5]
    years_10 = [y for y in counter.keys() if current_year - int(y) <= 10]
    years_20 = [y for y in counter.keys() if current_year - int(y) <= 20]
    
    sum_5 = sum(counter[y] for y in years_5)
    sum_10 = sum(counter[y] for y in years_10)
    sum_20 = sum(counter[y] for y in years_20)
    
    percent_5 = (sum_5 / total_occurrences) * 100 if total_occurrences else 0
    percent_10 = (sum_10 / total_occurrences) * 100 if total_occurrences else 0
    percent_20 = (sum_20 / total_occurrences) * 100 if total_occurrences else 0
    
    return {
        "counter": dict(counter),
        "percentages": percentages,
        "last_5_years_percent": percent_5,
        "last_10_years_percent": percent_10,
        "last_20_years_percent": percent_20,
    }

text = """
Lorem ipsum et al. 1990 
"""

result = analyze_text_with_time(text)

# print("Occurrence counter:", result["counter"])
print("General percentages:", result["percentages"])
print("Last 5 years (%):", result["last_5_years_percent"])
print("Last 10 years (%):", result["last_10_years_percent"])
print("Last 20 years (%):", result["last_20_years_percent"])
