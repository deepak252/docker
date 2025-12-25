import random
from faker import Faker

fake = Faker()


DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "company.com", "xyz.com", "example.com", "apple.com"]
INDUSTRIES = [
    "Technology",
    "Finance",
    "Healthcare",
    "E-commerce",
    "Education",
    "Manufacturing",
    "Retail",
    "Logistics",
    "Real Estate",
    "Media",
    "Energy",
]
COMPANY_SUFFIXES = suffixes = [
    "Technologies", "Solutions", "Systems", "Labs",
    "Group", "Industries", "Holdings", "Corp", "Ltd"
]

def random_company_name():
    company_name = fake.company()
    suffix = random.choice(COMPANY_SUFFIXES)

    if company_name.lower().endswith(suffix.lower()):
        return company_name

    return f"{company_name} {suffix}"

def random_industry():
    return random.choice(INDUSTRIES)

def random_country_id(max_id=5):
    return random.randint(1, max_id)


def random_media_type():
    return random.choice(["IMAGE", "VIDEO", "PDF"])

def random_gender():
    return random.choice(["M", "F"])

def random_age():
    return random.randint(18, 65)


def random_budget(min_val=5000, max_val=100000):
    return random.randint(min_val, max_val)

def random_name(gender = 'M'):
    if gender == 'F':
        return fake.name_female()
    return fake.name_male()

def name_to_email(name = '', domains = DOMAINS):
    email_prefix = name.lower().replace(" ", "")
    return f"{email_prefix}@{random.choice(domains)}"

def random_email(domains = DOMAINS):
    return fake.email(domain=random.choice(domains))

def random_sentence(max_words=10):
    return fake.sentence(nb_words=max_words)


def random_date_recent(days=90):
    return fake.date_between(start_date=f"-{days}d", end_date="today")


# def execute(callback, label = ""):
#     start = time.time()

#     callback()

#     end = time.time()

#     print(f"Time taken : {label} : {(end - start) * 1000:.2f} ms") # 1315.68 ms