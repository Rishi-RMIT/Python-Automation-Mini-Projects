from datetime import datetime
from docxtpl import DocxTemplate
import pandas as pd

#open with name arg
doc = DocxTemplate("template-manager-info.docx")

#sender variables
my_name = "AeroBOT"
my_phone = "(123) 456-789"
my_email = "AeroBOT@gmail.com"
my_address = "124 La Trobe Street, Melbourne, VIC 3000"
today_date = datetime.today().strftime("%d %b, %Y")

#fill in sender variables
context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
           'today_date': today_date}

#recipient variables in dataframe
df = pd.read_csv('fake_data.csv')

for index, entry in df.iterrows():
    recipient_context = {
        'hiring_manager_name' : entry['name'],
        'address' : entry['address'],
        'phone_number' : entry['phone_number'],
        'email' : entry['e-mail'],
        'job_position' : entry['job'],
        'company_name' : entry['company']
    }

    recipient_context.update(context)

    #save & generate docx
    doc.render(recipient_context)
    doc.save(f"generated_doc_{index}.docx")