import NoteTakingCombiner, NoteTakingDuplicates

path = 'Chapter_18/Lesson2'

NoteTakingCombiner.start_bad(path)
amount = NoteTakingDuplicates.start_duplicates(path)
if amount != 0:
    print('Problem')
else:
    pass
