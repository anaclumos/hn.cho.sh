import os
import frontmatter
from babel.dates import format_date
from datetime import datetime

all_files = os.listdir("legacy/pages")

for file in all_files:
    if os.path.isdir("legacy/pages/" + file):
        for subfile in os.listdir("legacy/pages/" + file):
            all_files.append(file + "/" + subfile)

for file in all_files:
    if os.path.isdir("legacy/pages/" + file):
        continue
    if not file.endswith(".mdx"):
        continue
    with open("legacy/pages/" + file, "r") as f:
        lines = f.readlines()
        post = frontmatter.load(f)
        if post.metadata:
            continue
        else:
            date = file.split(".")[0]
            if len(date.split("/")) != 3:
                print(
                    "File "
                    + file
                    + " has no frontmatter, but the date is not in YYYY/MM/DD format"
                )
                continue
            locale = file.split(".")[1]
            day = datetime.strptime(date, "%Y/%m/%d")
            subtitle = format_date(day, format="long", locale=locale)
            title = ""
            for i, line in enumerate(lines):
                if line.startswith("###"):
                    title = line.replace("###", "").strip()
                    break
            # write frontmatter
            # if file already has frontmatter, skip
            if lines[0].startswith("---"):
                continue
            title = title.split("](")[0]
            title = title.replace("[", "")
            post.metadata["top_news"] = title
            post.metadata["localized_date"] = subtitle
            with open("legacy/pages/" + file, "w") as f:
                f.write(frontmatter.dumps(post) + "\n\n" + "".join(lines))
            print("File " + file + ", added title and subtitle")
