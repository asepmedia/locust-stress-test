import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
  wait_time = between(1, 2)

  @task
  def index_page(self):
    self.client.get("/learning")
  
  @task
  def video_page(self):
    self.client.get("/learning_detail/412")

  def on_start(self):
    self.client.post("/login", data={"email":"asep@indah.com", "password":"secret"})