from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'ID': 1,
        'Title': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'Salary': 'Rs. 10,00,000'
    },
    {
        'ID': 2,
        'Title': 'Data Scintest',
        'Location': 'Bengaluru, India',
        'Salary': 'Rs. 20,00,000'
    },
    {
        'ID': 3,
        'Title': 'Back-end Developer',
        'Location': 'Bengaluru, India',
      
    },
]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def job_list():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
