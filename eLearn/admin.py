from django.contrib import admin

# Register your models here.
from .models import Registration, SystemSettings, SiteSubscribers, Events, EventDetails, ContactUS, HaederSlider, Members, ourTeam
# from .models.registration import Registration
# from .models.systemSettings import SystemSettings
# from .models.siteSubscribers import SiteSubscribers
# from .models.events import Events
# from .models.eventDetails import EventDetails
# from .models.contactUS import ContactUS
# from .models.haederSlider import HaederSlider
# from .models.members import Members
# from .models.ourteam import ourTeam

admin.site.register(Registration)
admin.site.register(SystemSettings)
admin.site.register(SiteSubscribers)
admin.site.register(Events)
admin.site.register(EventDetails)
admin.site.register(ContactUS)
admin.site.register(HaederSlider)
admin.site.register(Members)
admin.site.register(ourTeam)
