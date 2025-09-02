from django.db import models
from django.contrib.auth.models import User

DIFFICULTY_CHOICES = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)

CATEGORY_CHOICES = (
    ('Array', 'Array'),
    ('String', 'String'),
    ('LinkedList', 'LinkedList'),
    ('Tree', 'Tree'),
    ('Graph', 'Graph'),
    ('DP', 'DP'),
    ('Backtracking', 'Backtracking'),
    ('Other', 'Other'),
)

STATUS_CHOICES = (
    ('Solved', 'Solved'),
    ('Attempted', 'Attempted'),
    ('Unsolved', 'Unsolved'),
)

class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems")
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unsolved')
    date_solved = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title