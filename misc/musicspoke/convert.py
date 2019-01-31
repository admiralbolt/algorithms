# Translate our csv into a more usable form:
import pickle

with open("poll_original.csv", "r") as rh:
  lines = rh.readlines()
  dates = lines[0].strip().split(",")
  times = lines[1].strip().split(",")
  current_date = ""
  labels = []
  for i, time in enumerate(times):
    if dates[i]:
      current_date = dates[i]
    if not current_date:
      labels.append("")
      continue
    labels.append("%s %s" % (current_date, time))
  labels.pop()
  with open("labels.pickle", "wb") as wh:
    pickle.dump(labels, wh)
  # Now that we have good labels, iterate through each composer to find their
  # correct edges:
  with open("poll.csv", "w") as wh:
    wh.write("Composer,Slot\n")
    for line in lines[2:]:
      line = line.strip().split(",")
      composer = line[0]
      for i, val in enumerate(line):
        if val != "OK" or i >= len(labels):
          continue
        wh.write("%s,%s\n" % (composer, labels[i]))
