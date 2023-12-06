Hi, if you're here (yes, Alan, I'm talking to you), I assume you want to know how to add a new semester's demo day.

1. Create a new file in `_by_year/YYYYss.md` (e.g., copy an existing file)
   - Update the metadata in the header
   - Update sponsors as needed
2. Put image links for sponsors in `assets/images/sponsors`
3. Generate participant data by feeding the output of the google form (as a 'csv' download) and piping the output into the data directory: `python3 scripts/process_form.py path/to/download.csv > _data/YYYYss.yaml`
4. Update the default page by editing [`index.markdown`](https://github.com/UB-CSE-Demo-Day/ub-cse-demo-day.github.io/blob/main/index.markdown)


#### process_form.py

This script uses some rough heuristics to standardize things like student names and email addresses.  If it encounters something it can't process, it'll throw an exception.  Generally, I find it easiest to edit the form-generated spreadsheet to reformat the participant names column into:
```
Student Name - email@buffalo.edu,
Student Name - email@buffalo.edu,
...
```

#### website URL
https://ub-cse-demo-day.github.io/<br>
https://ub-cse-demo-day.github.io/by_year/YYYYss

#### Default URL
update index.markdown to point to the new short title
