# Design Facebook Photo Tagging [Solution_Walkthrough]

Design a feature that reduces the effort of tagging people in photos when a user uploads a photo to Facebook.

Many systems design questions are intentionally left very vague and are literally given in the form of `Design Foobar`. It's your job to ask clarifying questions to better understand the system that you have to build.

We've laid out some of these questions below; their answers should give you some guidance on the problem. Before looking at them, we encourage you to take few minutes to think about what questions you'd ask in a real interview.

# Clarifying Questions To Ask

# [Question_1]
Q: When you say reduce the effort of tagging people in photos upon upload, do you mean automatically tagging or just presenting suggestions on which users should be tagged in the photo?

A: Let's present a list of suggestions.

# [Question_2]
Q: Will these suggestions be in a dropdown menu, perhaps appearing when a user clicks on a face?

A: Yes, there should be a box surrounding people's faces in photos such that when uploading the photo, users have the chance to click the boxes and tag a user.

# [Question_3]
Q: Do I need to design the ingestion of these photos into some analysis system?

A: Assume that the photos you have access to come into an HDFS cluster from a batch ingestion each day.

# [Question_4]
Q: Do I have to design the system which serves the tag suggestions, or just the model(s)?

A: Let's not focus on serving the predictions.

# [Question_5]
Q: Okay, do I need to design the ingestion of these photos into some analytics system?

A: Assume that the photos you have access to come into an HDFS cluster from a batch ingestion each day from our PostgreSQL cluster.

# [Question_6]
Q: Can I assume that these images are in HDF5 format under 30MB with dimensions under 1500x1500?

A: Yes, that's fine.

# [Question_7]
Q: Can I use pre-trained models?

A: Yes, but you have to explain how you'd train and use them, and how they work.

# [Question_8]
Q: Can I assume that we have access to a workforce which can label images?

A: Yes, but go into detail on how you'd use this workforce to label images.

# [Question_9]
Q: Can I assume that we only need to detect frontal faces, no occlusions, and no severe illumination problems?

A: To start out with, yes. At the end of the interview, we'll revisit this.

# [Question_10]
Q: Will we want to detect faces from various distances away from the camera lens?

A: Yes, you should design a system which support multiple scales of faces.

# [Question_11]
Q: I'm assuming that we want to be able to detect more than one face per image?

A: Yes. That's right.
