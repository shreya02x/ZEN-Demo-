import time
import random
import csv
from datetime import datetime
from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Config
RUN_DURATION = 180  # seconds (3 min)
LOG_CSV = "zen_trl6_run.csv"
PLOT_PNG = "zen_trl6_actions.png"
REPORT_PDF = "zen_trl6_plus_report.pdf"

# Flask app for Fog simulation
app = Flask(__name__)

@app.route('/job', methods=['POST'])
def fog_job():
    data = request.get_json()
    job_id = data.get('job_id')
    out_file = f"result_{job_id}.png"
    os.makedirs("results", exist_ok=True)
    plt.figure()
    plt.plot([1, 2, 3], [random.randint(0, 10) for _ in range(3)])
    plt.title(f"Fog Job {job_id}")
    plt.savefig(os.path.join("results", out_file))
    plt.close()
    print(f"[FOG] processed job {job_id} -> results/{out_file}")
    return jsonify({"job_id": job_id, "result": {"out_file": out_file, "status": "done"}})

# Scheduler simulation
def run_scheduler():
    start_time = time.time()
    logs = []
    print(f"[{datetime.now()}] Scheduler starting...")

    while time.time() - start_time < RUN_DURATION:
        solar = random.choice([50, 300, 600, 800])
        battery = max(0, min(100, random.randint(30, 80)))
        task_type = random.choice(["light", "heavy"])

        if solar >= 600 and battery > 20:
            action = "RUN_LOCAL"
        elif solar >= 300 and battery > 10:
            action = "OFFLOAD"
            job_id = f"job-{int(time.time())}"
            print(f"[SCHED] Offloading job {job_id} to fog")
            with app.test_client() as c:
                resp = c.post("/job", json={"job_id": job_id})
                print(f"[SCHED] Fog response: {resp.json}")
        else:
            action = "PAUSE"

        log_entry = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "SIMULATED", f"{solar} W/m2 ({int(solar/8)}%)",
            f"{battery}%", task_type, action
        ]
        logs.append(log_entry)
        print(f"[SCHED] {log_entry[0]} | src={log_entry[1]} | solar={log_entry[2]} | batt={log_entry[3]} | task={task_type} | action={action}")
        time.sleep(6)

    return logs

# Save CSV
def save_csv(logs, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Source", "Solar", "Battery", "TaskType", "Action"])
        writer.writerows(logs)
    print(f"[{datetime.now()}] Wrote CSV to {path}")

# Make plot
def make_plot(logs, path):
    times = [row[0][-8:] for row in logs]
    solar_vals = [int(row[2].split()[0]) for row in logs]
    batt_vals = [int(row[3][:-1]) for row in logs]
    actions = [row[5] for row in logs]

    plt.figure(figsize=(10, 5))
    plt.plot(times, solar_vals, label="Solar W/m2")
    plt.plot(times, batt_vals, label="Battery %")
    plt.xticks(rotation=45)
    plt.ylabel("Value")
    plt.legend()
    plt.title("ZEN TRL6+ Simulation Actions")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    print(f"[{datetime.now()}] Wrote plot to {path}")

# Make PDF
def make_pdf(path_pdf, png_path, csv_path):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "ZEN - TRL6+ Demo Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, "This report shows the results of a 3-minute TRL6+ simulation of the Zero Emissions Node (ZEN) scheduler and fog node job processing.")

    pdf.ln(5)
    pdf.cell(0, 8, "Simulation Graph:", ln=True)
    pdf.image(png_path, x=10, y=None, w=180)

    pdf.ln(80)
    pdf.cell(0, 8, "For detailed logs, see the attached CSV file.", ln=True)

    pdf.output(path_pdf)
    print(f"[{datetime.now()}] Wrote PDF to {path_pdf}")

# Main run
def run_demo_and_report():
    logs = run_scheduler()
    save_csv(logs, LOG_CSV)
    make_plot(logs, PLOT_PNG)
    make_pdf(REPORT_PDF, PLOT_PNG, LOG_CSV)

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting zen_trl6_plus_report demo")
    run_demo_and_report()
