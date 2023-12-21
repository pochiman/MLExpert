# Design Amazon Alexa

Alexa is Amazon's custom-built voice assistant.

Many systems design questions are intentionally left very vague and are literally given in the form of `Design Foobar`. It's your job to ask clarifying questions to better understand the system that you have to build.

We've laid out some of these questions below; their answers should give you some guidance on the problem. Before looking at them, we encourage you to take few minutes to think about what questions you'd ask in a real interview.

# Clarifying Questions To Ask

# [Question_1]
Q: How will users interact with Alexa?

A: Users will interact with Alexa through an Amazon Echo Dot, which is a small device that can be placed on any surface, like a table or a countertop.

# [Question_2]
Q: Will users initilize an interaction with a wake word? If so, do I need to implement that?

A: Yes, you'll need to implement wake-word detection. The wake word will be "Alexa", though the exact word shouldn't matter much for this exercise.

# [Question_3]
Q: Can I assume that only a single user will be speaking at once in a relatively quiet room?

A: Yes.

# [Question_4]
Q: Should Alexa be able to handle multiple languages?

A: No. A single language is okay.

# [Question_5]
Q: Can I assume that the user is a native english speaker?

A: Yes, that's fine for this interview.

# [Question_6]
Q: What capabilities do we need to support as a voice assistant?

A: For now, let's assume that we have about a dozen "skills" that can be called on (e.g., asking for the weather forecast,ordering food, fetching a ride, playing a song, etc.).

# [Question_7]
Q: Do any of the skills require speaker recognition? For example, should Alexa behave differently depending on who's asking a question?

A: For now, let's assume that the skills don't require speaker recognition.
