from hospital.models import Patient
from django.dispatch import receiver
from django.signals import pre_save, post_save


@receiver(models.signals.pre_save)
def pre_add_movement_history(instance, sender, *args, **kwargs):
    print('PRE_SAVE:')
    print(sender)
    print(instance)

@receiver(models.signals.post_save)
def post_add_movement_history(instance, sender, *args, **kwargs):
    print('POST_SAVE:')
    print(sender)
    print(instance)
