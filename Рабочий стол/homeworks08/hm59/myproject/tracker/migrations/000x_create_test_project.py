from django.db import migrations

def create_test_project(apps, schema_editor):
    Project = apps.get_model('tracker', 'Project')
    Task = apps.get_model('tracker', 'Task')

    project = Project.objects.create(
        start_date='2023-01-01',
        end_date=None,
        title='Тестовый проект',
        description='Этот проект создан для тестирования.'
    )

    for task in Task.objects.all():
        task.project = project
        task.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', 'previous_migration_name'),
    ]

    operations = [
        migrations.RunPython(create_test_project),
    ]
