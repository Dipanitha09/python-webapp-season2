from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analysis",
    'location': "New York, USA",
    'salary': '1000000'
  },
  {
    'id': 2,
    'title': "Data Engineer",
    'location': "Delhi, India",
    'salary': '1500000'
  },
  {
    'id': 3,
    'title': "Data Miner",
    'location': "Banglore, India",
    'salary': '1200000'
  },
  {
    'id': 4,
    'title': "Fashion Designer",
    'location': "New York, USA",
    'salary': '1800000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="ZYRA")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
