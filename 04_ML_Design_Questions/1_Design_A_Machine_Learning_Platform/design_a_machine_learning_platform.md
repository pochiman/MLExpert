# Design A Machine Learning Platform

  Design a machine learning platform to support some arbitrary big tech company
  like Google or Amazon.

  Many systems design questions are intentionally left very vague and are literally given in the form of `Design Foobar`. It's your job to ask clarifying questions to better understand the system that you have to build.

  We've laid out some of these questions below; their answers should give you some guidance on the problem. Before looking at them, we encourage you to take few minutes to think about what questions you'd ask in a real interview.

# Clarifying Questions To Ask

# [Question_1]

  Q: Are we building this mainly for a website and/or app that millions of users interact with daily?

  A: Yes, there's a website and a corresponding mobile version that millions of people visit every day.

# [Question_2]

  Q: I'm assuming that we'll be supporting dozens of teams, tens of thousands of features, and potentially hundreds of models. Is that a correct assumption?

  A: Yes, that's the right scale.

# [Question_3]

  Q: Do we have access to a data lake of all the clickstreams and logs required to create relevant features?

  A: Yes, there's an HDFS data lake.

# [Question_4]

  Q: Is the data that we need to process on the order of petabytes?

  A: Yes, it is.

# [Question_5]

  Q: Along with that sized data, is there also the need for thousands of daily data jobs to create the tens of thousands of features and labels?

  A: Yes, that's reasonable.

# [Question_6]

  Q: Does the platform need to support deep learning models?

  A: For now, we'll stick to basic models.
