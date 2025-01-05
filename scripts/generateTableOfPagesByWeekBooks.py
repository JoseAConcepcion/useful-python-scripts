import pandas as pd

def generate_book_table(df):
    # Table structure
    table_markdown = "| Book | Total Pages | Pages to Read per Week | Finished? |\n"
    table_markdown += "|-------|-------------|------------------------|-----------|\n"

    for index, row in df.iterrows():
        title = row['Title']
        total_pages = row['Pages']
        pages_per_week = round(total_pages / 7)
        table_markdown += f"| {title} | {total_pages} | {pages_per_week} |  |\n"

    return table_markdown

df = pd.read_csv('books.csv')
table = generate_book_table(df)

with open('book_table.md', 'w') as md_file:
    md_file.write(table)

print("\033[32mDone.")
