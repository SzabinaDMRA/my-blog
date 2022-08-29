from app.models import ContactRequest


def GetContactList():
    get_all_contact = ContactRequest.select(
        ContactRequest.name,
        ContactRequest.email,
        ContactRequest.category,
        ContactRequest.priority
    )

    contactList = []

    for contact in get_all_contact:
        contactList.append(
            dict(
                name=contact.name,
                email=contact.email,
                category=contact.category,
                priority=contact.priority
            )
        )

    return contactList


def SaveContactRequest(name, email, category, priority, message):
    try:
        ContactRequest.create(
            name=name,
            email=email,
            category=category,
            priority=priority,
            message=message
        )

        return True
    except Exception as error:
        print(error)

        return False
