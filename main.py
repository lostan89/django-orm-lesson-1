import os
import django


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    django.setup()

    from datacenter.models import Passcard

    objects = Passcard.objects.all()
    first_object = objects[0]
    print(f"""
        owner_name: {first_object.owner_name},
        passcode: {first_object.passcode},
        created_at: {first_object.created_at}
        is_active: {first_object.is_active}
        """)
    active_passcard = Passcard.objects.filter(is_active=True)
    print("Количество пропусков:", Passcard.objects.count())
    print("Активных пропусков", len(active_passcard))


if __name__ == "__main__":
    main()
