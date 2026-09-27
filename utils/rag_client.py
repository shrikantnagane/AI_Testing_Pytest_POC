class RAGClient:
    def retrieve(self, question):
        # Placeholder for retrieval logic
        # In a real implementation, this would query a knowledge base or database
        # For demonstration, we return a static context and facts
        context = """
            regression testing is testing performed to ensure that recent code changes, bug fixes, or 
            updates haven't accidentally broken existing functionality that was previously working. 
            Regression testing is a type of software testing that verifies that previously developed and tested software still performs correctly after it was changed or interfaced with other software. 
            The intent of regression testing is to catch bugs that may have been inadvertently introduced into existing areas of a system as a result of new code changes. It is an essential part of the software development process, especially in agile and continuous integration environments where code changes are frequent."""
                    
        facts = [
                "regression testing",
                "testing performed to ensure that recent code changes, bug fixes",
                "updates haven't accidentally broken existing functionality"
            ]
        
        return context, facts
        