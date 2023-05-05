import sys
import csv
import re
import yaml

path = sys.argv[1]

def parsemember(member):
  if "-" in member or ":" in member or "，" in member or "–" in member:
    match = re.split(":|-|@|–", member)
    name = match[0]
    ubit = match[1]
  elif "<" in member or "(" in member:
    match = re.match("([^<(]+)(\\(|<)([^\\)>@]+)", member)
    name = match.group(1)
    ubit = match.group(3)
  else:
    raise Exception(member)
  return {
    "name" : name.strip(),
    "email" : ubit.strip() + "@buffalo.edu"
  }

def parsegroup(group):
  members = [
    parsemember(x.strip()) 
    for x in re.split(", *|\n|;", group) 
    if x != ""
  ]
  return members

courses = {}

with open(path) as file:
  data = csv.reader(file)
  header = data.__next__()
  for row in data:
    timestamp, email, title, abstract, course, url, details, team = row
    if course not in courses:
      courses[course] = []

    record = {
      "title" : title,
      "description" : abstract,
      "team" : parsegroup(team)
    }

    if "http" in url:
      record["url"] = url

    courses[course] += [ record ]

course_list = [
  {
    "code" : name,
    "projects" : courses[name],
  }
  for name in courses
]

print(yaml.dump(course_list))

