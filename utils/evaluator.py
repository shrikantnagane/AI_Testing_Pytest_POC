class Evaluator:

    def calculate_relevance(self, question, response):

        keywords = [
            "regression testing",
            "existing functionality",
            "software testing",
            "bug fixes",
            "new features"
        ]

        matched = 0

        for keyword in keywords:
            if keyword.lower() in response.lower():
                matched = matched + 1
            else:
                print(f"Keyword '{keyword}' not found in response.")

        return matched / len(keywords)

    def calculate_groundedness(self, response, context, facts):
        
        matched = 0

        for fact in facts:
            if fact.lower() in response.lower() and fact.lower() in context.lower():
                matched = matched + 1

        return matched / len(facts) 
        
    def calculate_hallucination(self, response, context, facts):
        hallucinated = 0

        for fact in facts:
            if fact.lower() not in response.lower() and fact.lower() not in context.lower():
                hallucinated = hallucinated + 1

        return hallucinated / len(facts)