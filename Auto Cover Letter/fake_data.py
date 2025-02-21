from faker import Faker
import pandas as pd

fake = Faker()

#generate fake profiles & turn into dataframe w 🐼's
profiles = [fake.profile() for i in range(10)]
df = pd.DataFrame(profiles)

#only select desired columns
df = df[['name', 'mail', 'address', 'job', 'company']]

print(df)

#generate fake phone number & add to dataframe
numbers = profiles = [fake.basic_phone_number() for j in range(10)]
df['phone_number'] = numbers

print(df.columns)

#rename column
df.rename(columns={'mail' : 'e-mail'}, inplace=True)

#turn df into csv
df.to_csv('fake_data.csv', index=False)