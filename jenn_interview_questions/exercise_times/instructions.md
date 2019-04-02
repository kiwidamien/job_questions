You've just been hired by Esoteric 24hr Fitness as their first data
scientist.  Your first task is to analyze a data set they collected.
The data covers a period from Jan 1st 2011 to mid-March 2011, and
contains information about what exercises people did in that
period. The data takes the format:
  time,user_id,exercise_code
  2011-01-02T08:43:00,194,strength4
  2011-01-02T08:49:00,258,strength4
  2011-01-02T09:02:00,194,strength2
  2011-01-02T09:08:30,296,cardio3
  2011-01-02T09:18:00,258,cardio1
where `time` is a timestamp that shows when an exercise *began* (we
don't know when the exercise ended), the userid is an integer that
corresponds to a gym member, and exercise_code is a label that shows
what exercise it is. No one is sure exactly which exercise a code
corresponds to (other than the strength and cardio distinction).
Using this data, see if you can answer the following questions:
  - Explore when the gym tends to be used most and least.  The
    machines need to be cleaned for ~2 hours once a week, and going
    forward the gym will shut down for those 2 hours (so in the
    future, the gym will be open only 166 hours per week).  What
    2-hour window should the gym choose for cleaning and maintenance,
    so as to be minimally disruptive to users?
  - The gym might want to replace the least popular machine.  What is
    the least popular exercise?  How confident are you that this
    answer is robust?
  - How long do members spend doing the individual exercises? (This
    will be used to help trainers plan time-efficient routines.)
    The personal trainers think that some members in this study were
    doing some exercises too quickly and had bad form. Can we identify
    which members these were, to target them for personal training
    advice?
  - The personal trainers also have the idea that some people tend to
    stick to certain exercises.  Can we find groups of exercises that
    tend to cluster together in the user base?
