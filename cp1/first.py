import survey

def livebirths(table):
  livebirths = 0

  for each in table.records:
    thisoutcome = each.outcome

    if thisoutcome != "N/A" and thisoutcome == 1:
      livebirths += 1

  return livebirths

def livebirthsfirst(table):
  """
  Displays live births in two groups, one of first babies and one of others.
  """

  firstbirths = 0
  otherbirths = 0

  for each in table.records:
    thisoutcome = each.outcome
    thisorder = each.birthord

    if thisoutcome != "N/A" and thisoutcome == 1 and thisorder == 1:
      firstbirths += 1

    elif thisoutcome != "N/A" and thisoutcome == 1 and thisorder!= 1:
      otherbirths += 1

    else:
      # Record was N/A
      pass

  return (firstbirths, otherbirths)

def average_pregnancy_length_ord(table, birthord):
  """
  Computes the average pregnancy length in weeks for live births.
  Specify a particular birth order to be calculated.
  """

  pregnancy_lengths = []

  for each in table.records:
    thisoutcome = each.outcome
    thisorder = each.birthord
    thisprglength = each.prglength

    if thisoutcome != "N/A" and thisoutcome == 1 and thisorder == birthord and thisprglength in range(0, 51):
      pregnancy_lengths.append(thisprglength)

  return sum(pregnancy_lengths) / float(len(pregnancy_lengths))

def average_pregnancy_length_other(table):
  """
  Computes the average pregnancy length in weeks for non-first live births.
  """

  pregnancy_lengths = []

  for each in table.records:
    thisoutcome = each.outcome
    thisorder = each.birthord
    thisprglength = each.prglength

    if thisoutcome != "N/A" and thisoutcome == 1 and thisorder != 1 and thisprglength in range(0, 51):
      pregnancy_lengths.append(thisprglength)

  return sum(pregnancy_lengths) / float(len(pregnancy_lengths))


def main():
  table = survey.Pregnancies()
  table.ReadRecords()
  print 'Number of pregnancies', len(table.records)
  print 'Number of live births', livebirths(table)
  print 'Number of first births is %i and other births is %i' % (livebirthsfirst(table))
  print 'Average pregnancy length for first births: %f' % average_pregnancy_length_ord(table, 1)
  print 'Average pregnancy length for other births: %f' % average_pregnancy_length_other(table)

if __name__ == '__main__':
    main()