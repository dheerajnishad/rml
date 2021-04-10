# rml
create a Customer Support Application using Django:



Customer Enquiry
-> The customer visits the url and fills his name, phone number, email id and query.
-> upon submission a mail must be triggered to the service provider's predefined email id (Ex: abc@gmail.com) and enquiry must be stored in the database.

Image description:
![Capture3](https://user-images.githubusercontent.com/43162312/114266903-a4d03a80-9a16-11eb-9101-d2f34041275c.JPG)

Service Provider Feedback
-> Service provider receives the mail notification and mail has the url that takes him to the customer enquiry page displaying enquiry details.
-> The page must have a response text box field which the service provider fills in and submits and upon submitting the customer receives the mail containing the response from the service provider.

Image description: Mail send to service Provider:

![Capture](https://user-images.githubusercontent.com/43162312/114266975-fb3d7900-9a16-11eb-9f4e-0dfbede6a39a.JPG)

Image description:When open url on mail:
![Capture1](https://user-images.githubusercontent.com/43162312/114267030-2e800800-9a17-11eb-88e2-bd0edeb27dd1.JPG)

Customer Review
-> The customer must get a mail notification after 60 minutes containing the url to the customer satisfaction page, the page must ask if the user is (satisfied or unsatisfied). 
-> upon submission must capture user satisfaction against the enquiry made by the customer.
-> The url sent to the customer over mail must expire after 30 minutes of sending.

Image description: Mail send to customer:
![Capture12](https://user-images.githubusercontent.com/43162312/114268758-7bb4a780-9a20-11eb-84fe-971c00328bd7.JPG)


Image description: When open url send on mail:
![Capture123](https://user-images.githubusercontent.com/43162312/114268829-d64e0380-9a20-11eb-851b-17fe92a35ef6.JPG)

Image description: API :
![Capture1234](https://user-images.githubusercontent.com/43162312/114268894-2af17e80-9a21-11eb-89f0-bc56b71b1ece.JPG)


Requirements.txt:

asgiref==3.3.4 \
Django==3.2 \
django-background-tasks==1.2.5 \
django-compat==1.0.15 \
djangorestframework==3.12.4 \
python-decouple==3.4 \
pytz==2021.1 \
six==1.15.0 \
sqlparse==0.4.1 \
typing-extensions==3.7.4.3 

# to run project open 1st terminal and run cmd == python manage.py runserver
#for background task open 2nd terminal and run cmd == python manage.py process_tasks
