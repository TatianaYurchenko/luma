# https://dev-gs.qa-playground.com/api/v1
#

import requests
HOST = "https://dev-gs.qa-playground.com/api/v1"
response = requests.post(
    url=f"{HOST}/setup",
    headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE2NTU1MDY1LCJpYXQiOjE3MTU5NTUwNjUsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjJmZGVhODkyLTI0ZGEtNDgxNi1iOGU3LWMyMzJiMzBhNzM1NyIsImVtYWlsIjoidGFmODgxNTZAbWFpbC5ydSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ2l0aHViIiwicHJvdmlkZXJzIjpbImdpdGh1YiJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzEwMjg1MzQ0NT92PTQiLCJlbWFpbCI6InRhZjg4MTU2QG1haWwucnUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiVGF0aWFuYVl1cmNoZW5rbyIsInByb3ZpZGVyX2lkIjoiMTAyODUzNDQ1Iiwic3ViIjoiMTAyODUzNDQ1IiwidXNlcl9uYW1lIjoiVGF0aWFuYVl1cmNoZW5rbyJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6InJlY292ZXJ5IiwidGltZXN0YW1wIjoxNzE1OTU1MDQwfV0sInNlc3Npb25faWQiOiJlYzg1M2EwOS1kOTFjLTQzNDUtOTgyMS1iNjNkZjQzZmM3YjUiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.Or5qU94bsVlCImDmxDkO6n4I13ndtVyPYxsuVDRDKcI",
"X-Task-Id": "API-1"})