import uvicorn
import os
import sys

# Add current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Default configuration
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("DEBUG", "false").lower() == "true"
    
    print(f"Starting VisoBERT API on {host}:{port}...")
    uvicorn.run("api.main:app", host=host, port=port, reload=reload)
