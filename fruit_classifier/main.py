import time
import subprocess
import uvicorn

def start_dagster():
    """Starts Dagster Dev, which includes Dagit UI and the daemon."""
    print("Starting Dagster with 'dagster dev'...")
    dagster_process = subprocess.Popen(["dagster", "dev", "--port", "3002" ])
    return dagster_process

def run_dagster_pipeline():
    """Runs the Dagster pipeline to generate the trained model."""
    print("Running Dagster pipeline...")
    subprocess.run(["dagster", "job", "execute", "-m", "diabetesProj.assets"], check=True)

def start_fastapi():
    """Starts the FastAPI server."""
    print("Starting FastAPI server...")
    uvicorn.run("src.models.predict:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    # Start Dagster
    dagster_process = start_dagster()
    time.sleep(20)  # Wait for Dagster to start

    # Run the Dagster pipeline (train model)
    run_dagster_pipeline()

    # After model training, start FastAPI
    start_fastapi()

    # If FastAPI is interrupted, terminate Dagster process
    try:
        pass
    except KeyboardInterrupt:
        print("Shutting down...")
        dagster_process.terminate()
