# Design A Fake News Detector

Design a system to detect fake news.

Many systems design questions are intentionally left very vague and are literally given in the form of `Design Foobar`. It's your job to ask clarifying questions to better understand the system that you have to build.

We've laid out some of these questions below; their answers should give you some guidance on the problem. Before looking at them, we encourage you to take few minutes to think about what questions you'd ask in a real interview.

# Clarifying Questions To Ask

# [Question_1]
Q: How are we defining fake news?

A: Let's define fake news as news articles that contain intentionally misleading info from what appears to be a reliable source.

# [Question_2]
Q: Who are we designing the system for?

A: Social media platforms. They're our primary customers.

# [Question_3]
Q: Why are these social media platforms paying us?

A: Our service aims to limit the negative financial, health, and social impacts of misinformation on the platforms.

# [Question_4]
Q: For clarification, is this a reasonable way that one of these platforms would use our service: they call our service with a news article that's been posted on their platform, and depending on our response, they have logic around allowing the post, limiting exposure of the post, or disallowing the post?

A: Yes, that sounds reasonable, but our service doesn't tell the platform how they should handle unreliable news articles. In other words, you shouldn't be concerned with that.

# [Question_5]
Q: What do our clients expect us to provide to them through our service?

A: Our platform returns a response of either 'reliable' or 'unreliable' depending on the provided news article.

# [Question_6]
Q: I'm assuming that we need to be able to explain why our service returns 'reliable' or 'unreliable'. Is this reasonable?

A: Yes, being able to explain our decision is important to both the model development and our clients if they have an inquiry.

# [Question_7]
Q: How will these social media platforms interact with our service?

A: Our service is API-based.

# [Question_8]
Q: Do clients call our service with the raw text of articles?

A: They can, but they can also just send us the URL of a news article.

# [Question_9]
Q: Do we have to implement a way to extract articles from provided URLs, or can we assume that we're provided with that functionality?

A: Yes, we have to implement that extraction.

# [Question_10]
Q: Do clients expect higher latencies if they send us just the URL of an article?

A: Yes, and we can also reject requests when we can't extract an article from the provided URL.

# [Question_11]
Q: Do we allow clients to bring their own models or data for our system to operate with?

A: No, we only use our proprietary models and data.

# [Question_12]
Q: Do we need to build an ML platform supporting dozens of scientists to rapidly iterate our model development?

A: No, I'm more concerned with how your system handles data and hosts a single model.
