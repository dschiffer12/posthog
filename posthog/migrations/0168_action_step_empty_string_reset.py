# Generated by Django 3.1.8 on 2021-05-26 23:18

from django.db import migrations


def action_step_empty_string_reset(apps, schema_editor):
    try:
        ActionStep = apps.get_model("posthog", "ActionStep")
        for obj in ActionStep.objects.all():
            obj.href = obj.href or None
            obj.text = obj.text or None
            obj.selector = obj.selector or None
            obj.url = obj.url or None
            obj.save()
    except:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0167_feature_flag_override"),
    ]

    operations = [
        migrations.RunPython(action_step_empty_string_reset, migrations.RunPython.noop, elidable=True),
    ]
