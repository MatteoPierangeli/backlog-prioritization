#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a list to store the issues
backlog = []

while True:
    # Ask for the feature name (Type 'finished' to exit)
    feature_name = input("Feature name (Type 'finished' to exit): ")
    
    if feature_name.lower() == "finished":
        break

    # Ask for Business Value on a scale from 1 to 5
    business_value = int(input("Business Value (from 1 to 5): "))

    # Ask for Urgency on a scale from 1 to 5
    urgency = int(input("Urgency (from 1 to 5): "))

    # Ask for Opportunity Enablement on a scale from 1 to 5
    opportunity_enablement = int(input("Opportunity Enablement (from 1 to 5): "))

    # Ask for Development Effort on a scale from 1 to 5
    development_effort = int(input("Development Effort (from 1 to 5): "))

    # Calculate WSJF
    wsjf = (business_value + urgency + opportunity_enablement) / development_effort

    # Add the information to the list of issues
    backlog.append((feature_name, business_value, urgency, opportunity_enablement, development_effort, wsjf))

# Sort the issues by WSJF in descending order
sorted_backlog = sorted(backlog, key=lambda x: x[5], reverse=True)

# Print the sorted table
print("\nPrioritized Backlog (based on WSJF):")
print("{:<20} {:<15} {:<10} {:<20} {:<15} {:<10}".format("Feature Name", "Business Value", "Urgency", "Opportunity Enablement", "Development Effort", "WSJF"))
for issue in sorted_backlog:
    print("{:<20} {:<15} {:<10} {:<20} {:<15} {:<10}".format(*issue))


# In[ ]:




