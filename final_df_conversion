from csv import writer
with open('final_df_amazon', 'w', newline= '', encoding = 'utf8') as f:
    header = ["Title", "Rating", "Body", "Char_Count", "Word_Count", "Polarity", "Subjectivity"]
    my_writer = writer(f)
    my_writer.writerow(header)
    for i in range(len(final_df)):
        my_writer.writerow(final_df.iloc[i])
