from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    """ clients of the funnel """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    company = db.Column(db.String(50))
    position = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    extra_phone = db.Column(db.String(50))
    sector = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    linkedin = db.Column(db.String(50))
    source = db.Column(db.String(50))
    observations = db.Column(db.String(400))

    def __init__(self, name, lastName, company, position, email, phone, extraPhone, sector, city, country, linkedin, source, observations):
        self.name = name
        self.last_name = lastName
        self.company = company
        self.position = position
        self.email = email
        self.phone = phone
        self.extra_phone = extraPhone
        self.sector = sector
        self.city = city
        self.country = country
        self.linkedin = linkedin
        self.source = source
        self.observations = observations

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.last_name,
            "company": self.company,
            "position": self.position,
            "email": self.email,
            "phone": self.phone,
            "extraPhone": self.extra_phone,
            "sector": self.sector,
            "city": self.city,
            "country": self.country,
            "linkedin": self.linkedin,
            "source": self.source,
            "observations": self.observations
        }

class Opportunity(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    project = db.Column(db.String(50))
    project_description = db.Column(db.String(300))
    cost = db.Column(db.String(50))
    time = db.Column(db.String(50))
    reach = db.Column(db.String(50)) 
    
    def __init__(self, project, projectDescription, cost, time, reach):
        self.project = project
        self.project_description = projectDescription
        self.cost = cost
        self.time = time
        self.reach = reach

    def serialize(self):
        return {
            "id": self.id,
            "project": self.project,
            "projectDescription": self.project_description,
            "cost": self.cost,
            "time": self.time,
            "reach": self.reach
        }

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }