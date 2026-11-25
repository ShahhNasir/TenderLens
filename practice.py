# Create an empty list to store tender records
tenders = []


# Create the first tender
machine_learning_tender = {
    "title": "Machine Learning Prediction Platform",
    "organisation": "State Digital Services",
    "reference": "SDS/ML/2026/77",
    "category": "Machine Learning",
    "estimated_value": 3500000
}


# Add the first tender to our list
tenders.append(machine_learning_tender)


# Create our fictional IT tender
cloud_tender = {
    "title": "Cloud Infrastructure Modernization",
    "organisation": "National Technology Solutions",
    "reference": "NTS/CLOUD/2026/31",
    "category": "Cloud Computing",
    "estimated_value": 4800000
}


# Add the second tender to our list
tenders.append(cloud_tender)


# Print information about the first tender
print("Tender 1")
print("Title:", tenders[0]["title"])
print("Category:", tenders[0]["category"])
print("Estimated Value:", tenders[0]["estimated_value"])


# Print information about the second tender
print("\nTender 2")
print("Title:", tenders[1]["title"])
print("Category:", tenders[1]["category"])
print("Estimated Value:", tenders[1]["estimated_value"])


Artificail_intelligence_tender = {
    "title": "Reinforcement Learning Agent",
    "organisation": "National Technology Solutions",
    "reference": "NTS/AIML/2026/01",
    "Category": "AIML",
    "estimated_value": 2300000
}

tenders.append(Artificail_intelligence_tender)

tenders[0]["estimated_value"] = 400000

print("\n")
print("*"*50)
print(tenders)
