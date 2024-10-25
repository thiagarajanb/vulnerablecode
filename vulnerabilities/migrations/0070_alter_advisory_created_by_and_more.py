# Generated by Django 4.2.15 on 2024-10-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0069_exploit_delete_kev"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advisory",
            name="created_by",
            field=models.CharField(
                help_text="Fully qualified name of the importer prefixed with themodule name importing the advisory. Eg:vulnerabilities.pipeline.nginx_importer.NginxImporterPipeline",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="packagechangelog",
            name="software_version",
            field=models.CharField(
                default="34.0.2",
                help_text="Version of the software at the time of change",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="vulnerabilitychangelog",
            name="software_version",
            field=models.CharField(
                default="34.0.2",
                help_text="Version of the software at the time of change",
                max_length=100,
            ),
        ),
    ]