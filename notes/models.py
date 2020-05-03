from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files import File

from pygments import highlight  # new
from pygments.formatters.html import HtmlFormatter  # new
from pygments.lexers import  guess_lexer  # new
from pygments.styles import get_all_styles


STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
# Create your models here.
SEMESTER = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
)
STREAM = (
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
    ('CV', 'CV'),
    ('BCA', 'BCA'),
    ('BBA', 'BBA'),
    ('MCA', 'MCA'),
    ('MBA', 'MBA'),
    ('LLB', 'LLB'),
    ('LLM', 'LLM'),
    ('B-ARCH', 'B-ARCH'),
    ('BBA-HEM', 'BBA-HEM'),
    ('B-DES', 'B-DES'),
)
CHOICES = (
    ('plaintext', 'plaintext'),
    ('language-c', 'C'),
    ('language-csharp', 'C#'),
    ('language-cpp', 'C++'),
    ('language-python', 'Python'),
    ('language-java', 'Java'),
    ('language-javascript', 'JavaScript'),
    ('language-kotlin', 'Kotlin'),
    ('language-html,', 'HTML,'),
    ('language-css', 'CSS'),
    ('language-php7', 'PHP7'),
    ('language-arm', 'ARM'),
    ('language-xml', 'XML'),
    ('language-makefile', 'Makefile'),
    ('language-objective-c', 'Objective-C'),
    ('language-sql', 'SQL'),
    ('language-perl', 'Perl'),
    ('language-shell', 'Shell'),
    ('language-apache', 'Apache'),
    ('language-bash', 'Bash'),
    ('language-coffeescript', 'CoffeeScript'),
    ('language-diff', 'Diff'),
    ('language-go', 'Go'),
    ('language-http', 'HTTP'),
    ('language-json', 'JSON'),
    ('language-lesslua', 'LessLua'),
    ('language-markdown', 'Markdown'),
    ('language-ruby', 'Ruby'),
    ('language-rust', 'Rust'),
    ('language-scss', 'SCSS'),
    ('language-swift', 'Swift'),
    ('language-ini', 'INI'),
    ('language-typescript', 'TypeScript'),
    ('language-yaml', 'YAML'),
)


class LabPost(models.Model):

    title = models.CharField(max_length=100)
    subject = models.CharField(default="abcd", max_length=100)
    file = models.FileField(null=True, upload_to='files/', blank=True)

    stream = models.CharField(
        default='CSE', max_length=30, choices=STREAM)

    semester = models.IntegerField(default=1, choices=SEMESTER)

    description = models.TextField(blank=True, max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    postbody = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    highlighted = models.TextField()  # new
    style = models.CharField(choices=STYLE_CHOICES,
                             default='perldoc', max_length=100)

    def save(self, *args, **kwargs):  # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = guess_lexer(self.postbody)

        # linenos = 'table' if self.linenos else False
        linenos = 'table'
        formatter = HtmlFormatter(style=self.style,
                                  full=True)
        self.highlighted = highlight(self.postbody, lexer, formatter)
        super(LabPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_post', kwargs={'pk': self.pk})


class FilePost(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(default="", max_length=100)
    file0 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file1 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file2 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file3 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file4 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file5 = models.FileField(null=True, upload_to='filepost/', blank=True)
    file6 = models.FileField(null=True, upload_to='filepost/', blank=True)

    stream = models.CharField(
        default='CSE', max_length=30, choices=STREAM)

    semester = models.IntegerField(default=1, choices=SEMESTER)
    list = ['filepost.file0', 'filepost.file1',
            'filepost.file2', 'filepost.file3'
            'filepost.file4', 'filepost.file5', 'filepost.file6'
            ]

    description = models.TextField(blank=True, max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    language = models.CharField(
        default='plaintext', max_length=30, choices=CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('material', kwargs={'pk': self.pk})
