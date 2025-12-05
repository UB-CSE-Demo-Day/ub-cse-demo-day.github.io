import sys
import csv
import re
import yaml

path = sys.argv[1]
members = []

def parsemember(member):
  if "-" in member or ":" in member or "，" in member or "–" in member:
    match = re.split(":|-|@|–", member)
    name = match[0]
    ubit = match[1]
  elif "<" in member or "(" in member:
    match = re.match("([^<(]+)(\\(|<)([^\\)>@]+)", member)
    name = match.group(1)
    ubit = match.group(3)
  elif "@" in member:
    match = re.split("@", member)
    name = match[0]
    ubit = match[0]
  else:
    raise Exception(member)

  members.append(ubit.strip() + "@buffalo.edu")
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

with open(path, encoding='utf-8', errors='ignore') as file:
  data = csv.reader(file)
  header = data.__next__()
  for row in data:
    timestamp, email, title, abstract, course, url, details, team = row
    members.append(email)
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

members = list(dict.fromkeys(members))
f = open("participants.txt", "w")
for member in members:
  f.write(member)
  f.write("\n")

f.close()

