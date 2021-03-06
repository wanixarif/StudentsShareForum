# Generated by Django 3.0.4 on 2020-03-24 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0016_auto_20200323_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
                ('file0', models.FileField(blank=True, null=True, upload_to='filepost/')),
                ('file1', models.FileField(blank=True, null=True, upload_to='filepost/')),
                ('file2', models.FileField(blank=True, null=True, upload_to='filepost/')),
                ('stream', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECH', 'MECH'), ('CV', 'CV'), ('BCA', 'BCA'), ('BBA', 'BBA'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('LLB', 'LLB'), ('LLM', 'LLM'), ('B-ARCH', 'B-ARCH'), ('BBA-HEM', 'BBA-HEM'), ('B-DES', 'B-DES')], default='CSE', max_length=30)),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=1)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('language', models.CharField(choices=[('plaintext', 'plaintext'), ('language-c', 'C'), ('language-csharp', 'C#'), ('language-cpp', 'C++'), ('language-python', 'Python'), ('language-java', 'Java'), ('language-javascript', 'JavaScript'), ('language-kotlin', 'Kotlin'), ('language-html,', 'HTML,'), ('language-css', 'CSS'), ('language-php7', 'PHP7'), ('language-arm', 'ARM'), ('language-xml', 'XML'), ('language-makefile', 'Makefile'), ('language-objective-c', 'Objective-C'), ('language-sql', 'SQL'), ('language-perl', 'Perl'), ('language-shell', 'Shell'), ('language-apache', 'Apache'), ('language-bash', 'Bash'), ('language-coffeescript', 'CoffeeScript'), ('language-diff', 'Diff'), ('language-go', 'Go'), ('language-http', 'HTTP'), ('language-json', 'JSON'), ('language-lesslua', 'LessLua'), ('language-markdown', 'Markdown'), ('language-ruby', 'Ruby'), ('language-rust', 'Rust'), ('language-scss', 'SCSS'), ('language-swift', 'Swift'), ('language-ini', 'INI'), ('language-typescript', 'TypeScript'), ('language-yaml', 'YAML')], default='plaintext', max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
