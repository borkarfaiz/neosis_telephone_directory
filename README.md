# Neosis Telphone Directory
It is a telephone directory that lets users add their contacts in the system. and there are features to search and sort the contacts. user first must signup to use all the features.

**[Assignment Link](https://docs.google.com/document/d/1mxy4IsKZ0kdMWYs0mbH_PTC7HMzfp06Mv5alVZ3Yq4o/edit#)**

## Setting up the Project
- First, you should install the docker. **[Install Docker](https://docs.docker.com/engine/install/)**
- Build the docker image.
    ```bash
    sudo docker-compose -f local.yml build
    ```
- Run the container
    ```bash
    sudo docker-compose -f local.yml up -d
    ```
Congratulation all setup has been completed nothing more to setup.


## Some Commands for docker
 - Making migrations
     ```bash
     docker-compose -f local.yml run --rm django python manage.py makemigrations
     ```
 - For django shell
     ```bash
     docker-compose -f local.yml run --rm django python manage.py shell
     ```
 - For opening the bash
     ```bash
     docker-compose -f local.yml run --rm django bash
     ```
## Generate Fake data
 - Navigate to the project directory
     ```bash
     cd ~/NeosisAssignments/neosis_telephone_directory
     ```
 - open django shell
     ```bash
     sudo docker-compose -f local.yml run --rm django python manage.py shell_plus --ipython
     ```
 - Run the below script to generate the fake data
     ```ipython
    from datetime import date
    from dateutil.relativedelta import relativedelta
    from random import randint
    import random

    from neosis_telephone_directory.users.models import User
    from neosis_telephone_directory.telephone_directory.models import ContactViewCount, Contacts




    # generate fake Contacts
    fake_data = [
        ('faiz', 'nazir', 'borkar'),
        ('salman', 'nazir', 'borkar'),
        ('tausif', 'nazir', 'borkar'),
        ('faizan', 'razzak', 'maalim'),
        ('manjiri', '', 'majrekar'),
        ('sagar', '', 'Narvekar'),
        ('arun', 'selvaraj', 'Naicker'),
        ('akshay', '', 'rajmane'),
        ('kaustubh', 'vinod', 'tandel'),
        ('eshant', '', 'bist'),
        ('jigar', '', 'lad'),
        ('ankur', '', 'sakar'),
        ('burhanuudin', '', 'baatliwala'),
        ('geeta', '', 'yaadav'),
        ('tushar', '', 'Naachan'),
        ('Prachi', '', 'savvarkar'),
        ('rakesh', '', 'samal'),
        ('benazir', '', 'mulla'),
        ('virkant', '', 'kadam'),
        ('shubham', '', 'gapat'),
        ('meena', '', 'tandel'),

    ]
    for user_id in User.objects.exclude(is_superuser=True).values_list('id', flat=True):
        for data in fake_data:
            first_name = data[0]
            middle_name = data[1]
            last_name = data[2]
            email = f"{last_name}_{first_name}@gmail.com"
            numbers = list('0123456789')		
            mobile_number = "9" + "".join(random.choice(numbers) for  i in range(9))
            contact, created =  Contacts.objects.get_or_create(
                user_id=user_id, first_name=first_name, last_name=last_name
            )
            contact.middle_name = middle_name
            contact.email = email
            contact.mobile_number = mobile_number
            contact.save()

    # ContactViewCount Creation
    today = date.today()
    contact_ids = Contacts.objects.values_list('id', flat=True)
    for contact_id in contact_ids:
        for i in range(10, 0, -1):
            count = randint(5, 20)
            date_to_add = today - relativedelta(days=i)
            contact_view, created = ContactViewCount.objects.get_or_create(
                count_date=date_to_add, contact_id=contact_id
            )
            contact_view.count = F('count') + count
            contact_view.save() 

     ```
